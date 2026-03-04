import json
import os
import re
import time
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

BASE_URL = os.getenv("SN_BASE_URL", "https://xeretecdev.service-now.com")
TOKEN_URL = os.getenv("SN_TOKEN_URL", f"{BASE_URL}/oauth_token.do")
CLIENT_ID = os.getenv("SN_CLIENT_ID", "")
CLIENT_SECRET = os.getenv("SN_CLIENT_SECRET", "")
MAX_RPM = int(os.getenv("SN_MAX_RPM", "120"))
MAX_TABLES = int(os.getenv("SN_MAX_TABLES", "2000"))
OUT = Path("generated")

LAST_REQ_TS = 0.0
ACCESS_LIMITS = []


def throttle():
    global LAST_REQ_TS
    interval = 60.0 / max(MAX_RPM, 1)
    now = time.time()
    wait = interval - (now - LAST_REQ_TS)
    if wait > 0:
        time.sleep(wait)
    LAST_REQ_TS = time.time()


def http_json(method, url, headers=None, body=None, retries=4):
    headers = headers or {}
    for i in range(retries):
        try:
            throttle()
            req = urllib.request.Request(url, method=method, headers=headers)
            data = body.encode("utf-8") if isinstance(body, str) else body
            with urllib.request.urlopen(req, data=data, timeout=30) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw), None
        except Exception as e:
            if i == retries - 1:
                return None, str(e)
            time.sleep([1, 2, 4, 8][min(i, 3)])
    return None, "max retries"


def get_token():
    if not CLIENT_ID or not CLIENT_SECRET:
        return None, "Missing SN_CLIENT_ID or SN_CLIENT_SECRET environment variables"
    body = urllib.parse.urlencode(
        {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
        }
    )
    data, err = http_json(
        "POST",
        TOKEN_URL,
        headers={"Content-Type": "application/x-www-form-urlencoded", "Accept": "application/json"},
        body=body,
    )
    if err:
        return None, err
    return data.get("access_token"), None


def api_get_table(token, table, fields, query=None, limit=100, cap=1000):
    results, offset = [], 0
    while offset < cap:
        params = {
            "sysparm_limit": min(limit, cap - offset),
            "sysparm_offset": offset,
            "sysparm_fields": ",".join(fields),
            "sysparm_display_value": "false",
            "sysparm_exclude_reference_link": "true",
        }
        if query:
            params["sysparm_query"] = query
        url = f"{BASE_URL}/api/now/table/{table}?{urllib.parse.urlencode(params)}"
        data, err = http_json("GET", url, headers={"Accept": "application/json", "Authorization": f"Bearer {token}"})
        if err:
            return results, err
        batch = data.get("result", [])
        results.extend(batch)
        if len(batch) < params["sysparm_limit"]:
            break
        offset += len(batch)
    return results, None


def extract_edges(kind, name, sys_id, script):
    if not script:
        return []
    src = f"{kind}:{name}({sys_id})"
    edges = []
    patterns = [
        (r"GlideRecord\(['\"]([a-zA-Z0-9_]+)['\"]\)", "table"),
        (r"gs\.eventQueue\(['\"]([a-zA-Z0-9_.]+)['\"]", "event"),
        (r"sn_ws\.RESTMessageV2\(['\"]([a-zA-Z0-9_ .:-]+)['\"]", "rest_message"),
    ]
    for pat, t in patterns:
        for m in re.finditer(pat, script):
            edges.append({"source": src, "target": f"{t}:{m.group(1)}", "evidence": m.group(0), "artifact_sys_id": sys_id})
    return edges


def write_minimal_outputs(error):
    for p in [OUT, OUT / "DATA_MODEL", OUT / "PROCESSES", OUT / "INTEGRATIONS", OUT / "SECURITY", OUT / "REPORTS"]:
        p.mkdir(parents=True, exist_ok=True)

    files = {
        "README.md": "# ServiceNow Instance Autodocumentation\n\nGeneration could not complete due to connectivity/auth limitations.\n",
        "INVENTORY.md": "# Inventory\n\nNo inventory collected.\n",
        "ACCESS_LIMITATIONS.md": f"# Access Limitations\n\n- {error}\n",
        "DATA_MODEL/TABLE_CATALOG.md": "# Table Catalog\n\nNo table data collected.\n",
        "DATA_MODEL/REFERENCE_GRAPH.mmd": "graph LR\n",
        "PROCESSES/PROCESS_INDEX.md": "# Process Index\n\nNo process artifacts collected.\n",
        "PROCESSES/PROCESS_CHAINS.md": "# Process Chains\n\nNo dependency chains collected.\n",
        "PROCESSES/DEPENDENCY_GRAPH.mmd": "graph LR\n",
        "INTEGRATIONS/INTEGRATION_CATALOG.md": "# Integration Catalog\n\nNo integration artifacts collected.\n",
        "SECURITY/ACL_MATRIX.md": "# ACL Matrix\n\nNo ACL artifacts collected.\n",
        "REPORTS/artifact_index.json": json.dumps({"error": error}, indent=2),
        "REPORTS/dependency_edges.json": "[]\n",
        "REPORTS/table_dictionary_summary.json": "{}\n",
    }
    for rel, content in files.items():
        (OUT / rel).write_text(content)


