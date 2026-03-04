import json
import os
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape


def load_env_file(path=".env"):
    env_path = Path(path)
    if not env_path.exists():
        return
    for line in env_path.read_text(encoding="utf-8").splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or "=" not in stripped:
            continue
        key, value = stripped.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


load_env_file()


def env_first(*keys, default=None):
    for key in keys:
        value = os.getenv(key)
        if value is not None and str(value).strip():
            return str(value).strip()
    return default


def env_int(*keys, default):
    value = env_first(*keys, default=str(default))
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


def normalize_cap(value):
    if value is None:
        return None
    try:
        parsed = int(value)
    except (TypeError, ValueError):
        return None
    return None if parsed <= 0 else parsed


def as_bool(value):
    if isinstance(value, bool):
        return value
    if value is None:
        return False
    return str(value).strip().lower() in {"1", "true", "yes", "y"}


def safe_text(value):
    return "" if value is None else str(value).strip()


def md_escape(value):
    return safe_text(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def escape_mermaid(value):
    return md_escape(value).replace('"', "'")


def markdown_table(headers, rows):
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(["---"] * len(headers)) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(md_escape(cell) for cell in row) + " |")
    return "\n".join(lines)


def write_text(path, content):
    path.write_text(content, encoding="utf-8")


def write_json(path, payload):
    path.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def docx_paragraph(text, style="normal"):
    style_map = {
        "title": {"bold": True, "size": "36"},
        "heading": {"bold": True, "size": "28"},
        "subheading": {"bold": True, "size": "24"},
        "normal": {"bold": False, "size": "22"},
    }
    style_cfg = style_map.get(style, style_map["normal"])
    text_value = safe_text(text)

    run_props = [f'<w:sz w:val="{style_cfg["size"]}"/>']
    if style_cfg["bold"]:
        run_props.insert(0, "<w:b/>")
    run_props_xml = "<w:rPr>" + "".join(run_props) + "</w:rPr>"
    paragraph_props = '<w:pPr><w:spacing w:after="120"/></w:pPr>'

    if not text_value:
        return f"<w:p>{paragraph_props}</w:p>"

    return (
        "<w:p>"
        f"{paragraph_props}"
        "<w:r>"
        f"{run_props_xml}"
        f'<w:t xml:space="preserve">{xml_escape(text_value)}</w:t>'
        "</w:r>"
        "</w:p>"
    )


def write_docx(path, paragraphs):
    path.parent.mkdir(parents=True, exist_ok=True)

    body_xml = "".join(docx_paragraph(text, style) for style, text in paragraphs)
    document_xml = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
        "<w:body>"
        f"{body_xml}"
        '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/>'
        '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
        'w:header="708" w:footer="708" w:gutter="0"/></w:sectPr>'
        "</w:body>"
        "</w:document>"
    )
    content_types_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/word/document.xml" '
        'ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>'
        "</Types>"
    )
    package_rels_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" '
        'Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" '
        'Target="word/document.xml"/>'
        "</Relationships>"
    )
    document_rels_xml = (
        '<?xml version="1.0" encoding="UTF-8"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships"/>'
    )

    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("[Content_Types].xml", content_types_xml)
        archive.writestr("_rels/.rels", package_rels_xml)
        archive.writestr("word/document.xml", document_xml)
        archive.writestr("word/_rels/document.xml.rels", document_rels_xml)


def bullet_lines(values, formatter):
    lines = []
    for value in values:
        line = safe_text(formatter(value))
        if line:
            lines.append(f"- {line}")
    return lines


def build_ceo_brief_paragraphs(
    generated_at,
    elapsed_seconds,
    base_url,
    table_names,
    dict_rows,
    process_artifacts,
    integration_artifacts,
    event_registry_rows,
    acl_rows,
    scripted_acl_count,
    role_acl_count,
    edges,
    tables_by_risk,
    out_degree,
    integration_hosts,
    acl_operation_counter,
    access_limits,
):
    top_risk_tables = tables_by_risk[:5]
    top_dependencies = out_degree.most_common(5)
    top_hosts = integration_hosts.most_common(5)
    top_acl_ops = acl_operation_counter.most_common(5)

    paragraphs = [
        ("title", "ServiceNow CEO Briefing"),
        ("normal", f"Generated: {generated_at.strftime('%Y-%m-%d %H:%M:%S UTC')}"),
        ("normal", f"Platform: {base_url}"),
        ("normal", f"Generation duration: {elapsed_seconds} seconds"),
        ("normal", ""),
        ("heading", "Executive Snapshot"),
        ("normal", f"- Platform footprint: {len(table_names)} tables and {len(dict_rows)} dictionary fields."),
        ("normal", f"- Automation footprint: {len(process_artifacts)} process artifacts and {len(edges)} extracted code dependencies."),
        ("normal", f"- Integration footprint: {len(integration_artifacts)} integration artifacts and {len(event_registry_rows)} registered events."),
        (
            "normal",
            f"- Security footprint: {len(acl_rows)} ACLs, including {scripted_acl_count} scripted ACLs and {role_acl_count} ACLs with explicit roles.",
        ),
        ("normal", ""),
        ("heading", "Highest-Risk Tables"),
    ]

    if top_risk_tables:
        paragraphs.extend(
            ("normal", line)
            for line in bullet_lines(
                top_risk_tables,
                lambda item: (
                    f"{item[0]}: risk {item[1]['risk_score']}, fields {item[1]['field_count']}, "
                    f"business rules {item[1]['business_rule_count']}, ACLs {item[1]['acl_count']}"
                ),
            )
        )
    else:
        paragraphs.append(("normal", "- No table risk data available."))

    paragraphs.append(("normal", ""))
    paragraphs.append(("heading", "Automation Concentration"))
    if top_dependencies:
        paragraphs.extend(
            ("normal", line)
            for line in bullet_lines(top_dependencies, lambda item: f"{item[0]} drives {item[1]} downstream dependencies")
        )
    else:
        paragraphs.append(("normal", "- No dependency concentration detected."))

    paragraphs.append(("normal", ""))
    paragraphs.append(("heading", "Integration Exposure"))
    if top_hosts:
        paragraphs.extend(
            ("normal", line)
            for line in bullet_lines(top_hosts, lambda item: f"{item[0]} appears in {item[1]} integration artifacts")
        )
    else:
        paragraphs.append(("normal", "- No external hosts parsed from endpoint metadata."))

    paragraphs.append(("normal", ""))
    paragraphs.append(("heading", "Security Operation Mix"))
    if top_acl_ops:
        paragraphs.extend(
            ("normal", line)
            for line in bullet_lines(top_acl_ops, lambda item: f"{item[0]} operation appears in {item[1]} ACL records")
        )
    else:
        paragraphs.append(("normal", "- No ACL operation data available."))

    paragraphs.append(("normal", ""))
    paragraphs.append(("heading", "Access Limitations"))
    if access_limits:
        paragraphs.extend(("normal", f"- {safe_text(limit)}") for limit in access_limits)
    else:
        paragraphs.append(("normal", "- No access limitations were observed during this run."))

    paragraphs.extend(
        [
            ("normal", ""),
            ("heading", "Recommended Executive Actions"),
            ("normal", "- Assign named owners for the highest-risk tables and set a quarterly control-review cadence."),
            ("normal", "- Prioritize engineering review of high fan-out automation sources to reduce change blast radius."),
            ("normal", "- Review scripted ACLs and ensure each one has a clear business owner and test coverage."),
            ("normal", ""),
            ("heading", "Supporting Artifacts"),
            ("normal", "- generated/README.md"),
            ("normal", "- generated/INVENTORY.md"),
            ("normal", "- generated/DATA_MODEL/TABLE_CATALOG.md"),
            ("normal", "- generated/PROCESSES/PROCESS_INDEX.md"),
            ("normal", "- generated/PROCESSES/PROCESS_CHAINS.md"),
            ("normal", "- generated/INTEGRATIONS/INTEGRATION_CATALOG.md"),
            ("normal", "- generated/SECURITY/ACL_MATRIX.md"),
        ]
    )
    return paragraphs


