# Integration Catalog

## Executive Narrative
This register identifies external integration touchpoints and event-driven interfaces that expose the platform boundary.

## Integration Summary
- REST messages: **11**
- REST methods: **28**
- SOAP messages: **8**
- Registered events: **499**
- Event usages detected in scripts: **36**

## External Host Concentration
| Host | Artifacts |
| --- | --- |
| dev.azure.com | 7 |
| api.vantage.online | 6 |
| euprodms.prod.hpicatalyst.com | 5 |
| fcm.googleapis.com | 4 |
| xeretec.freshdesk.com | 2 |
| finance.yahoo.com | 2 |
| maps.googleapis.com | 2 |
| ${pushhost} | 2 |
| xeretecprod.my.salesforce.com | 2 |
| routes.googleapis.com | 1 |

## Full Integration Register
| Type | Name | Method | Endpoint | Active | Scope | Sys ID |
| --- | --- | --- | --- | --- | --- | --- |
| rest_message | DevOps Connector |  | https://dev.azure.com/xeretec/SoftwareDev/_apis/wit/workitems | false | global | bdf621a8dbd478d00ccf918cd39619d5 |
| rest_message | Firebase Cloud Messaging Send |  | https://fcm.googleapis.com/fcm/send | false | global | 84b45b63ff1331009738ffffffffffb9 |
| rest_message | Firebase Cloud Messaging V1 Send |  | https://fcm.googleapis.com/v1/projects/${project_id}/messages:send | false | global | 3a9d85e6c36021105e1a6333d840dd4c |
| rest_message | Google Map |  | https://maps.googleapis.com/maps/api/directions/json | false | global | d2304fac838fd210bbb45b6fc22bc0ae |
| rest_message | HP DaaS Proactive Management |  | https://euprodms.prod.hpicatalyst.com/services/ccc-ticketing/1.0/tickets | false | 1281fe89db169f00c3d6f9361d961925 | 38b45791dbde9f00c3d6f9361d961961 |
| rest_message | SalesForce Production |  | https://xeretecprod.my.salesforce.com/services/data | false | global | ee87e3ca1b3abc90afb921f0b24bcba0 |
| rest_message | ServiceNow NLU Service |  | ${server_url}/api/now/v1/nlu | false | global | 9d6049de7333230021a044764df6a772 |
| rest_message | ServiceNowMobileApp Push |  | https://${pushHost}/api/now/v1/push/${applicationName}/enqueue | false | global | ded0e522ff1231009738fffffffffffc |
| rest_message | Vantage Online Connector |  | https://api.vantage.online/application/loginsingle | false | global | b08a43321bb07410afb921f0b24bcbaf |
| rest_message | Xeretec FreshDesk Connector |  | https://xeretec.freshdesk.com/helpdesk/ | false | global | 395b5da11b4ef810afb921f0b24bcb37 |
| rest_message | Yahoo Finance |  | http://finance.yahoo.com/d/quotes.csv | false | global | bd478c46df020100cd7da5f59bf2636f |
| rest_method |  | get | ${server_url}/api/now/v1/nlu/getEntitesByModel/${modelId} | false | global | 026019d27373230021a044764df6a77b |
| rest_method |  | put | https://euprodms.prod.hpicatalyst.com/services/ccc-ticketing/1.0/tickets | false | 1281fe89db169f00c3d6f9361d961925 | 02b757d1dbde9f00c3d6f9361d961912 |
| rest_method |  | delete | https://euprodms.prod.hpicatalyst.com/services/ccc-ticketing/1.0/tickets/${sys_id} | false | 1281fe89db169f00c3d6f9361d961925 | 0434789c4ff213006ccbf3117310c74b |
| rest_method |  | post | https://api.vantage.online/application/loginsingle | false | global | 054ad37e1b38f4108e64eb92b24bcb3c |
| rest_method |  | get | https://maps.googleapis.com/maps/api/directions/json | false | global | 087083ec838fd210bbb45b6fc22bc00b |
| rest_method |  | get | https://euprodms.prod.hpicatalyst.com/services/ccc-ticketing/1.0/children | false | 1281fe89db169f00c3d6f9361d961925 | 1dbf54604f6313007bdda7d18110c786 |
| rest_method |  | post | https://routes.googleapis.com/distanceMatrix/v2:computeRouteMatrix?key=${apiKey} | false | global | 277007ec838fd210bbb45b6fc22bc011 |
| rest_method |  | get | ${server_url}/api/now/v1/nlu/getIntentsByModel/${modelId} | false | global | 459059d27373230021a044764df6a78f |
| rest_method |  | get | https://dev.azure.com/xeretec/SoftwareDev/_apis/wit/workitems/${type}?api-version=6.0 | false | global | 4c87a928dbd478d00ccf918cd3961908 |
| rest_method |  | get | http://finance.yahoo.com/d/quotes.csv | false | global | 4d678c46df020100cd7da5f59bf26399 |
| rest_method |  |  | https://fcm.googleapis.com/fcm/send | false | global | 4ef4df23ff1331009738ffffffffff2b |
| rest_method |  | get | ${server_url}/api/now/v1/nlu/getAllPublishedModels | false | global | 55bf05d27373230021a044764df6a732 |
| rest_method |  | patch | https://dev.azure.com/xeretec/SoftwareDev/_apis/wit/workitems/${id}?api-version=6.1-preview | false | global | 5c35ab721b98f8109e12997e0d4bcb72 |
| rest_method |  | get | https://xeretecprod.my.salesforce.com/services/data/v51.0/query?q=SELECT+${fieldString}+from+${table}+WHERE+${whereClause} | false | global | 61e76fca1b3abc90afb921f0b24bcbf1 |
| rest_method |  | patch | https://dev.azure.com/xeretec/SoftwareDev/_apis/wit/workitems/${id}?api-version=6.1-preview | false | global | 65bbbd5bdb20fc900ccf918cd39619c7 |
| rest_method |  | get | https://api.vantage.online/customer?&${sel}&$filter=reference%20eq%20'${ref}' | false | global | 6aca4f721bb07410afb921f0b24bcbb6 |
| rest_method |  | get | https://api.vantage.online/equipment?&$select=Id,SerialNumber,Location&$filter=SerialNumber%20eq%20'${ref}' | false | global | 86ef337a1bfcf4108e64eb92b24bcb4e |
| rest_method |  | post | https://dev.azure.com/xeretec/SoftwareDev/_apis/wit/workitems/$Task?api-version=6.1-preview | false | global | 881479acdb1878d00ccf918cd39619b6 |
| rest_method |  | patch | https://dev.azure.com/xeretec/SoftwareDev/_apis/wit/workitems/${id}?api-version=6.1-preview | false | global | 9d22d360db14b8d00ccf918cd39619dc |
| rest_method |  | post | https://euprodms.prod.hpicatalyst.com/services/ccc-ticketing/1.0/tickets | false | 1281fe89db169f00c3d6f9361d961925 | aa559f91dbde9f00c3d6f9361d961953 |
| rest_method |  | post | ${server_url}/api/now/v1/nlu/predictSync | false | global | b50a64977333230021a044764df6a77c |
| rest_method |  | get | ${server_url}/api/now/v1/nlu/getEntitesByIntent/${intentId} | false | global | b80095d27373230021a044764df6a74f |
| rest_method |  | get | https://xeretec.freshdesk.com/helpdesk/tickets.json | false | global | c9cb15251b4ef810afb921f0b24bcb53 |
| rest_method |  | post | https://fcm.googleapis.com/v1/projects/${project_id}/messages:send | false | global | d11ec5e6c36021105e1a6333d840ddd1 |
| rest_method |  | post | https://api.vantage.online/application/loginsingle | false | global | d71157be1bb07410afb921f0b24bcb97 |
| rest_method |  |  | https://${pushHost}/api/now/v1/push/${applicationName}/enqueue | false | global | e5112922ff1231009738ffffffffff40 |
| rest_method |  | post | https://api.vantage.online/application/loginsingle | false | global | ebcadfbe1b38f4108e64eb92b24bcb83 |
| rest_method |  | patch | https://dev.azure.com/xeretec/SoftwareDev/_apis/wit/workitems/${id}?api-version=6.1-preview | false | global | f1dcd3391b9834109e12997e0d4bcbed |
| soap_message | Amazon | SOAP |  | false | global | d4359a410a0a0bd1632aa26b41cc7457 |
| soap_message | Instance Clone Schedule | SOAP |  | false | global | 053f0b8e1b10200081599e3bcc071362 |
| soap_message | Provision ServiceNow Accounts | SOAP |  | false | global | 5a2d0757eb100200c8690e815206fe74 |
| soap_message | ServiceNow getRecords | SOAP |  | false | global | 86a3cc360a0a0b336a23f3c7d940cd60 |
| soap_message | StockQuote | SOAP |  | false | global | baf3bde50a0a0bdc7b10de1e2e7d72c1 |
| soap_message | TemperatureConvert | SOAP |  | false | global | d42866f00a0a0bd1548903a00b44d4bd |
| soap_message | WeatherForecast | SOAP |  | false | global | b6cf43e00a0a0bd06a4aca642df21248 |
| soap_message | demoi1 incident | SOAP |  | false | global | b6c634660a0a0bd0431995a69faad9b4 |

