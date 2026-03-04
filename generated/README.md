# ServiceNow Enterprise Autodocumentation

_Generated: 2026-03-04 11:53:31 UTC_

## Executive Summary
- Platform footprint documented: **499 tables** and **499 dictionary fields**.
- Process automation documented: **2783 artifacts** across business rules, scripts, UI actions, scheduled jobs, and flows.
- Integration surface documented: **47 external integration artifacts** plus **499 registered events**.
- Security posture documented: **498 ACL records**, including **48 scripted ACLs** and **0 ACLs with explicit roles**.
- Code-level dependencies extracted: **1168 unique edges**.

## Key Management Signals
- Highest structural complexity tables: kb_feedback, cmdb_ci_endpoint_biztalk, task_ordering_rule, ml_capability_definition_base, problem, u_fd_articles_staged, clone_data_exclude, sys_app_template_output_var, sys_user_group, cmdb_ci_app_server_ora_ias_m
- Highest automation fan-out sources: script_include:SMTemplates(0530d0f0d7311100158ba6859e610384), script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704), script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d), scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282), business_rule:Cascade delete records(05712f9277352110b15a31cd6b5a998a), scheduled_script:Migrate homepages(353a54c647a032107a684bdb736d437d), script_include:AgentScheduleAjax(0328a950c37312001c845cb981d3ae5c), ui_action:Unload Dashboard (for Dev)(10278db24f02311054a65e8330ce0bd5), script_include:ProminFindingsDefUtilSNC(001df27a43d40210a829bf5ff7b8f267), script_include:WorkflowApprovalUtils(0360b36d0a0a0b260a89dfec60c339c4)
- Most frequent ACL operations: read (130), write (113), delete (92), create (87), 0997ab83733303005978e4b9cdf6a7b9 (50)

## Document Index
- `CEO_BRIEF.docx`: board-ready summary for executive review.
- `INVENTORY.md`: enterprise table register with scope and risk ranking.
- `DATA_MODEL/TABLE_CATALOG.md`: full schema-level metrics and field composition.
- `DATA_MODEL/REFERENCE_GRAPH.mmd`: table reference topology (Mermaid graph).
- `PROCESSES/PROCESS_INDEX.md`: automation catalog and execution footprint.
- `PROCESSES/PROCESS_CHAINS.md`: dependency hotspots and complete edge appendix.
- `PROCESSES/DEPENDENCY_GRAPH.mmd`: automation dependency graph (Mermaid).
- `INTEGRATIONS/INTEGRATION_CATALOG.md`: complete integration inventory and external endpoint profile.
- `SECURITY/ACL_MATRIX.md`: ACL operation matrix and full control register.
- `REPORTS/*.json`: full machine-readable exports for audit, BI, or downstream analysis.

## Runtime Parameters
- Base URL: `https://xeretecdev.service-now.com`
- Page size: `500` rows/request
- Table inventory cap: `unbounded`
- Per-table row cap: `unbounded`
- Generation time: `8` seconds

## Access Limitations
- None observed for accessed tables.