def write_ceo_brief_failure(path, error):
    generated_at = datetime.now(timezone.utc)
    paragraphs = [
        ("title", "ServiceNow CEO Briefing"),
        ("normal", f"Generated: {generated_at.strftime('%Y-%m-%d %H:%M:%S UTC')}"),
        ("normal", ""),
        ("heading", "Generation Status"),
        (
            "normal",
            "Automated discovery did not complete because of connectivity, authentication, or permission limits.",
        ),
        ("normal", f"- Reported issue: {safe_text(error)}"),
        ("normal", ""),
        ("heading", "What This Means"),
        ("normal", "- The detailed inventory and risk signals in this run are incomplete."),
        ("normal", "- Access credentials and API reachability should be validated before relying on this report."),
        ("normal", ""),
        ("heading", "Next Step"),
        ("normal", "- Re-run generation after resolving the issue listed above."),
    ]
    write_docx(path, paragraphs)

BASE_URL = env_first("SN_BASE_URL", "SERVICENOW_INSTANCE_URL", default="https://xeretecdev.service-now.com")
TOKEN_URL = env_first("SN_TOKEN_URL", "SERVICENOW_TOKEN_URL", default=f"{BASE_URL}/oauth_token.do")
CLIENT_ID = env_first("SN_CLIENT_ID", "SERVICENOW_CLIENT_ID", default="")
CLIENT_SECRET = env_first("SN_CLIENT_SECRET", "SERVICENOW_CLIENT_SECRET", default="")

MAX_RPM = env_int("SN_MAX_RPM", default=120)
PAGE_SIZE = env_int("SN_PAGE_SIZE", default=500)
MAX_TABLES = env_int("SN_MAX_TABLES", default=0)
MAX_RECORDS_PER_TABLE = env_int("SN_MAX_RECORDS_PER_TABLE", default=0)
GRAPH_EDGE_LIMIT = env_int("SN_GRAPH_EDGE_LIMIT", default=0)

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
            with urllib.request.urlopen(req, data=data, timeout=60) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw), None
        except urllib.error.HTTPError as e:
            detail = e.read().decode("utf-8", errors="ignore")
            msg = f"HTTP {e.code}: {detail[:300].strip()}" if detail else f"HTTP {e.code}: {e.reason}"
            if i == retries - 1:
                return None, msg
        except Exception as e:
            if i == retries - 1:
                return None, str(e)
        time.sleep([1, 2, 4, 8][min(i, 3)])
    return None, "max retries"


def get_token():
    if not CLIENT_ID or not CLIENT_SECRET:
        return None, "Missing OAuth credentials (SN_CLIENT_ID/SN_CLIENT_SECRET or SERVICENOW_CLIENT_ID/SERVICENOW_CLIENT_SECRET)"
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
    token = (data or {}).get("access_token")
    if not token:
        return None, f"Token response missing access_token: {data}"
    return token, None

def api_get_table(token, table, fields=None, query=None, limit=PAGE_SIZE, cap=None):
    results = []
    offset = 0
    hard_cap = normalize_cap(MAX_RECORDS_PER_TABLE if cap is None else cap)

    while True:
        if hard_cap is not None and offset >= hard_cap:
            break

        page_limit = max(1, limit)
        if hard_cap is not None:
            page_limit = min(page_limit, hard_cap - offset)
            if page_limit <= 0:
                break

        params = {
            "sysparm_limit": page_limit,
            "sysparm_offset": offset,
            "sysparm_display_value": "false",
            "sysparm_exclude_reference_link": "true",
        }
        if fields:
            params["sysparm_fields"] = ",".join(fields)
        if query:
            params["sysparm_query"] = query

        url = f"{BASE_URL}/api/now/table/{table}?{urllib.parse.urlencode(params)}"
        data, err = http_json(
            "GET",
            url,
            headers={"Accept": "application/json", "Authorization": f"Bearer {token}"},
        )
        if err:
            return results, err

        batch = (data or {}).get("result", [])
        if not isinstance(batch, list):
            return results, f"Unexpected response shape for {table}: {type(batch)}"

        results.extend(batch)
        fetched = len(batch)
        offset += fetched
        if fetched < page_limit:
            break

    return results, None