## Registered Events
| Event | Table | Fired By | Sys ID |
| --- | --- | --- | --- |
|  | sys_email |  | 008f8e621baa10d0ee26dd39cd4bcbe3 |
|  |  | any view of a record | 0130d0fb0a0a0b4201fd9ce4acb86abf |
|  |  | java class | 0137cba743422110d68db0e245b8f213 |
|  | service_task | Escalation Engine | 013bc31d1be22300985ba64fad4bcb63 |
|  | kb_feedback_task | Escalation Engine | 013bc31d1be22300985ba64fad4bcb6d |
|  | reconcile_duplicate_task | Escalation Engine | 013bc31d1be22300985ba64fad4bcb71 |
|  | change_request_imac | Escalation Engine | 013bc31d1be22300985ba64fad4bcb79 |
|  | statemgmt_renew_lease_task | Escalation Engine | 013bc31d1be22300985ba64fad4bcb80 |
|  | reclassification_task | Escalation Engine | 013bc31d1be22300985ba64fad4bcb83 |
|  | vtb_task | Escalation Engine | 013bc31d1be22300985ba64fad4bcb86 |
|  | kb_knowledge | kb_view.do | 014545050a0a0b4201ef59002eadfbe5 |
|  | sys_attachment | SysAttachment | 031bed0c0a0a0bdc266d1cf1e920cca1 |
|  |  |  | 0367265eebda211043ad0d94d852283a |
|  | sc_task | Business Rule | 0395ee4bc0a8010200a4f80e62a53845 |
|  | sc_task | Business Rule | 039657f2c0a80102002f3d17967ed845 |
|  |  | Check Scoped App Author Config Changes sysauto_script job | 043218e3c3301200f7d1ca3adfba8ff3 |
|  | sys_auth_policy_device_app_registry |  | 052bd0dac34a4110559d74c3e540dde5 |
|  | sn_customerservice_escalation | Escalation trend to changes | 052e8d59b3810300ba066e5f26a8dc3c |
|  | service_task | Escalation Engine | 053bc31d1be22300985ba64fad4bcb62 |
|  | sysapproval_group | Escalation Engine | 053bc31d1be22300985ba64fad4bcb65 |
|  | kb_feedback_task | Escalation Engine | 053bc31d1be22300985ba64fad4bcb6c |
|  | reconcile_duplicate_task | Escalation Engine | 053bc31d1be22300985ba64fad4bcb70 |
|  | statemgmt_renew_lease_task | Escalation Engine | 053bc31d1be22300985ba64fad4bcb7f |
|  | incident_task | Escalation Engine | 053bc31d1be22300985ba64fad4bcb82 |
|  | vtb_task | Escalation Engine | 053bc31d1be22300985ba64fad4bcb85 |
|  | gsw_task | Escalation Engine | 053bc31d1be22300985ba64fad4bcb88 |
|  | license_details | ServiceNow Subscription Downloader | 0562a000c3322100f4a13b251eba8f35 |
|  |  |  | 057030d05320030075b6cbaac2dc34cc |
|  | task_sla |  | 05c058fcc3122200b6dcdfdc64d3aeed |
|  |  | upgrade.js | 0706654b0a0a0a650081ce30e64dcfe0 |
|  | sysapproval_approver | Approval Events (Non-Task) Business rule | 07435201ef001000dada097009225619 |
|  |  |  | 087d31684361111030dbf03a5ab8f239 |
|  | sysapproval_group | Escalation Engine | 093bc31d1be22300985ba64fad4bcb64 |
|  | chat_queue_entry | Escalation Engine | 093bc31d1be22300985ba64fad4bcb6f |
|  | change_request_imac | Escalation Engine | 093bc31d1be22300985ba64fad4bcb7a |
|  | recommended_field_remediation | Escalation Engine | 093bc31d1be22300985ba64fad4bcb7e |
|  | incident_task | Escalation Engine | 093bc31d1be22300985ba64fad4bcb81 |
|  | reclassification_task | Escalation Engine | 093bc31d1be22300985ba64fad4bcb84 |
|  | gsw_task | Escalation Engine | 093bc31d1be22300985ba64fad4bcb87 |
|  | sn_customerservice_case | Business Rule 'Case closed RP notifications' | 098a4124eb333010bbd186de42522808 |
|  |  |  | 09df8292c6112275014f5a314af32bd7 |
|  |  |  | 0a018d0ec6112275001cdfc2c154e528 |
|  | cert_task | certification task business rule | 0b1cce34c3413000c111113e5bba8fb0 |
|  |  | Workflow activity (Notification) | 0b47918f0a0a0b273be2146a788979f1 |
|  | ecc_agent | 'Agent status monitor' Business Rule | 0b637d6f4a362312007aee4ece815fbc |
|  |  |  | 0bae447c370121009a80a0ffbe41f11d |
|  |  | Notification engine | 0bc2f1118f0020001c519cfde0f923cc |
|  | sn_actsub_activity | Business Rule | 0c958d120f920010e6d4fd820b767e9c |
|  |  | java class | 0ca607a743422110d68db0e245b8f2ff |
|  |  | VA Topics/Topic Blocks after successful deflection | 0cb48d4d5347201033cdddeeff7b12d3 |
|  | change_request | change events business rule | 0ccc46f0b7620010fa5b8644de11a968 |
|  | sn_customerservice_escalation | Escalation state changes to closed | 0d005c44b3600300ff6e6e5f26a8dcdd |
|  | problem_task | Escalation Engine | 0d3bc31d1be22300985ba64fad4bcb60 |
|  | sysapproval_group | Escalation Engine | 0d3bc31d1be22300985ba64fad4bcb63 |
|  | chat_queue_entry | Escalation Engine | 0d3bc31d1be22300985ba64fad4bcb6e |
|  | reconcile_duplicate_task | Escalation Engine | 0d3bc31d1be22300985ba64fad4bcb71 |
|  | change_request_imac | Escalation Engine | 0d3bc31d1be22300985ba64fad4bcb79 |
|  | recommended_field_remediation | Escalation Engine | 0d3bc31d1be22300985ba64fad4bcb7d |
|  | statemgmt_renew_lease_task | Escalation Engine | 0d3bc31d1be22300985ba64fad4bcb80 |
|  | reclassification_task | Escalation Engine | 0d3bc31d1be22300985ba64fad4bcb83 |
|  | gsw_task | Escalation Engine | 0d3bc31d1be22300985ba64fad4bcb86 |
|  | sys_email |  | 0df40b743b032300c869c2c703efc49d |
|  |  | SysAttachment | 0e29421383101000dada83ec37d9292d |
|  | pwd_process | Script include | 0e71d8c453f330106bdaddeeff7b12f7 |
|  |  | Script Include: SoCDefinitionSNC | 0f6e1a1d57501300532c3da73d94f971 |
|  |  | NextBestActionServiceImpl script include | 104db2d1432312102280698f38b8f26f |
|  |  |  | 1171596db7232300be6198c1ee11a938 |
|  | dscy_credentials_affinity | BRs: "Cleanup Credential References" and "Remove Credential Affinity" | 11a3d54cff3220103894c787d53bf1f9 |
|  |  |  | 11d83fb2731020100a5310c92bf6a7e2 |
|  | sn_employee_app_access | sn_employee._addAccessToApp | 11fab976775d1110a956b9999a5a99d5 |
|  |  | Script Include | 13f063620f124010b25fea12ff767e57 |
|  | sys_ux_screen | UIBTK Duplicate Page Scripted REST API | 1458f77c9d231110f8772de6b52d4d2f |
|  | cmdb_data_management_task |  | 14b5ebffff4c22107716ffffffffff2c |
|  | wm_task | Scheduled Job Trigger | 16c653c34f462200bb5e89bf0210c785 |
|  |  | After Task-To-CI creation completes | 172410fb7370301026f6aa114df6a756 |
|  | jwt_keystore_aliases | Fired by JWT Key Expiry Notification Scheduled Job | 1762a8e6b7842300616ceb67ee11a9cb |
|  |  | Script Include | 17f5aff20f022010b25fea12ff767e5f |
|  |  | IndexEvent | 17ff3e2453320010bca8ddeeff7b124c |
|  | ecc_queue |  | 18e291a77f3012008c5abb87adfa9156 |
|  |  |  | 190504d2cb223300a54f78d5634c9c84 |
|  |  |  | 19aa608eff0022104cdfffffffffff79 |
|  | pa_job_logs | Data Collector Job | 1a7a4120d7330100fa6c0c12ce61030e |
|  | task | Change events and task events business rules | 1a931f1dc61122aa01dc7b3e9a40b0fa |
|  |  | Scheduled Imports | 1aa678e10a0a0b390013704d50834286 |
|  | kb_social_qa_vote | Business rule | 1aad96abc32331006f333b0ac3d3ae2b |
|  |  | Script Include | 1ac694a90f521010b25fea12ff767e87 |
|  | sn_ex_sp_notifs_portal_notification_content |  | 1bd8487e77bf4210ed6c756f1b5a9928 |
|  |  | Data Collector Job | 1c792776a3312110891437af26fcda98 |
|  | sn_customerservice_case |  | 1c92fd861b783b00985ba64fad4bcbec |
|  | kb_knowledge | Approval Publish workflow | 1cfa0301b7403300343f08a9ee11a902 |
|  | task_activity |  | 1d70bcc7eb02310023c7a9bcf106fe73 |
|  | sc_request |  | 1da94fd11b9a9050985ba64fad4bcb0d |
|  | pwd_map_proc_to_group | Java class | 1df2506a531330106bdaddeeff7b12f6 |
|  | sc_req_item | sc_req_item comment events business rule | 1e0608bd0a0a3c74018096fc93d76513 |
|  |  | ExternalUserManagementUtils script include | 1e15cea9c36b10103e6eb0c7c840dde4 |
|  | sc_req_item | sc_req_item comment events business rule | 1e2376fd0a0a3c7401655b3386d6ca89 |
|  |  | UpdateChecker.checkAvailableUpdates | 1e5b3df9c3011200f7d1ca3adfba8fb5 |
|  | change_request | change events business rule | 1ed4311e9720200031af390ddd29755d |
|  | cab_attendee |  | 1f05204eebf022002a7a666cd206feae |
|  | live_group_member | business rule | 1f5de5e7c32321006f333b0ac3d3ae11 |
|  | cmdb_data_management_task |  | 1fa8f7920723201017b703767cd30004 |
|  | sn_customerservice_escalation | Escalation assigned to changes | 200ab851b3410300ba066e5f26a8dc05 |
|  |  |  | 2060fc905320030075b6cbaac2dc34ef |
|  |  | SysAttachment | 2080620183101000dada83ec37d9295c |
|  | sc_request |  | 20afa9991b4c5c10ea17dd3fbd4bcb39 |
|  | sys_push_feedback | Push plugin fires after being told of an invalid device | 2146f662ff0102009738fffffffffff2 |
|  | hermes_ip_filtering_audit |  | 219273924f83121071e0a0e552ce0b2c |
|  | sys_table_rotation | TableRotation business rule when a table rotation is deleted | 2225b74f0a0a0b9500bc25aac391cccc |
|  | sys_user_group | Java class | 228043ec533330106bdaddeeff7b1254 |
|  | interaction |  | 22892ea2ff2b0610cabbf6648c4fd90c |
|  |  | TextIndexActionHandler | 228d76f25320320025472c39e3dc34b5 |
|  | sys_app | Business Rule: Fire app created event on insert | 23584c2693d7021048080b7e92891837 |
|  | sn_customerservice_case | Business Rule 'Case resolved RP notifications' | 239a8524eb333010bbd186de4252289e |
|  |  | Script Action | 23ac33076710001017f141119585ef42 |
|  | sysapproval_approver | Approval Events (Task) | 2416a792933002003b7a7a75e57ffbc5 |
|  |  |  | 2474f282775202106d1fe8898c5a996d |
|  | change_task | Escalation Engine | 24d7b1929760200031af390ddd297522 |
|  |  |  | 27380c9ac30a4110559d74c3e540dd20 |
|  |  |  | 27788c9ac30a4110559d74c3e540dd36 |
|  | pa_indicator_breakdowns | PA fire scores clean up event on delete | 27bc6d60d70022004cd2a3b20e6103ab |
|  |  |  | 2827eec28b7b9210e5414e5bf12395aa |
|  |  | Script Include | 286ed68993901300ac40f5be867ffba1 |
|  |  |  | 28cd728553113200d47ccbaac2dc34cb |
|  | task_activity |  | 2b86f9b0eb02310023c7a9bcf106fe08 |
|  |  |  | 2bb73a00c301020055d9db1122d3ae02 |
|  |  | cmdb.group.modified | 2be8a2a673220010af8a1fd9fdf6a75e |
|  | release_feature | SNC Release feature events | 2cdb1c67a9fe3dba014df29d5bded769 |
|  | release_feature | SNC Release feature events | 2cdb6443a9fe3dba01a4d2f004ab7395 |
|  | release_feature | SNC Release feature events | 2cdba353a9fe3dba01a286f4d99ef41e |
|  | release_feature | SNC Release feature events | 2cdbed38a9fe3dba006318eec2e9dff0 |
|  | release_feature | SNC Release feature events | 2cdc21dfa9fe3dba01fe51f7bb542ba6 |
|  | release_phase | SNC Release phase events | 2cdecef5a9fe3dba0104eff493620801 |
|  | release_phase | SNC Release phase events | 2cdf01e4a9fe3dba01c75e31d367b4dc |
|  | release_phase | SNC Release phase events | 2cdf377ca9fe3dba00eae25ba25a52f3 |
|  | release_project | SNC Release project events | 2ce1cb25a9fe3dba011b26687b7c05dd |
|  | release_project | SNC Release project events | 2ce21d73a9fe3dba013c4b62c18cc9e4 |
|  | release_project | SNC Release project events | 2ce26a97a9fe3dba01de30c8d4df37c5 |
|  | release_project | SNC Release project events | 2ce2b992a9fe3dba01e00a26f08a05ce |
|  | live_group_member | business rule | 2d6515d3c32321006f333b0ac3d3aeea |
|  | sc_request | sc_request events business rule | 2d989086c611228401eee3fb98941f2f |
|  | sc_request | sc_request events business rule | 2d98c90dc61122840136d1d7a0932193 |
|  | sc_req_item | sc_request events business rule | 2d994fc6c611228400f801c423771aa0 |
|  | kb_knowledge | kb_view.do | 2e16c9bc0a0a0b52009746da75ea5e56 |
|  | jwt_keystore_aliases | Fired by JWT Key Expired Notification Scheduled Job | 2e307befb7002300616ceb67ee11a9fe |
|  |  | Business rule: Generate chgMgt Event | 2e5570e9b74323000999e4f6ee11a9ed |
|  | sysapproval_approver | Approval Events (Non-Task) Business rule | 2e7e5d30ef001000dada0970092256da |
|  |  | Capacity based license count | 2e8988cc773210100afbf62ad9106146 |
|  | sc_request | sc_request events business rule | 2f336219c0a80064009a44f176e9e7e9 |
|  | kb_feedback_task | UI action when resolution is rejected for a feedback task  in kb_feedback_task table | 2f3fd19667001300d358bb2d07415a0d |
|  | sc_req_item | business rule | 2f40ba60c0a800640127077b71e98869 |
|  | sc_req_item | sc_request events business rule | 2f410a05c0a80064018a62f680622a94 |
|  | sc_request | sc_request events business rule | 2f42f79fc0a8006401ec0130b3ba97f1 |
|  | sn_doc_task | Fired by BR : Trigger event for review doc task | 2f4369f5c77b0010296ad3de17c260df |
|  |  |  | 30a3d013b771011071b980408e11a942 |
|  | par_dashboard | Hard coded | 316c2daaa3a642100abcad2f241e6103 |
|  | sn_customerservice_case | updates to the case | 325a6cee3b630300b5c42479b3efc415 |
|  |  |  | 32f2c4d8b782011071b980408e11a99f |
|  |  | Benchmark data upload | 334a2bb46720320097eeff5557415a05 |
|  | sys_report_import_table | [Reporting]  Import Tables expired | 33d7e161d72322005aed4ebfae6103ef |
|  |  | CSDM Lifecycle operation | 343be3a64303b11017b739603ab8f297 |
|  |  | CiModelProcessor | 346b1465c30013003e76741e81d3aefd |
|  | cmdb_policy_ci_exclusion_list |  | 3480c13177af7110bac410ed9f5a999d |
|  |  | Scheduled job | 34b8d08e3b772200b90c4bb534efc440 |
|  |  | System | 35377b73c3003010fdbd3f57bb40dd30 |
|  |  |  | 3559d45a530902106adfddeeff7b12e2 |
|  |  |  | 355b31c3ff11301010bad66cf43bf136 |
|  |  | sn_admin_center.AdminCenterUtil sys_script_include | 35cf2aa8436b5510b643a7ec6bb8f28b |
|  |  |  | 364dfa32534310105f48ddeeff7b12ae |
|  | cab_attendee |  | 366c4e58dbe732004d27b31be0b8f5b1 |
|  | sys_email |  | 36961a601b0ae090ee26dd39cd4bcbb5 |
|  |  |  | 36c4ccc24323021098ae9cd82ab8f2bd |
|  |  |  | 36ff5d20c0a808ae00f3e6f8f3299a3b |
|  |  |  | 38a83c7e0b9022005775aabcb4673a9d |
|  | sys_user_grmember | Business Rule | 3a1ee565c3323010a282a539e540dd71 |
|  | catalog_category_request | Not fired | 3a6c71705f1211001c9b2572f2b4773e |
|  |  | KMF module key registry | 3a79d1131b03011070fe4195d34bcbd8 |
|  | sc_req_item | Business Rule | 3adf79d97f00000100e4de50c13b0d72 |
|  | sysevent | System | 3ae8311714dc1700964fa81e247aa8cb |
|  |  |  | 3b48ee6b77223110411d94b92c5a998d |
|  | sn_communities_activity | Script Action | 3b6093fa67a722005ab69a6617415abf |
|  | sys_search_context_config |  | 3c59600dff6c2210c0f1ffffffffffee |
|  |  | Scheduled Job | 3db1fe5a7f7812107629a6470d86655a |
|  | change_request | change events busines rule | 3e30a3c9c61122810068969c218a6d87 |
|  | change_request | change events busines rule | 3e529640c611228101c3e05a71e5384b |
|  | sn_ex_sp_portal_extensible_navigation |  | 3e6afeb33b55921008a989da26e45a00 |
|  | pa_breakdowns | PA fire scores clean up event on delete | 3e8c57a2d73312004cd2a3b20e610310 |
|  |  |  | 3eaf727177522110b61ec1bfbd5a995f |
|  | ecc_queue | SensorProcessor.java | 3ff0eccdc30303003e76741e81d3ae8e |
|  | sn_customerservice_case |  | 406015e51b90a0502fd8db5be54bcbf7 |
|  | sys_email |  | 409b76da1b3e60903c0ffc4e0d4bcb58 |
|  | required_field_remediation | Escalation Engine | 413bc31d1be22300985ba64fad4bcb67 |
|  | kb_submission | Escalation Engine | 413bc31d1be22300985ba64fad4bcb6a |
|  | orphan_ci_remediation | Escalation Engine | 413bc31d1be22300985ba64fad4bcb73 |
|  | std_change_proposal | Escalation Engine | 413bc31d1be22300985ba64fad4bcb76 |
|  | live_message | Collaboration | 41ae5bb29f132100d5f9b3e2957fcf04 |
|  |  |  | 42123313eb0001105843ceb2b2522800 |
|  | reminder | Business Rule | 4259e20bc611227d016f48e481556643 |
|  |  |  | 43433200eb1011105843ceb2b2522800 |
|  |  |  | 437d2132eb0101105843ceb2b2522800 |
|  |  | A scheduled execution of POP3ReaderJob | 441bde430ffb00108299c37ac4767e72 |
|  | required_field_remediation | Escalation Engine | 453bc31d1be22300985ba64fad4bcb66 |
|  | cert_follow_on_task | Escalation Engine | 453bc31d1be22300985ba64fad4bcb69 |
|  | std_change_proposal | Escalation Engine | 453bc31d1be22300985ba64fad4bcb75 |
|  | stale_ci_remediation | Escalation Engine | 453bc31d1be22300985ba64fad4bcb78 |
|  | kb_knowledge_base_request | Escalation Engine | 453bc31d1be22300985ba64fad4bcb7c |
|  | cmdb_ci_outage | Business Rule | 46e17c41d7111200a9addd173e24d450 |
|  | par_export_job | Business Rule | 4737fdbc9f40121006dd0127aa0a1c31 |
|  | reminder | Business Rule | 475919ecc611227d00b04589dccb48eb |
|  | sys_certificate | certificate events business rule | 48160f650a0a0b2400918290a0b16963 |
|  | ast_contract | Condition check definition for Contacts table | 4895906fc0a8016400ae07cadff149cf |
|  | cert_follow_on_task | Escalation Engine | 493bc31d1be22300985ba64fad4bcb68 |
|  | orphan_ci_remediation | Escalation Engine | 493bc31d1be22300985ba64fad4bcb74 |
|  | stale_ci_remediation | Escalation Engine | 493bc31d1be22300985ba64fad4bcb77 |
|  | kb_knowledge_base_request | Escalation Engine | 493bc31d1be22300985ba64fad4bcb7b |
|  | sys_email |  | 49523a9e1bfa60903c0ffc4e0d4bcb9f |
|  | sn_apptmnt_booking_appointment_booking |  | 495cbeba5bfe0010f22b6e533381c705 |
|  | ecc_agent | "Agent status monitor" BR when MID's status is updated | 4965e6eb9fd9130055063758442e7056 |
|  | sys_certificate | certificate events business rule | 49741870c0a8006f00fa00f350ba623a |
|  | cmdb_ci_outage | Business Rule | 49c17c41d7111200a9addd173e24d44c |
|  | ecc_agent_cluster | MID Server Cluster Management | 4a1378c20a0006bc119174b2dde99e18 |
|  | sys_hub_trigger_template |  | 4a4a45d0ffcb52105cd1c9c403cb14ef |
|  | problem_task | problem_task events business rule | 4a70db520a0007040020ccac7cdac1de |
|  | problem_task | problem_task events business rule | 4a7192460a000704019a081837d4b385 |
|  | problem_task | problem_task events business rule | 4a71fea80a00070401ab71c23eccd0c3 |
|  | problem_task | problem_task events business rule | 4a722ffe0a00070401179ae1e20aab4e |
|  | problem_task | problem_task events business rule | 4a726c530a000704016a6469f6fd41bd |
|  | problem_task | problem_task events business rule | 4a72bdea0a00070400257edfee9d90a4 |
|  | problem_task | Escalation Engine | 4a730f7f0a000704001e92794bb8f83f |
|  | ecc_agent | MID Server Monitor scheduled job | 4b1fb8030ab30157002aa160dbb58a79 |
|  |  | ImportSetRun | 4b36734047101200c3dad7527c9a71c6 |
|  | task_sla | SLA workflow activity | 4b7ac3530a0a0b300099153f83980d2f |
|  | task_sla | SLA workflow activity | 4b83f3410a0a0b3000a899b441916c7b |
|  |  |  | 4bd1faf34311211084dedd2db9b8f232 |
|  | sc_cat_item |  | 4c2069017716211047c88f1a5b5a9993 |
|  | incident | incident events business rule | 4d0b7e44c611227b010619b714a8b983 |
|  | cert_follow_on_task | Escalation Engine | 4d3bc31d1be22300985ba64fad4bcb67 |
|  | kb_submission | Escalation Engine | 4d3bc31d1be22300985ba64fad4bcb6a |
|  | orphan_ci_remediation | Escalation Engine | 4d3bc31d1be22300985ba64fad4bcb73 |
|  | stale_ci_remediation | Escalation Engine | 4d3bc31d1be22300985ba64fad4bcb76 |
|  | live_message | business rule | 4d972d99ff220000dadaebcfebffadcc |
|  | cert_task | Escalate UI Action | 4da965f04741300042bd757f2ede2743 |
|  | sn_apptmnt_booking_appointment_booking | Scheduled Job | 4dc272d1b3775300eda5a72256a8dc22 |
|  |  | When offering commitment is inserted or updated | 4e59d54e0790b01070e493d0fad3009a |
|  | sysapproval_approver | Business rule "Approval Events (Non-Task)" | 4ebcf5c6b7122300bc1308a9ee11a94c |
|  |  | Fix script | 4f2ed1bbcba013008c061aeb034c9c79 |
|  | sc_cat_item |  | 4f949ad0532310101553ddeeff7b1211 |
|  |  | java class | 4f982202536130106bdaddeeff7b12ce |
|  | sc_task | sc_task events busines rule | 5038008c4a362312008bdd85783f56f4 |
|  | wm_order | When a request is created via email | 508bb9a7c3323100ba9ddccdf3d3aebe |
|  |  | Check Scoped App Updates sysauto_script job | 50afff53c3301200f7d1ca3adfba8f46 |
|  |  |  | 511a2212eb3011105843ceb2b2522800 |
|  | fm_ci_rate_card | scheduled job 'CI Rate Card Item Review' | 514a004dc0a80a6d4690c37dfced51f1 |
|  |  | Business Rule | 5159116eec261110f877c235d1257741 |
|  |  |  | 520720314301211069aaacbb89b8f200 |
|  | live_mention |  | 52808409474221007f47563dbb9a71e2 |
|  |  |  | 528b0312430231104a584cb0d9b8f200 |
|  |  |  | 53d620314301211069aaacbb89b8f200 |
|  |  |  | 53e62313430321109c0c4cb0d9b8f200 |
|  | sys_one_extend_batch_run | OneExtend Evaluation service implementor | 5583533393eb52106f9d4b2f34891860 |
|  | sc_request |  | 5586f6911b1a9050985ba64fad4bcb8c |
|  |  | Updatechecker script include | 55a400fa0f173300886e67bcfa767e2b |
|  | ldap_server_config | LDAP Connection Test | 560e5073c303210016194ffe5bba8fbf |
|  | incident |  | 57239b7ac31611100f24c87af040ddfb |
|  |  | Script Include | 57acb47f3b030300b90c4bb534efc476 |
|  |  |  | 57b055d05382011071b9ddeeff7b12a7 |
|  | sn_customerservice_case |  | 57b09d101b98a8102fd8db5be54bcb61 |
|  | live_message_like |  | 585b5337c0a80a6d138f422aacf15979 |
|  | live_message |  | 585d25a4c0a80a6d3b1fa8e4f7fd6fb2 |
|  | live_message |  | 58614ce3c0a80a6d4a02ceb73328c9bd |
|  | asmt_assessment_instance | Subflow when 50% of an assessment duration is passed | 5864f55dd7220100c11180f29e6103f1 |
|  | service_offering | Business Rule: CSDM - Support Group and Change Group | 59a9b8977302101061b79c0c6df6a7bc |
|  | sn_customerservice_case |  | 59be81251b90a0502fd8db5be54bcbee |
|  | sc_request |  | 59f323501b445810ea17dd3fbd4bcbc7 |
|  |  | sn_admin_center.AdminCenterUtil sys_script_include | 5b22ba27b7b611109cfe23508e11a9e1 |
|  |  | Scheduled Job | 5b766a6a7fa112107629a6470d86658a |
|  | sys_sync_history | System | 5b97c003bf0211002eff1c2a7f073963 |
|  | cmdb_ci_outage | Business Rule | 5be17c41d7111200a9addd173e24d413 |
|  | wm_task | When the state, assignee, assignment group and work notes are changed | 5c8bb9a7c3323100ba9ddccdf3d3aebe |
|  | sn_actsub_activity | Business Rule | 5cf341120f920010e6d4fd820b767eef |
|  | cmn_notif_device | Script Include | 5d7ea7960b300300572a6f3ef6673a5f |
|  | pwd_cred_store |  | 5d98f9579f020300e78d317f842e70f4 |
|  | sys_user | System | 5e1449bb0a0a0a0a0082b92b59be7d84 |
|  | sys_user | System | 5e1477260a0a0a0a018460583a8bbf97 |
|  | sys_user | System | 5e14da500a0a0a0a0139e80ce5debc2c |
|  |  | System | 5e64b59c938712109439a3cd91891881 |
|  | sc_cat_item |  | 5e8786d0532310101553ddeeff7b126b |
|  | kb_social_qa_vote | Business rule | 5f4e56abc32331006f333b0ac3d3aeeb |
|  |  |  | 5f6212eaffb83110d185612a453bf187 |
|  | cab_attendee |  | 5fb06fa5ebf022002a7a666cd206feda |
|  |  |  | 5fc2900647be61503fbe9e25126d4346 |
|  | cmdb_ci_business_process | scheduled job | 5fce269373d31010ec95d11ee2f6a757 |
|  |  |  | 6019577a77623110411d94b92c5a99e3 |
|  |  |  | 603f303343222110fafaacbb89b8f200 |
|  |  |  | 605c1212eb3301105843ceb2b2522800 |
|  | pwd_reset_request | Script include after verifying user in Password reset flow | 605de0785352011026b0ddeeff7b12b5 |
|  |  | Password Reset Activity Monitor: business rule | 60910834eb2201002db7648d9106fe69 |
|  |  |  | 609c2022eb1111105843ceb2b2522800 |
|  |  | Business rule: Generate chgMgt Event | 60a4d3d1b79323000999e4f6ee11a9eb |
|  |  |  | 60b63133eb1201105843ceb2b2522800 |
|  |  |  | 60c657e3c0a8018c0099ba6cd4f3b11f |
|  | sys_broadcast_message | ServiceNow HI | 60feba2147200200151119fbac9a719e |
|  | appsec_domain_result_set | Business Rule | 6197d67d53a31300a699ddeeff7b1261 |
|  | asmt_assessment_instance | Dispatch Survey Notification Event | 61e84d7ac7323010e028dc8703c26027 |
|  | sn_customerservice_escalation | Escalation state changes to declined | 61ff4c44b3600300ff6e6e5f26a8dcac |
|  |  |  | 628d2132eb0101105843ceb2b2522800 |
|  |  |  | 62e511336703311096c87ff538f92200 |
|  |  | java code | 6314272f43822110d68db0e245b8f294 |
|  |  |  | 6356123343313110fafaacbb89b8f200 |
|  |  |  | 638620314301211069aaacbb89b8f200 |
|  |  |  | 6392000143113110fafaacbb89b8f200 |
|  | sys_sync_history | Cancel code review UI action | 63a0c733d702110050f5edcb9e6103d6 |
|  |  | 'Update MID Server Status table' and 'Update mean on MID Server Status' Business Rules | 643fc13ac740320003fa9c569b9763d1 |
|  | task_ci |  | 656a8f2e0a0a0b8700b84a541cbc0511 |
|  | incident |  | 656bb9130a0a0b8700465032465ad356 |
|  | incident |  | 656c1d570a0a0b87006a364977919ba1 |
|  |  | Notification Action API | 65c81d92c312201032dd09c77d40dd4f |
|  | syslog |  | 65fe3aff1b515450ea17dd3fbd4bcb41 |
|  | kb_feedback_task | UI action when resolution is accepted for a feedback task  in kb_feedback_task table | 666f959667001300d358bb2d07415a3a |
|  | kb_social_qa_answer |  | 66ac49f6d701120023c84f80de61032d |
|  | cmdb_data_management_task |  | 66b0763a772320108043270bba10612d |
|  | sysapproval_approver | Approval Events (Task) | 66e97252933002003b7a7a75e57ffb91 |
|  | live_group_member | business rule | 67d415d3c32321006f333b0ac3d3ae29 |
|  | sys_app_template | Java code when templates are run | 680889ac770301101209442a2c5a998d |
|  | sn_customerservice_escalation | Escalation comment changes | 691ab851b3410300ba066e5f26a8dce9 |
|  | m2m_app_theme | Graphql resolver for updating order for theme builder | 69694a33ff2422107484ffffffffff57 |
|  |  |  | 697d5d0e1bf43b00985ba64fad4bcb9e |
|  | license_details | system | 69dedea30b13220000ea8cddb4673a44 |
|  | one_api_service_plan_feature_invocation | OneApi Feature Script Executor | 6b0d281253b4a1101fdbddeeff7b1297 |
|  |  | Script Includes | 6b5a5e133bb8030037556b4ee3efc463 |
|  |  |  | 6bdd0382eb7021106564ab7e1a5228b0 |
|  |  |  | 6bddc406d731120023c84f80de6103cb |
|  |  | System | 6c403a3b0a0a0ba7007d57202fad3e8e |
|  |  | System | 6c409b1e0a0a0ba700584784227bafbd |
|  |  | System | 6c4187000a0a0ba700a7b4e0bf28039e |
|  | sm_order | When a request is created via email | 6c705a76df713100b5157a0d3df263c3 |
|  | kb_feedback_task | Business rule when a feedback task is reassigned in kb_feedback_task table | 6c8a463d67330300d358bb2d07415a98 |
|  | problem | problem events business rule | 6cd631929760200031af390ddd2975f9 |
|  | sys_search_suggestion_blacklist |  | 6cfca76b0f7323003d0e4062ff767e92 |
|  | itil_appointment | Global business rule | 6d18044dc611227a010d4fcf6e6a2d7e |
|  | itil_appointment | Global business rule | 6d187370c611227a01c76b8dc79f732d |
|  | kb_knowledge |  | 6df034fa77a10210972839bd1e5a9993 |
|  | pa_job_logs | Data Collector Job | 6e210cb2d7321100fa6c0c12ce610312 |
|  |  |  | 6e7f74f8ffe68a10d68b65d7d3b8fee9 |
|  | provider_auth | com.glide.external.app | 6e9964733b270300c869c2c703efc411 |
|  |  | System | 6ea4fdbbc32220102c5b4e483c40dd7b |
|  | kb_social_qa_question | Business rule | 6f1d56abc32331006f333b0ac3d3ae91 |
|  | global | Scheduled Job | 6f42e7250b02030031a567bff6673a3f |
|  | ecc_agent | MID Server Monitor scheduled job | 6ff2078253531200dd41a3c606dc3458 |
|  |  |  | 70022232eb1301105843ceb2b2522800 |
|  |  | ui page | 7099f3a94fc1421028d79e4628c714bd |
|  |  |  | 70f13313eb0001105843ceb2b2522800 |
|  | customer_contact |  | 71051bb3c363020095ccd02422d3ae65 |
|  |  | Sidebar responder to calculate unread badge count | 715ef11043e22110d1064006fbb8f200 |
|  | cmdb_ci_outage | Script Action | 723e8c92d7111200a9addd173e24d4af |
|  |  | Script:  EntitlementsDisplayDetailsDownloader._postProcess | 7257a84143b10210243f9cd82ab8f2c4 |
|  |  |  | 72f7130067111110acf57ff538f92200 |
|  |  |  | 73223313eb0001105843ceb2b2522800 |
|  | ml_solution_definition | Trigger which checks for data abundance for ML trainings | 73820bdab7033300d4260f98ee11a9bf |
|  |  |  | 73923313eb0001105843ceb2b2522800 |
|  |  |  | 73a8481f1ba592105b3a54e3604bcb5c |
|  |  |  | 73cc0220eb0011105843ceb2b2522800 |
|  | sn_apptmnt_booking_appointment_booking |  | 74043fbe5b368010f22b6e533381c7eb |
|  | kb_knowledge | KBViewModelSNC | 74ceb98a90746210f877797bb141761d |
|  | wm_task | When the assignment group is changed | 7555fe7a4f462600bb5e89bf0210c79d |
|  |  | Business rule: Generate chgMgt Event | 75687109c3e22010a282a539e540dd29 |
|  | life_cycle_mapping | UI Action on List | 7685387273b210109cc5aa114df6a795 |
|  | sys_report | Hard coded | 787473960a0a3c19016bb3f9dc1cf669 |
|  | sys_report | Hard coded | 78b0eee10a6aae7201f3ce9f31908798 |
|  |  | System | 78cf7a62c33120102c5b4e483c40dd68 |
|  | live_poll | business rule | 78ff5b22472321007f47563dbb9a718d |
|  |  |  | 791d0d1f77333110ee0d0cc2fa5a99ce |
|  |  | Business Rule | 79765839c7133010bb93c49af4c2600e |
|  | cert_task | certification task events Business Rule | 79d85bda0a00070449f6d5375c81700a |
|  | cert_instance | certification instance events Business Rule | 79d90d280a0007047d39896d877963e1 |
|  | cert_audit_instance | certification audit instance events Business Rule | 79d9c1f00a000704777c5ef06acd0cb2 |
|  | cert_audit_instance | certification audit instance events Business Rule | 79d9f0380a0007046db17ad105346716 |
|  | cert_instance | certification instance events Business Rule | 79da25a60a00070449df4b58804d8587 |
|  | cert_element | certification element events Business Rule | 79db04840a0007046ab97614dcc91f85 |
|  | problem_task | problem_task events business rule | 7a3e87a25f011000b12e3572f2b47752 |
|  |  | Business rule: Generate chgMgt Event | 7a6e46cfb74323000999e4f6ee11a9a2 |
|  | sysevent | System | 7b77b99314dc1700964fa81e247aa8f8 |
|  | sn_apptmnt_booking_appointment_booking |  | 7c8c7eba5bfe0010f22b6e533381c72a |
|  | change_task | Escalation Engine | 7cd6fd529760200031af390ddd297578 |
|  |  |  | 7cd88994c3601300e7c7d44d81d3ae90 |
|  |  | Business Rule | 7d2682580f470010b25fea12ff767e50 |
|  |  |  | 7d9b4ff2c31611100f24c87af040dd08 |
|  | cab_attendee |  | 7e30dc03ebf022002a7a666cd206fee7 |
|  |  |  | 7edbfc062bc19210a757f5236e91bf9e |
|  |  | script | 7ef33e0a93c22010ebd4f157b67ffb81 |
|  | task_activity |  | 7ef4700beb02310023c7a9bcf106fefb |
|  |  |  | 7f6a863e534f02106adfddeeff7b12b9 |
|  | multi_factor_browser_fingerprint | System | 8006763673323300fdbd04fbc4f6a791 |
|  |  |  | 803e5e195ff302105e9db48b6773136d |
|  | problem_task | Escalation Engine | 813bc31d1be22300985ba64fad4bcb61 |
|  | sysapproval_group | Escalation Engine | 813bc31d1be22300985ba64fad4bcb64 |
|  | chat_queue_entry | Escalation Engine | 813bc31d1be22300985ba64fad4bcb6f |
|  | change_request_imac | Escalation Engine | 813bc31d1be22300985ba64fad4bcb7a |
|  | recommended_field_remediation | Escalation Engine | 813bc31d1be22300985ba64fad4bcb7e |
|  | incident_task | Escalation Engine | 813bc31d1be22300985ba64fad4bcb81 |
|  | reclassification_task | Escalation Engine | 813bc31d1be22300985ba64fad4bcb84 |
|  | gsw_task | Escalation Engine | 813bc31d1be22300985ba64fad4bcb87 |
|  | cert_task | Certification task escalation | 81e926a4c3b03000c111113e5bba8fcb |
|  |  |  | 81f4870e7f0a9210f0791d6eec8665c9 |
|  |  |  | 81f546edc611222b0060029d66ebcafc |
|  |  |  | 8201131f77221110866ea2059f5a99ef |
|  | sc_task | business rule | 8252f413c0a8010a01bd21845bb17295 |
|  | sc_task | business rule | 8253247ac0a8010a018f17ceb08287eb |
|  |  |  | 828614e52b151210a757f5236e91bf6f |
|  |  |  | 82ac77ba47b665503fbe9e25126d4356 |
|  |  | ClusterReaper | 82c023710a0a0a65016339496372d74b |
|  |  |  | 82c494b2c611222b014b2f1a19acda28 |
|  | sysapproval_approver | Approval Events (Non-Task) Business rule | 83565201ef001000dada097009225635 |
|  |  |  | 83e88c5dffc832103694ffffffffff1a |
|  | problem_task | Escalation Engine | 853bc31d1be22300985ba64fad4bcb60 |
|  | service_task | Escalation Engine | 853bc31d1be22300985ba64fad4bcb63 |
|  | kb_feedback_task | Escalation Engine | 853bc31d1be22300985ba64fad4bcb6d |
|  | chat_queue_entry | Escalation Engine | 853bc31d1be22300985ba64fad4bcb6e |
|  | reconcile_duplicate_task | Escalation Engine | 853bc31d1be22300985ba64fad4bcb71 |
|  | change_request_imac | Escalation Engine | 853bc31d1be22300985ba64fad4bcb79 |
|  | recommended_field_remediation | Escalation Engine | 853bc31d1be22300985ba64fad4bcb7d |
|  | statemgmt_renew_lease_task | Escalation Engine | 853bc31d1be22300985ba64fad4bcb80 |
|  | reclassification_task | Escalation Engine | 853bc31d1be22300985ba64fad4bcb83 |
|  | vtb_task | Escalation Engine | 853bc31d1be22300985ba64fad4bcb86 |
|  | pwd_expiration | Scheduled Job to send password expiration reminder. | 854a73025352301017c3ddeeff7b1248 |
|  | cmdb_ci_outage | Script Action | 858ac892d7111200a9addd173e24d40a |
|  | sys_user | System | 859b8a13c0a80164005d1333938ef440 |
|  | sys_user | System | 859e7bd4c0a8016400ac57420f7234b6 |
|  |  | Replication Engine | 86b3ac12c0a8000501f6c439dbbf6dcb |
|  | wm_task | Work Task State Flow - When the task is auto assigned to an agent | 86e8cf814f522600bb5e89bf0210c7ec |
|  | vtb_task | VTB Additional Assignee Update buisness rule | 8708e6f09330020092ffb46b767ffb14 |
|  | service_task | Escalation Engine | 893bc31d1be22300985ba64fad4bcb62 |
|  | kb_feedback_task | Escalation Engine | 893bc31d1be22300985ba64fad4bcb6c |
|  | reconcile_duplicate_task | Escalation Engine | 893bc31d1be22300985ba64fad4bcb70 |
|  | statemgmt_renew_lease_task | Escalation Engine | 893bc31d1be22300985ba64fad4bcb7f |
|  | incident_task | Escalation Engine | 893bc31d1be22300985ba64fad4bcb82 |
|  | vtb_task | Escalation Engine | 893bc31d1be22300985ba64fad4bcb85 |
|  | asmt_assessment_instance | Notify quiz user business rule | 895b32a66762220063b4c3105685efe8 |
|  |  | Script include on IAR model train complete | 89ca3c4dc7022110c59d3d9c95c26041 |
|  | task_sla |  | 89cc61421b2898d0ea17dd3fbd4bcb62 |
|  | discovery_status | script include DIscovery.complete() | 8a3500800a0a0b2e0072f1edbceac2f9 |
|  | sn_customerservice_case |  | 8a4e58e6773031101e9e557dcd5a996e |
|  | vtb_card | System | 8a5382a45f200010c5e240df2f7313a2 |
|  |  | Scheduled job | 8a7c9815c3313110458f1fec5440dd0c |
|  | sys_atf_test_suite_result | Business Rule: Send email upon test suite completion | 8aa24e8267232200cf8305225685ef3b |
|  | sn_customerservice_case |  | 8acb52921baa455018ba748bd34bcbd2 |
|  |  | Business rule | 8b138bda40222110f8771a97e2196d8f |
|  | change_request |  | 8b7dfd3223a823001488dc1756bf654f |
|  | pa_dashboards | Hard Coded | 8bc9cde2b7f52110997a9f78ce11a93b |
|  |  | label_user_m2m | 8c047c1ea3122110cf554fde36fcda93 |
|  | ml_solution | Business Rule | 8c6a80837364230080b29ca9faf6a71e |
|  | service_task | Escalation Engine | 8d3bc31d1be22300985ba64fad4bcb61 |
|  | sysapproval_group | Escalation Engine | 8d3bc31d1be22300985ba64fad4bcb64 |
|  | kb_feedback_task | Escalation Engine | 8d3bc31d1be22300985ba64fad4bcb6b |
|  | chat_queue_entry | Escalation Engine | 8d3bc31d1be22300985ba64fad4bcb6f |
|  | recommended_field_remediation | Escalation Engine | 8d3bc31d1be22300985ba64fad4bcb7e |
|  | incident_task | Escalation Engine | 8d3bc31d1be22300985ba64fad4bcb81 |
|  | vtb_task | Escalation Engine | 8d3bc31d1be22300985ba64fad4bcb84 |
|  | gsw_task | Escalation Engine | 8d3bc31d1be22300985ba64fad4bcb87 |
|  | cert_task | certification task business rule | 8da93326c3413000c111113e5bba8f45 |
|  | change_task | Escalation Engine | 8dd43d529760200031af390ddd297591 |
|  | sys_user | reset_password UI Page | 8e3e3b90465667e27946404ee43dcc15 |
|  | wm_task |  | 8e7822ac1b049810ea17dd3fbd4bcb9b |
|  |  | Script Include | 8ed7191653411110dd8eddeeff7b125b |
|  | interaction | Business rule "Append Internal Transcript" on interaction table | 8ed77dea73530010802a1f477bf6a785 |
|  | reminder | Business Rule | 8f0f8749c611227800fde7ba9d8efddc |
|  | sm_task | When the state, assignee, assignment group and work notes are changed | 8fd66920d7313100561583e80e61035f |
|  | sys_analytics_cache |  | 90fd342f43000210aaf41347efb8f238 |
|  | sn_actsub_activity | Business Rule | 9124c1120f920010e6d4fd820b767e01 |
|  | sn_doc_task | Fired by BR : Trigger event for review doc task | 916b6206c7730010296ad3de17c26002 |
|  | ldap_server_config | LDAP Connection Test - Scheduled Job | 9193f560c332010016194ffe5bba8fb5 |
|  | sn_customerservice_registration |  | 9195ba6cc32302003a657bfaa2d3ae8e |
|  |  | java class | 91d8757f531130106bdaddeeff7b1255 |
|  | cmdb_data_management_task |  | 923e28c90713201017b703767cd30004 |
|  | sysapproval_approver | approver changes business rule | 9277c1d1c0a8010a00c0b38595cb45b2 |
|  | sysapproval_approver | approver changes business rule | 9277f555c0a8010a00e022ae83d234d0 |
|  | sysapproval_approver | approver changes business rule | 92781b6bc0a8010a0043671d841cf76f |
|  | kb_social_qa_comment | Business rule | 931e96abc32331006f333b0ac3d3aebf |
|  | sysevent_queue_config |  | 942e62a4eb430210e78eed9c425228fa |
|  |  | UpdateChecker script include | 9484edd40fe53300b717be630b767eb7 |
|  | live_group_member | business rule | 94b415d3c32321006f333b0ac3d3ae30 |
|  | sn_customerservice_case | Business Rule 'Case closed RP notifications' | 960276e2eb123010bbd186de425228fd |
|  | live_group_member | business rule | 96c2eba1c0a801693ed9da25efd78c34 |
|  | live_group_member | business rule | 96c541afc0a8016945e68de0af76dab7 |
|  | live_group_member | business rule | 96c5a1b3c0a801690df29bb76eaceed6 |
|  | live_group_member | business rule | 96c64f5bc0a801691e7bd4df061b2d1b |
|  | change_request | A process which could effect the state of the Change Request but doesn't directly change the record | 96c8824553d3101034d1ddeeff7b12fd |
|  | sysapproval_approver | Approval Events (Non-Task) Business rule | 97425201ef001000dada097009225638 |
|  |  | TableRotation when it is determined that a rotation to the next table is required | 986276e30a0a0b8a005d4754e07d03dd |
|  | one_api_service_plan_feature_invocation | OneApi Feature Script Executor | 99468cb0531121101fdbddeeff7b121f |
|  | sys_user | reset_password UI Page | 99c4a1a39f031200f45c7b9ac42e70fc |
|  | pa_thresholds | PAThresholdJob | 99c7b872d7011100ef2281537e610372 |
|  | sn_customerservice_case | Business Rule 'Case commented RP notifications' | 9a1a0de0eb333010bbd186de425228a1 |
|  |  | Business rule | 9a610b9a40222110f8771a97e2196d26 |
|  | user_multifactor_auth | System | 9ad06a62d700020091204187ed6103c8 |
|  | pwd_map_proc_to_group | Java class | 9ad21c2a531330106bdaddeeff7b12c7 |
|  |  | Business rule: Generate chgMgt Event | 9c17693a23ab23001488dc1756bf65f4 |
|  | sc_cat_item |  | 9c73b68177021110271f07c77b5a9930 |
|  |  |  | 9d295c34c3212110547aab8f8740dde3 |
|  | live_group_member | business rule | 9d3515d3c32321006f333b0ac3d3ae90 |