def main():
    token, err = get_token()
    if err:
        write_minimal_outputs(f"OAuth/token failure: {err}")
        print("Generated minimal outputs with access limitations.")
        return

    inventory, err = api_get_table(token, "sys_db_object", ["name", "label", "sys_id", "sys_scope"], cap=MAX_TABLES)
    if err:
        write_minimal_outputs(f"sys_db_object read failed: {err}")
        print("Generated minimal outputs with access limitations.")
        return

    table_names = [r.get("name") for r in inventory if r.get("name")]
    dict_rows, derr = api_get_table(token, "sys_dictionary", ["name", "element", "internal_type", "reference", "mandatory", "sys_id"], cap=8000)
    if derr:
        ACCESS_LIMITS.append(f"sys_dictionary: {derr}")
        dict_rows = []

    br_rows, berr = api_get_table(token, "sys_script", ["sys_id", "name", "collection", "when", "script", "active"], query="active=true", cap=4000)
    if berr:
        ACCESS_LIMITS.append(f"sys_script: {berr}")
        br_rows = []

    for p in [OUT, OUT / "DATA_MODEL", OUT / "PROCESSES", OUT / "INTEGRATIONS", OUT / "SECURITY", OUT / "REPORTS"]:
        p.mkdir(parents=True, exist_ok=True)

    refs = [(r["name"], r["element"], r["reference"], r.get("sys_id")) for r in dict_rows if r.get("reference")]
    edges = []
    for br in br_rows:
        edges.extend(extract_edges("business_rule", br.get("name"), br.get("sys_id"), br.get("script", "")))

    summary = defaultdict(lambda: {"field_count": 0, "reference_field_count": 0, "sys_id": "", "label": ""})
    inv_map = {r["name"]: r for r in inventory if r.get("name")}
    for t in table_names:
        summary[t]["sys_id"] = inv_map[t].get("sys_id")
        summary[t]["label"] = inv_map[t].get("label")
    for d in dict_rows:
        t = d.get("name")
        if not t:
            continue
        summary[t]["field_count"] += 1
        if d.get("reference"):
            summary[t]["reference_field_count"] += 1

    (OUT / "README.md").write_text(f"# ServiceNow Instance Autodocumentation\n\n- Tables inventoried: {len(table_names)}\n- Business rules analyzed: {len(br_rows)}\n- Dependency edges extracted: {len(edges)}\n")
    (OUT / "INVENTORY.md").write_text("# Inventory\n\n" + "\n".join([f"- `{t}` (`{inv_map[t].get('sys_id')}`)" for t in sorted(table_names)[:500]]))
    (OUT / "ACCESS_LIMITATIONS.md").write_text("# Access Limitations\n\n" + ("\n".join([f"- {x}" for x in ACCESS_LIMITS]) if ACCESS_LIMITS else "- None observed for accessed tables."))
    (OUT / "DATA_MODEL" / "TABLE_CATALOG.md").write_text("# Table Catalog\n\n" + "\n".join([f"- `{t}` ({summary[t]['label']}) fields={summary[t]['field_count']} refs={summary[t]['reference_field_count']} sys_id=`{summary[t]['sys_id']}`" for t in sorted(table_names)[:600]]))
    (OUT / "DATA_MODEL" / "REFERENCE_GRAPH.mmd").write_text("graph LR\n" + "\n".join([f"  {a}[{a}] -->|{f}| {b}[{b}]" for a, f, b, _ in refs[:400]]))

    out_degree = Counter([e["source"] for e in edges])
    (OUT / "PROCESSES" / "PROCESS_INDEX.md").write_text("# Process Index\n\n## Business Rules\n" + "\n".join([f"- `{b.get('name')}` (`{b.get('sys_id')}`) table `{b.get('collection')}` when `{b.get('when')}`" for b in br_rows[:1000]]))
    (OUT / "PROCESSES" / "PROCESS_CHAINS.md").write_text("# Process Chains\n\n## Top 25 Critical Processes\n" + "\n".join([f"- `{s}` -> {c} downstream edges" for s, c in out_degree.most_common(25)]))
    (OUT / "PROCESSES" / "DEPENDENCY_GRAPH.mmd").write_text("graph LR\n" + "\n".join([f"  A{i}[\"{e['source'][:80]}\"] --> B{i}[\"{e['target'][:80]}\"]" for i, e in enumerate(edges[:500])]))

    (OUT / "INTEGRATIONS" / "INTEGRATION_CATALOG.md").write_text("# Integration Catalog\n\nGenerated via static analysis of business rule scripts for event/rest usage.\n")
    (OUT / "SECURITY" / "ACL_MATRIX.md").write_text("# ACL Matrix\n\nACL extraction is not included in this lightweight run. Extend crawler to `sys_security_acl` tables when access is available.\n")

    (OUT / "REPORTS" / "artifact_index.json").write_text(json.dumps({"sys_db_object": len(table_names), "sys_dictionary": len(dict_rows), "sys_script": len(br_rows)}, indent=2))
    (OUT / "REPORTS" / "dependency_edges.json").write_text(json.dumps(edges, indent=2))
    (OUT / "REPORTS" / "table_dictionary_summary.json").write_text(json.dumps(summary, indent=2))
    print("Generated documentation in ./generated")


if __name__ == "__main__":
    main()