def fetch_optional_table(token, table, fields, query=None, cap=None, fallback_fields=None):
    rows, err = api_get_table(token, table, fields=fields, query=query, cap=cap)
    if err and fallback_fields:
        rows, err = api_get_table(token, table, fields=fallback_fields, query=query, cap=cap)
    if err:
        ACCESS_LIMITS.append(f"{table}: {err}")
        return []
    return rows


def extract_edges(kind, name, sys_id, script):
    if not script:
        return []

    source_name = safe_text(name) or "unnamed"
    source_id = safe_text(sys_id) or "no_sys_id"
    src = f"{kind}:{source_name}({source_id})"

    patterns = [
        (r"(?:new\s+)?GlideRecord(?:Secure)?\(['\"]([a-zA-Z0-9_]+)['\"]\)", "table"),
        (r"gs\.eventQueue(?:Scheduled)?\(['\"]([a-zA-Z0-9_.]+)['\"]", "event"),
        (r"sn_ws\.RESTMessageV2\(['\"]([a-zA-Z0-9_ .:-]+)['\"]", "rest_message"),
        (r"(?:new\s+)?GlideAjax\(['\"]([a-zA-Z0-9_]+)['\"]\)", "script_include"),
        (r"FlowAPI\.(?:startFlow|executeFlow|startSubflow|executeSubflow)\(['\"]([a-zA-Z0-9_.:-]+)['\"]", "flow"),
    ]

    edges = []
    for pattern, target_type in patterns:
        for match in re.finditer(pattern, script):
            edges.append(
                {
                    "source": src,
                    "target": f"{target_type}:{match.group(1)}",
                    "evidence": match.group(0),
                    "artifact_sys_id": source_id,
                }
            )
    return edges