## Events Used by Automation
| Event | Usage Count |
| --- | --- |
| polaris.follow.update | 1 |
| sc_cart_item.multi_row.orphan.delete | 1 |
| sc_task.commented | 1 |
| sc_task.worknoted | 1 |
| sc_task.updated | 1 |
| sc_task.state.changed | 1 |
| sc_task.assigned.to.user | 1 |
| sc_task.assigned.to.group | 1 |
| sn_apptmnt_booking.cancelled | 1 |
| spm.availability.calculate | 1 |
| wo.task.assigned.to.group | 1 |
| ci.notification.for.task | 1 |
| group.affected | 1 |
| location.affected | 1 |
| record.send_survey | 1 |
| cert_task.inserted | 1 |
| cert_task.completed | 1 |
| cert_task.cancelled | 1 |
| task.approved | 1 |
| task.rejected | 1 |
| sn_appclient.install.scheduled.plugins | 1 |
| sn_vsc.sec.hardening.comparison | 1 |
| pwd.enrollment_reminder.trigger | 1 |
| sn_dependentclient.check.dependent_apps | 1 |
| task_activity.message | 1 |
| task_activity.appointment | 1 |
| data_cert.cleanup_invalid_cert_element | 1 |
| email_vas_desk | 1 |
| ldap.connection_failed | 1 |
| cmdbdatamanager.task.stale | 1 |
| sidebar.teams.setup.complete | 1 |
| sidebar.teams.setup.failure | 1 |
| sn_appauthor.check.config.update | 1 |
| csdm.tso.modified | 1 |
| fm.ci_ratecard.review | 1 |
| proactive.monitoring | 1 |