def dedupe_edges(edges):
    seen = set()
    deduped = []
    for edge in edges:
        key = (edge["source"], edge["target"], edge["evidence"], edge["artifact_sys_id"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(edge)
    return deduped


def build_mermaid_graph(edge_rows, limit=None):
    effective_limit = normalize_cap(limit)
    selected = edge_rows if effective_limit is None else edge_rows[:effective_limit]
    lines = ["graph LR"]
    node_ids = {}

    def node_id(label):
        if label not in node_ids:
            node_ids[label] = f"N{len(node_ids) + 1}"
            lines.append(f'  {node_ids[label]}["{escape_mermaid(label)}"]')
        return node_ids[label]

    for source, label, target in selected:
        src = node_id(source)
        dst = node_id(target)
        edge_label = safe_text(label)
        if edge_label:
            lines.append(f"  {src} -->|{escape_mermaid(edge_label)}| {dst}")
        else:
            lines.append(f"  {src} --> {dst}")

    return "\n".join(lines) + "\n"


def acl_table_name(acl_name):
    raw = safe_text(acl_name)
    if not raw:
        return ""
    return raw.split(".", 1)[0]


def write_minimal_outputs(error):
    for directory in [OUT, OUT / "DATA_MODEL", OUT / "PROCESSES", OUT / "INTEGRATIONS", OUT / "SECURITY", OUT / "REPORTS"]:
        directory.mkdir(parents=True, exist_ok=True)

    files = {
        "README.md": "# ServiceNow Enterprise Autodocumentation\n\nGeneration could not complete due to connectivity or authentication limitations.\n",
        "INVENTORY.md": "# Enterprise Inventory\n\nNo inventory data collected.\n",
        "ACCESS_LIMITATIONS.md": f"# Access Limitations\n\n- {error}\n",
        "DATA_MODEL/TABLE_CATALOG.md": "# Data Model Catalog\n\nNo table metadata collected.\n",
        "DATA_MODEL/REFERENCE_GRAPH.mmd": "graph LR\n",
        "PROCESSES/PROCESS_INDEX.md": "# Process Index\n\nNo process artifacts collected.\n",
        "PROCESSES/PROCESS_CHAINS.md": "# Process Chains\n\nNo dependency chains collected.\n",
        "PROCESSES/DEPENDENCY_GRAPH.mmd": "graph LR\n",
        "INTEGRATIONS/INTEGRATION_CATALOG.md": "# Integration Catalog\n\nNo integration artifacts collected.\n",
        "SECURITY/ACL_MATRIX.md": "# ACL Matrix\n\nNo ACL artifacts collected.\n",
        "REPORTS/artifact_index.json": json.dumps(
            {"error": error, "documents": {"ceo_brief": "CEO_BRIEF.docx", "readme": "README.md"}},
            indent=2,
        ),
        "REPORTS/dependency_edges.json": "[]\n",
        "REPORTS/table_dictionary_summary.json": "{}\n",
        "REPORTS/process_artifacts.json": "[]\n",
        "REPORTS/integration_artifacts.json": "[]\n",
        "REPORTS/acl_records.json": "[]\n",
        "REPORTS/table_inventory.json": "[]\n",
    }
    for rel_path, content in files.items():
        write_text(OUT / rel_path, content)

    write_ceo_brief_failure(OUT / "CEO_BRIEF.docx", error)


def main():
    started_at = datetime.now(timezone.utc)
    token, err = get_token()
    if err:
        write_minimal_outputs(f"OAuth/token failure: {err}")
        print("Generated minimal outputs with access limitations.")
        return

    print("Collecting table inventory...")
    inventory, err = api_get_table(
        token,
        "sys_db_object",
        ["sys_id", "name", "label", "sys_scope"],
        cap=MAX_TABLES,
    )
    if err:
        write_minimal_outputs(f"sys_db_object read failed: {err}")
        print("Generated minimal outputs with access limitations.")
        return
    if not inventory:
        write_minimal_outputs("sys_db_object returned no rows for this credential set.")
        print("Generated minimal outputs with access limitations.")
        return

    print("Collecting dictionary, process, integration, and security metadata...")
    dict_rows = fetch_optional_table(
        token,
        "sys_dictionary",
        ["sys_id", "name", "element", "internal_type", "reference", "mandatory"],
        fallback_fields=["sys_id", "name", "element", "reference"],
    )
    br_rows = fetch_optional_table(
        token,
        "sys_script",
        ["sys_id", "name", "collection", "when", "active", "sys_scope", "script"],
        fallback_fields=["sys_id", "name", "collection", "script"],
    )
    script_include_rows = fetch_optional_table(
        token,
        "sys_script_include",
        ["sys_id", "name", "api_name", "active", "sys_scope", "access", "script"],
        fallback_fields=["sys_id", "name", "active", "script"],
    )
    client_script_rows = fetch_optional_table(
        token,
        "sys_script_client",
        ["sys_id", "name", "table", "type", "active", "sys_scope", "script"],
        fallback_fields=["sys_id", "name", "table", "script"],
    )
    ui_action_rows = fetch_optional_table(
        token,
        "sys_ui_action",
        ["sys_id", "name", "table", "action_name", "active", "sys_scope", "script"],
        fallback_fields=["sys_id", "name", "table", "script"],
    )
    scheduled_job_rows = fetch_optional_table(
        token,
        "sysauto_script",
        ["sys_id", "name", "run_type", "active", "sys_scope", "script"],
        fallback_fields=["sys_id", "name", "script"],
    )
    flow_rows = fetch_optional_table(
        token,
        "sys_hub_flow",
        ["sys_id", "name", "active", "sys_scope", "description"],
        fallback_fields=["sys_id", "name", "active"],
    )
    rest_message_rows = fetch_optional_table(
        token,
        "sys_rest_message",
        ["sys_id", "name", "rest_endpoint", "authentication_type", "active", "sys_scope"],
        fallback_fields=["sys_id", "name", "rest_endpoint", "active"],
    )
    rest_method_rows = fetch_optional_table(
        token,
        "sys_rest_message_fn",
        ["sys_id", "name", "http_method", "rest_endpoint", "rest_message", "active", "sys_scope"],
        fallback_fields=["sys_id", "name", "http_method", "rest_endpoint", "active"],
    )
    soap_message_rows = fetch_optional_table(
        token,
        "sys_soap_message",
        ["sys_id", "name", "endpoint", "active", "sys_scope"],
        fallback_fields=["sys_id", "name", "endpoint", "active"],
    )
    event_registry_rows = fetch_optional_table(
        token,
        "sysevent_register",
        ["sys_id", "name", "table", "fired_by"],
        fallback_fields=["sys_id", "name", "table"],
    )
    acl_rows = fetch_optional_table(
        token,
        "sys_security_acl",
        ["sys_id", "name", "operation", "type", "active", "requires_role", "condition", "script", "sys_scope"],
        fallback_fields=["sys_id", "name", "operation", "type", "active", "script"],
    )

    for directory in [OUT, OUT / "DATA_MODEL", OUT / "PROCESSES", OUT / "INTEGRATIONS", OUT / "SECURITY", OUT / "REPORTS"]:
        directory.mkdir(parents=True, exist_ok=True)

    inv_map = {row.get("name"): row for row in inventory if row.get("name")}
    table_names = sorted(inv_map.keys())

    summary = defaultdict(
        lambda: {
            "sys_id": "",
            "label": "",
            "scope": "",
            "field_count": 0,
            "reference_field_count": 0,
            "mandatory_field_count": 0,
            "business_rule_count": 0,
            "acl_count": 0,
            "risk_score": 0,
        }
    )

    for table_name in table_names:
        inv = inv_map.get(table_name, {})
        summary[table_name]["sys_id"] = safe_text(inv.get("sys_id"))
        summary[table_name]["label"] = safe_text(inv.get("label"))
        summary[table_name]["scope"] = safe_text(inv.get("sys_scope")) or "global"

    refs = []
    for row in dict_rows:
        table_name = safe_text(row.get("name"))
        if not table_name:
            continue
        summary[table_name]["field_count"] += 1
        if as_bool(row.get("mandatory")):
            summary[table_name]["mandatory_field_count"] += 1
        reference = safe_text(row.get("reference"))
        if reference:
            summary[table_name]["reference_field_count"] += 1
            refs.append(
                {
                    "source": f"table:{table_name}",
                    "field": safe_text(row.get("element")),
                    "target": f"table:{reference}",
                    "dictionary_sys_id": safe_text(row.get("sys_id")),
                }
            )

    process_artifacts = []
    edges = []
    br_by_table = Counter()

    for br in br_rows:
        table_name = safe_text(br.get("collection"))
        if table_name:
            br_by_table[table_name] += 1
        process_artifacts.append(
            {
                "type": "business_rule",
                "name": safe_text(br.get("name")),
                "sys_id": safe_text(br.get("sys_id")),
                "table": table_name,
                "trigger": safe_text(br.get("when")),
                "active": as_bool(br.get("active")),
                "scope": safe_text(br.get("sys_scope")),
            }
        )
        edges.extend(extract_edges("business_rule", br.get("name"), br.get("sys_id"), safe_text(br.get("script"))))

    for script_include in script_include_rows:
        process_artifacts.append(
            {
                "type": "script_include",
                "name": safe_text(script_include.get("name")),
                "sys_id": safe_text(script_include.get("sys_id")),
                "table": "",
                "trigger": safe_text(script_include.get("access")),
                "active": as_bool(script_include.get("active")),
                "scope": safe_text(script_include.get("sys_scope")),
            }
        )
        edges.extend(
            extract_edges(
                "script_include",
                script_include.get("name"),
                script_include.get("sys_id"),
                safe_text(script_include.get("script")),
            )
        )

    for client_script in client_script_rows:
        process_artifacts.append(
            {
                "type": "client_script",
                "name": safe_text(client_script.get("name")),
                "sys_id": safe_text(client_script.get("sys_id")),
                "table": safe_text(client_script.get("table")),
                "trigger": safe_text(client_script.get("type")),
                "active": as_bool(client_script.get("active")),
                "scope": safe_text(client_script.get("sys_scope")),
            }
        )
        edges.extend(
            extract_edges(
                "client_script",
                client_script.get("name"),
                client_script.get("sys_id"),
                safe_text(client_script.get("script")),
            )
        )

    for ui_action in ui_action_rows:
        process_artifacts.append(
            {
                "type": "ui_action",
                "name": safe_text(ui_action.get("name")),
                "sys_id": safe_text(ui_action.get("sys_id")),
                "table": safe_text(ui_action.get("table")),
                "trigger": safe_text(ui_action.get("action_name")),
                "active": as_bool(ui_action.get("active")),
                "scope": safe_text(ui_action.get("sys_scope")),
            }
        )
        edges.extend(extract_edges("ui_action", ui_action.get("name"), ui_action.get("sys_id"), safe_text(ui_action.get("script"))))

    for scheduled_job in scheduled_job_rows:
        process_artifacts.append(
            {
                "type": "scheduled_script",
                "name": safe_text(scheduled_job.get("name")),
                "sys_id": safe_text(scheduled_job.get("sys_id")),
                "table": "",
                "trigger": safe_text(scheduled_job.get("run_type")),
                "active": as_bool(scheduled_job.get("active")),
                "scope": safe_text(scheduled_job.get("sys_scope")),
            }
        )
        edges.extend(
            extract_edges(
                "scheduled_script",
                scheduled_job.get("name"),
                scheduled_job.get("sys_id"),
                safe_text(scheduled_job.get("script")),
            )
        )

    for flow in flow_rows:
        process_artifacts.append(
            {
                "type": "flow",
                "name": safe_text(flow.get("name")),
                "sys_id": safe_text(flow.get("sys_id")),
                "table": "",
                "trigger": "flow_designer",
                "active": as_bool(flow.get("active")),
                "scope": safe_text(flow.get("sys_scope")),
            }
        )

    edges = dedupe_edges(edges)
    out_degree = Counter(edge["source"] for edge in edges)
    in_degree = Counter(edge["target"] for edge in edges)

    acl_table_counter = Counter()
    acl_operation_counter = Counter()
    scripted_acl_count = 0
    role_acl_count = 0
    for acl in acl_rows:
        table_name = acl_table_name(acl.get("name"))
        if table_name:
            acl_table_counter[table_name] += 1
        operation = safe_text(acl.get("operation")) or "unknown"
        acl_operation_counter[operation] += 1
        if safe_text(acl.get("script")):
            scripted_acl_count += 1
        if safe_text(acl.get("requires_role")):
            role_acl_count += 1

    for table_name in table_names:
        summary[table_name]["business_rule_count"] = br_by_table.get(table_name, 0)
        summary[table_name]["acl_count"] = acl_table_counter.get(table_name, 0)
        field_count = summary[table_name]["field_count"]
        ref_count = summary[table_name]["reference_field_count"]
        mandatory_count = summary[table_name]["mandatory_field_count"]
        br_count = summary[table_name]["business_rule_count"]
        acl_count = summary[table_name]["acl_count"]
        summary[table_name]["risk_score"] = field_count + (ref_count * 3) + (mandatory_count * 2) + (br_count * 5) + (acl_count * 4)

    tables_by_risk = sorted(summary.items(), key=lambda item: item[1]["risk_score"], reverse=True)
    scope_counter = Counter((safe_text(row.get("sys_scope")) or "global") for row in inventory)

    integration_artifacts = []
    integration_hosts = Counter()
    for row in rest_message_rows:
        endpoint = safe_text(row.get("rest_endpoint"))
        if endpoint:
            host = urllib.parse.urlparse(endpoint).hostname
            if host:
                integration_hosts[host] += 1
        integration_artifacts.append(
            {
                "type": "rest_message",
                "name": safe_text(row.get("name")),
                "sys_id": safe_text(row.get("sys_id")),
                "endpoint": endpoint,
                "method": "",
                "active": as_bool(row.get("active")),
                "scope": safe_text(row.get("sys_scope")),
            }
        )
    for row in rest_method_rows:
        endpoint = safe_text(row.get("rest_endpoint"))
        if endpoint:
            host = urllib.parse.urlparse(endpoint).hostname
            if host:
                integration_hosts[host] += 1
        integration_artifacts.append(
            {
                "type": "rest_method",
                "name": safe_text(row.get("name")),
                "sys_id": safe_text(row.get("sys_id")),
                "endpoint": endpoint,
                "method": safe_text(row.get("http_method")),
                "active": as_bool(row.get("active")),
                "scope": safe_text(row.get("sys_scope")),
            }
        )
    for row in soap_message_rows:
        endpoint = safe_text(row.get("endpoint"))
        if endpoint:
            host = urllib.parse.urlparse(endpoint).hostname
            if host:
                integration_hosts[host] += 1
        integration_artifacts.append(
            {
                "type": "soap_message",
                "name": safe_text(row.get("name")),
                "sys_id": safe_text(row.get("sys_id")),
                "endpoint": endpoint,
                "method": "SOAP",
                "active": as_bool(row.get("active")),
                "scope": safe_text(row.get("sys_scope")),
            }
        )

    event_usage = Counter()
    for edge in edges:
        target = safe_text(edge.get("target"))
        if target.startswith("event:"):
            event_usage[target.split(":", 1)[1]] += 1

    generated_at = datetime.now(timezone.utc)
    elapsed_seconds = int((generated_at - started_at).total_seconds())
    top_complex_tables = [name for name, _ in tables_by_risk[:10]]
    top_dependency_sources = [source for source, _ in out_degree.most_common(10)]
    top_acl_ops = [f"{op} ({count})" for op, count in acl_operation_counter.most_common(5)]

    readme_lines = [
        "# ServiceNow Enterprise Autodocumentation",
        "",
        f"_Generated: {generated_at.strftime('%Y-%m-%d %H:%M:%S UTC')}_",
        "",
        "## Executive Summary",
        f"- Platform footprint documented: **{len(table_names)} tables** and **{len(dict_rows)} dictionary fields**.",
        f"- Process automation documented: **{len(process_artifacts)} artifacts** across business rules, scripts, UI actions, scheduled jobs, and flows.",
        f"- Integration surface documented: **{len(integration_artifacts)} external integration artifacts** plus **{len(event_registry_rows)} registered events**.",
        f"- Security posture documented: **{len(acl_rows)} ACL records**, including **{scripted_acl_count} scripted ACLs** and **{role_acl_count} ACLs with explicit roles**.",
        f"- Code-level dependencies extracted: **{len(edges)} unique edges**.",
        "",
        "## Key Management Signals",
        f"- Highest structural complexity tables: {', '.join(top_complex_tables) if top_complex_tables else 'None available'}",
        f"- Highest automation fan-out sources: {', '.join(top_dependency_sources) if top_dependency_sources else 'None available'}",
        f"- Most frequent ACL operations: {', '.join(top_acl_ops) if top_acl_ops else 'None available'}",
        "",
        "## Document Index",
        "- `CEO_BRIEF.docx`: board-ready summary for executive review.",
        "- `INVENTORY.md`: enterprise table register with scope and risk ranking.",
        "- `DATA_MODEL/TABLE_CATALOG.md`: full schema-level metrics and field composition.",
        "- `DATA_MODEL/REFERENCE_GRAPH.mmd`: table reference topology (Mermaid graph).",
        "- `PROCESSES/PROCESS_INDEX.md`: automation catalog and execution footprint.",
        "- `PROCESSES/PROCESS_CHAINS.md`: dependency hotspots and complete edge appendix.",
        "- `PROCESSES/DEPENDENCY_GRAPH.mmd`: automation dependency graph (Mermaid).",
        "- `INTEGRATIONS/INTEGRATION_CATALOG.md`: complete integration inventory and external endpoint profile.",
        "- `SECURITY/ACL_MATRIX.md`: ACL operation matrix and full control register.",
        "- `REPORTS/*.json`: full machine-readable exports for audit, BI, or downstream analysis.",
        "",
        "## Runtime Parameters",
        f"- Base URL: `{BASE_URL}`",
        f"- Page size: `{PAGE_SIZE}` rows/request",
        f"- Table inventory cap: `{MAX_TABLES if MAX_TABLES > 0 else 'unbounded'}`",
        f"- Per-table row cap: `{MAX_RECORDS_PER_TABLE if MAX_RECORDS_PER_TABLE > 0 else 'unbounded'}`",
        f"- Generation time: `{elapsed_seconds}` seconds",
        "",
        "## Access Limitations",
    ]
    if ACCESS_LIMITS:
        readme_lines.extend(f"- {item}" for item in ACCESS_LIMITS)
    else:
        readme_lines.append("- None observed for accessed tables.")
    write_text(OUT / "README.md", "\n".join(readme_lines) + "\n")

    write_docx(
        OUT / "CEO_BRIEF.docx",
        build_ceo_brief_paragraphs(
            generated_at=generated_at,
            elapsed_seconds=elapsed_seconds,
            base_url=BASE_URL,
            table_names=table_names,
            dict_rows=dict_rows,
            process_artifacts=process_artifacts,
            integration_artifacts=integration_artifacts,
            event_registry_rows=event_registry_rows,
            acl_rows=acl_rows,
            scripted_acl_count=scripted_acl_count,
            role_acl_count=role_acl_count,
            edges=edges,
            tables_by_risk=tables_by_risk,
            out_degree=out_degree,
            integration_hosts=integration_hosts,
            acl_operation_counter=acl_operation_counter,
            access_limits=ACCESS_LIMITS,
        ),
    )

    scope_rows = [[scope, count] for scope, count in sorted(scope_counter.items(), key=lambda item: (-item[1], item[0]))]
    inventory_rows = []
    for table_name, stats in tables_by_risk:
        inventory_rows.append(
            [
                table_name,
                stats["label"],
                stats["scope"],
                stats["field_count"],
                stats["reference_field_count"],
                stats["mandatory_field_count"],
                stats["business_rule_count"],
                stats["acl_count"],
                stats["risk_score"],
                stats["sys_id"],
            ]
        )

    inventory_doc = [
        "# Enterprise Inventory",
        "",
        "## CEO Narrative",
        "The inventory below prioritizes platform assets by combined schema complexity, automation concentration, and security control density.",
        "",
        "## Scope Distribution",
        markdown_table(["Scope", "Table Count"], scope_rows) if scope_rows else "_No scope data available._",
        "",
        "## Full Table Register",
        markdown_table(
            [
                "Table",
                "Label",
                "Scope",
                "Fields",
                "Reference Fields",
                "Mandatory Fields",
                "Business Rules",
                "ACLs",
                "Risk Score",
                "Sys ID",
            ],
            inventory_rows,
        )
        if inventory_rows
        else "_No table data available._",
        "",
    ]
    write_text(OUT / "INVENTORY.md", "\n".join(inventory_doc))

    access_doc = ["# Access Limitations", ""]
    if ACCESS_LIMITS:
        access_doc.extend(f"- {item}" for item in ACCESS_LIMITS)
    else:
        access_doc.append("- None observed for accessed tables.")
    access_doc.append("")
    write_text(OUT / "ACCESS_LIMITATIONS.md", "\n".join(access_doc))

    table_catalog_rows = []
    for table_name, stats in tables_by_risk:
        field_count = stats["field_count"]
        ref_count = stats["reference_field_count"]
        mandatory_count = stats["mandatory_field_count"]
        ref_ratio = f"{(100.0 * ref_count / field_count):.1f}%" if field_count else "0.0%"
        mandatory_ratio = f"{(100.0 * mandatory_count / field_count):.1f}%" if field_count else "0.0%"
        table_catalog_rows.append(
            [
                table_name,
                stats["label"],
                field_count,
                ref_count,
                ref_ratio,
                mandatory_count,
                mandatory_ratio,
                stats["business_rule_count"],
                stats["acl_count"],
                stats["risk_score"],
            ]
        )

    data_model_doc = [
        "# Data Model Catalog",
        "",
        "## Executive Narrative",
        "This section captures schema composition, coupling intensity, and control surface per table.",
        "",
        "## Full Data Model Register",
        markdown_table(
            [
                "Table",
                "Label",
                "Fields",
                "Reference Fields",
                "Reference Ratio",
                "Mandatory Fields",
                "Mandatory Ratio",
                "Business Rules",
                "ACLs",
                "Risk Score",
            ],
            table_catalog_rows,
        )
        if table_catalog_rows
        else "_No schema data available._",
        "",
    ]
    write_text(OUT / "DATA_MODEL" / "TABLE_CATALOG.md", "\n".join(data_model_doc))

    reference_graph_edges = [(edge["source"], edge["field"], edge["target"]) for edge in refs]
    write_text(
        OUT / "DATA_MODEL" / "REFERENCE_GRAPH.mmd",
        build_mermaid_graph(reference_graph_edges, limit=GRAPH_EDGE_LIMIT),
    )

    process_type_counter = Counter(artifact["type"] for artifact in process_artifacts)
    process_type_rows = [[process_type, count] for process_type, count in sorted(process_type_counter.items(), key=lambda item: (-item[1], item[0]))]
    top_table_automation_rows = [[table, count] for table, count in br_by_table.most_common(50)]
    process_rows = [
        [
            artifact["type"],
            artifact["name"],
            artifact["table"],
            artifact["trigger"],
            "true" if artifact["active"] else "false",
            artifact["scope"],
            artifact["sys_id"],
        ]
        for artifact in sorted(process_artifacts, key=lambda item: (item["type"], item["name"], item["sys_id"]))
    ]

    process_index_doc = [
        "# Process Index",
        "",
        "## Executive Narrative",
        "The automation catalog below captures server-side, client-side, and scheduled logic assets that drive operational outcomes.",
        "",
        "## Automation Type Distribution",
        markdown_table(["Artifact Type", "Count"], process_type_rows) if process_type_rows else "_No process data available._",
        "",
        "## Top Tables by Business Rule Count",
        markdown_table(["Table", "Business Rule Count"], top_table_automation_rows) if top_table_automation_rows else "_No business-rule table mappings available._",
        "",
        "## Full Process Register",
        markdown_table(["Type", "Name", "Table", "Trigger", "Active", "Scope", "Sys ID"], process_rows) if process_rows else "_No process artifacts available._",
        "",
    ]
    write_text(OUT / "PROCESSES" / "PROCESS_INDEX.md", "\n".join(process_index_doc))

    out_degree_rows = [[source, count] for source, count in out_degree.most_common(50)]
    in_degree_rows = [[target, count] for target, count in in_degree.most_common(50)]
    dependency_rows = [[edge["source"], edge["target"], edge["evidence"], edge["artifact_sys_id"]] for edge in edges]

    process_chains_doc = [
        "# Process Chains",
        "",
        "## Executive Narrative",
        "Dependency concentration highlights where change carries outsized blast radius risk.",
        "",
        "## Highest Outbound Dependency Sources",
        markdown_table(["Source", "Downstream Edge Count"], out_degree_rows) if out_degree_rows else "_No dependency sources identified._",
        "",
        "## Highest Inbound Dependency Targets",
        markdown_table(["Target", "Inbound Edge Count"], in_degree_rows) if in_degree_rows else "_No dependency targets identified._",
        "",
        "## Full Dependency Register",
        markdown_table(["Source", "Target", "Evidence", "Artifact Sys ID"], dependency_rows) if dependency_rows else "_No dependencies extracted._",
        "",
    ]
    write_text(OUT / "PROCESSES" / "PROCESS_CHAINS.md", "\n".join(process_chains_doc))

    dependency_graph_edges = [
        (
            edge["source"],
            safe_text(edge["evidence"])[:48],
            edge["target"],
        )
        for edge in edges
    ]
    write_text(
        OUT / "PROCESSES" / "DEPENDENCY_GRAPH.mmd",
        build_mermaid_graph(dependency_graph_edges, limit=GRAPH_EDGE_LIMIT),
    )

    host_rows = [[host, count] for host, count in integration_hosts.most_common(50)]
    event_registry_rows_md = [
        [
            safe_text(row.get("name")),
            safe_text(row.get("table")),
            safe_text(row.get("fired_by")),
            safe_text(row.get("sys_id")),
        ]
        for row in sorted(event_registry_rows, key=lambda item: (safe_text(item.get("name")), safe_text(item.get("sys_id"))))
    ]
    event_usage_rows = [[event, count] for event, count in event_usage.most_common(100)]
    integration_rows = [
        [
            item["type"],
            item["name"],
            item["method"],
            item["endpoint"],
            "true" if item["active"] else "false",
            item["scope"],
            item["sys_id"],
        ]
        for item in sorted(integration_artifacts, key=lambda record: (record["type"], record["name"], record["sys_id"]))
    ]

    integration_doc = [
        "# Integration Catalog",
        "",
        "## Executive Narrative",
        "This register identifies external integration touchpoints and event-driven interfaces that expose the platform boundary.",
        "",
        "## Integration Summary",
        f"- REST messages: **{len(rest_message_rows)}**",
        f"- REST methods: **{len(rest_method_rows)}**",
        f"- SOAP messages: **{len(soap_message_rows)}**",
        f"- Registered events: **{len(event_registry_rows)}**",
        f"- Event usages detected in scripts: **{sum(event_usage.values())}**",
        "",
        "## External Host Concentration",
        markdown_table(["Host", "Artifacts"], host_rows) if host_rows else "_No external hosts were parsed from endpoint URLs._",
        "",
        "## Full Integration Register",
        markdown_table(["Type", "Name", "Method", "Endpoint", "Active", "Scope", "Sys ID"], integration_rows) if integration_rows else "_No integration artifacts available._",
        "",
        "## Registered Events",
        markdown_table(["Event", "Table", "Fired By", "Sys ID"], event_registry_rows_md) if event_registry_rows_md else "_No registered events available._",
        "",
        "## Events Used by Automation",
        markdown_table(["Event", "Usage Count"], event_usage_rows) if event_usage_rows else "_No event usage detected in analyzed scripts._",
        "",
    ]
    write_text(OUT / "INTEGRATIONS" / "INTEGRATION_CATALOG.md", "\n".join(integration_doc))

    acl_operation_rows = [[operation, count] for operation, count in acl_operation_counter.most_common()]
    acl_table_rows = [[table, count] for table, count in acl_table_counter.most_common(100)]
    acl_rows_md = [
        [
            safe_text(acl.get("name")),
            safe_text(acl.get("operation")),
            safe_text(acl.get("type")),
            safe_text(acl.get("requires_role")),
            "true" if safe_text(acl.get("script")) else "false",
            "true" if as_bool(acl.get("active")) else "false",
            safe_text(acl.get("sys_scope")),
            safe_text(acl.get("sys_id")),
        ]
        for acl in sorted(acl_rows, key=lambda item: (safe_text(item.get("name")), safe_text(item.get("operation")), safe_text(item.get("sys_id"))))
    ]

    security_doc = [
        "# ACL Matrix",
        "",
        "## Executive Narrative",
        "The ACL matrix captures access control depth, scripted control concentration, and operation mix across the instance.",
        "",
        "## Security Summary",
        f"- Total ACL records: **{len(acl_rows)}**",
        f"- Scripted ACL records: **{scripted_acl_count}**",
        f"- ACLs with explicit roles: **{role_acl_count}**",
        "",
        "## ACLs by Operation",
        markdown_table(["Operation", "Count"], acl_operation_rows) if acl_operation_rows else "_No ACL operation data available._",
        "",
        "## Top Tables by ACL Volume",
        markdown_table(["Table", "ACL Count"], acl_table_rows) if acl_table_rows else "_No ACL table mappings available._",
        "",
        "## Full ACL Register",
        markdown_table(
            ["Name", "Operation", "Type", "Requires Role", "Scripted", "Active", "Scope", "Sys ID"],
            acl_rows_md,
        )
        if acl_rows_md
        else "_No ACL records available._",
        "",
    ]
    write_text(OUT / "SECURITY" / "ACL_MATRIX.md", "\n".join(security_doc))

    summary_out = {table: summary[table] for table in sorted(summary.keys())}
    table_inventory_json = [
        {
            "table": table,
            "label": stats["label"],
            "scope": stats["scope"],
            "field_count": stats["field_count"],
            "reference_field_count": stats["reference_field_count"],
            "mandatory_field_count": stats["mandatory_field_count"],
            "business_rule_count": stats["business_rule_count"],
            "acl_count": stats["acl_count"],
            "risk_score": stats["risk_score"],
            "sys_id": stats["sys_id"],
        }
        for table, stats in tables_by_risk
    ]

    artifact_index = {
        "generated_at": generated_at.isoformat(),
        "base_url": BASE_URL,
        "documents": {
            "ceo_brief": "CEO_BRIEF.docx",
            "readme": "README.md",
        },
        "counts": {
            "sys_db_object": len(inventory),
            "sys_dictionary": len(dict_rows),
            "sys_script": len(br_rows),
            "sys_script_include": len(script_include_rows),
            "sys_script_client": len(client_script_rows),
            "sys_ui_action": len(ui_action_rows),
            "sysauto_script": len(scheduled_job_rows),
            "sys_hub_flow": len(flow_rows),
            "sys_rest_message": len(rest_message_rows),
            "sys_rest_message_fn": len(rest_method_rows),
            "sys_soap_message": len(soap_message_rows),
            "sysevent_register": len(event_registry_rows),
            "sys_security_acl": len(acl_rows),
            "dependency_edges": len(edges),
        },
        "runtime_config": {
            "page_size": PAGE_SIZE,
            "max_tables": MAX_TABLES,
            "max_records_per_table": MAX_RECORDS_PER_TABLE,
            "max_rpm": MAX_RPM,
            "graph_edge_limit": GRAPH_EDGE_LIMIT,
        },
        "access_limitations": ACCESS_LIMITS,
    }

    write_json(OUT / "REPORTS" / "artifact_index.json", artifact_index)
    write_json(OUT / "REPORTS" / "dependency_edges.json", edges)
    write_json(OUT / "REPORTS" / "table_dictionary_summary.json", summary_out)
    write_json(OUT / "REPORTS" / "process_artifacts.json", process_artifacts)
    write_json(OUT / "REPORTS" / "integration_artifacts.json", integration_artifacts)
    write_json(OUT / "REPORTS" / "acl_records.json", acl_rows)
    write_json(OUT / "REPORTS" / "table_inventory.json", table_inventory_json)

    print("Generated comprehensive documentation in ./generated")


if __name__ == "__main__":
    main()
