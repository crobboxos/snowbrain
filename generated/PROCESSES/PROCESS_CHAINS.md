# Process Chains

## Executive Narrative
Dependency concentration highlights where change carries outsized blast radius risk.

## Highest Outbound Dependency Sources
| Source | Downstream Edge Count |
| --- | --- |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | 18 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | 14 |
| script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d) | 12 |
| scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282) | 12 |
| business_rule:Cascade delete records(05712f9277352110b15a31cd6b5a998a) | 11 |
| scheduled_script:Migrate homepages(353a54c647a032107a684bdb736d437d) | 11 |
| script_include:AgentScheduleAjax(0328a950c37312001c845cb981d3ae5c) | 10 |
| ui_action:Unload Dashboard (for Dev)(10278db24f02311054a65e8330ce0bd5) | 10 |
| script_include:ProminFindingsDefUtilSNC(001df27a43d40210a829bf5ff7b8f267) | 9 |
| script_include:WorkflowApprovalUtils(0360b36d0a0a0b260a89dfec60c339c4) | 9 |
| script_include:GenAIProviderUtil(0624dc3affe4b210a3aeffffffffffe8) | 9 |
| script_include:GeneralWOForm(08f481067f231200068712f44efa919d) | 9 |
| script_include:AWAStatsUtils(0c13aac253320010a0bdddeeff7b1229) | 9 |
| script_include:VCenterSensor(1437f6d8c3603000ed4860eb5bba8fad) | 9 |
| script_include:TestExecutorAjax(0380e2605b2212006f23efe5f0f91abd) | 8 |
| script_include:ProminUtils(078d0838536500109e9eddeeff7b128b) | 8 |
| script_include:FSMMobileUtil(1553fea4235123002ff2cb0a56bf65a3) | 8 |
| scheduled_script:Calculate asset uptime(15a1ba431b9ba8903c0ffc4e0d4bcb3a) | 8 |
| scheduled_script:Calculate asset uptime (UHL)(6f6111381bbdf09018ba748bd34bcbfe) | 8 |
| script_include:CPIARUtils(02cd16d3eb0b01102b57e530695228e3) | 7 |
| script_include:SOWChangeUtilsSNC(02e123a553615110532cddeeff7b129e) | 7 |
| script_include:SCComparisonUtil(046c1a8653301110dd8eddeeff7b126e) | 7 |
| script_include:WFStageSet(06b405e91b010100adca1e094f07132f) | 7 |
| script_include:MobilePushNotificationHelper(09cee175531130103296ddeeff7b1234) | 7 |
| scheduled_script:CSDM Data Sync(3903094e5362101061b7ddeeff7b12be) | 7 |
| scheduled_script:Save and Manage CSM Trend Data(3eaa1a50dbe85050b40c355c68961969) | 7 |
| business_rule:sc_task_events(037d66e0c0a801020161091ecbd08f41) | 6 |
| business_rule:Password Reset Property Validation(06a6c0b2eb2001006a668c505206fe63) | 6 |
| business_rule:Cascade Delete - UX Page Metadata(0d1a8bc3b702211068a694e0be11a9e9) | 6 |
| business_rule:SNC Release Complete(0dfa51c30a0a0a0a007e942f5e62d3c9) | 6 |
| script_include:ManageSkillsUtils(0946b5a987fb51101bf7a64d0ebb35bd) | 6 |
| script_include:pwdEnrollmentReminderHelper(0c7c54b00b06030031a567bff6673ac0) | 6 |
| script_include:ATFClientUtil(126e1b9d0f77230091d0f00c97767ef3) | 6 |
| scheduled_script:Schedule master asset list reports(6f2ad5be1b2e50d0ee26dd39cd4bcb06) | 6 |
| script_include:ScheduledInstallService(000b82eb93312010ebd4f157b67ffb86) | 5 |
| script_include:CustomerPushActionUtils(0aa3df1011f18210f877fb5045d0c4ed) | 5 |
| script_include:McbOpenModalUtil(0ac2f515eb683110bd5afd0052522802) | 5 |
| script_include:ChangeInfoSNC(0b7dcfbca700011003396c94d17901c7) | 5 |
| script_include:ChecklistUtil(0bcbe951c31202004e44dccdf3d3ae2a) | 5 |
| script_include:KBPortalSitemapGeneratorUtil(0bea6d45382a9110f8778af503189ee4) | 5 |
| script_include:SPMUtilsFoundationImpl(0ef1f659b3403300f224a72256a8dc5e) | 5 |
| script_include:cxs_FltrConfig(0fbf18a6d773220034d145bcce6103f3) | 5 |
| script_include:TaskSLA(10d0c7590a0a2c394e2b1766a6e5fbad) | 5 |
| script_include:NotificationUnsubscribe(11d170917f0312005f58108c3ffa9118) | 5 |
| script_include:SOAPMessageGenerator(170a6cb60a0a0b114776fbaee3d46612) | 5 |
| ui_action:Run Again (Debug)(246083ea8f783200a5760b5437bdee31) | 5 |
| scheduled_script:Manage duplicated product codes(01ae4e211b6c6090ee26dd39cd4bcb65) | 5 |
| scheduled_script:Service Model Auto Remediation(42aaef8153133010b33bddeeff7b1225) | 5 |
| business_rule:Service Push Notification Subscriptions(005a98d2d7111200a9addd173e24d4b0) | 4 |
| business_rule:Change Phase Events(0f0ca5fec61122780019d6886ee2e0ef) | 4 |

## Highest Inbound Dependency Targets
| Target | Inbound Edge Count |
| --- | --- |
| table:sys_user | 25 |
| table:sys_dictionary | 23 |
| table:sys_user_grmember | 13 |
| table:sys_db_object | 13 |
| table:sys_attachment | 12 |
| table:sys_trigger | 10 |
| table:sys_properties | 9 |
| table:sys_user_has_role | 8 |
| table:wm_task | 8 |
| table:sys_scope | 7 |
| table:sysauto_script | 7 |
| table:customer_account | 7 |
| table:cmn_location | 6 |
| table:cmdb_ci | 6 |
| table:sm_part_requirement | 6 |
| table:sys_choice | 6 |
| table:cmdb_model | 6 |
| table:sysevent_email_action | 5 |
| table:sys_user_role | 5 |
| table:change_request | 5 |
| table:sys_store_app | 5 |
| script_include:DeleteRecordAjax | 5 |
| table:cmn_notif_device | 4 |
| table:sys_update_set | 4 |
| table:sys_update_xml | 4 |
| table:sys_atf_test | 4 |
| table:sys_update_version | 4 |
| table:sysapproval_approver | 4 |
| table:ast_contract | 4 |
| table:sys_user_preference | 4 |
| table:sm_config | 4 |
| table:pa_indicators | 4 |
| table:cmdb_rel_ci | 4 |
| table:sys_email | 4 |
| table:cxs_res_context_config | 4 |
| table:sys_user_group | 4 |
| table:sys_atf_test_result_item | 4 |
| table:ecc_agent | 4 |
| table:wm_order | 4 |
| table:task_sla | 4 |
| script_include:SMAJAX | 4 |
| table:sys_flow_context | 4 |
| table:sn_customerservice_case | 4 |
| table:alm_hardware | 4 |
| table:sysauto_report | 4 |
| table:cmn_notif_message | 3 |
| table:live_group_profile | 3 |
| table:chg_model | 3 |
| table:cmn_schedule | 3 |
| table:sys_filter_option_dynamic | 3 |

## Full Dependency Register
| Source | Target | Evidence | Artifact Sys ID |
| --- | --- | --- | --- |
| business_rule:Validate duplicate search source(0021984a533030101dcdddeeff7b12e4) | table:ais_search_profile_ais_search_source_m2m | new GlideRecord('ais_search_profile_ais_search_source_m2m') | 0021984a533030101dcdddeeff7b12e4 |
| business_rule:Clear Alias Override(005197ab4f930110f545a80652ce0bea) | table:sys_data_source | new GlideRecord('sys_data_source') | 005197ab4f930110f545a80652ce0bea |
| business_rule:Service Push Notification Subscriptions(005a98d2d7111200a9addd173e24d4b0) | table:sys_package | new GlideRecord("sys_package") | 005a98d2d7111200a9addd173e24d4b0 |
| business_rule:Service Push Notification Subscriptions(005a98d2d7111200a9addd173e24d4b0) | table:sysevent_email_action | new GlideRecord("sysevent_email_action") | 005a98d2d7111200a9addd173e24d4b0 |
| business_rule:Service Push Notification Subscriptions(005a98d2d7111200a9addd173e24d4b0) | table:cmn_notif_message | new GlideRecord("cmn_notif_message") | 005a98d2d7111200a9addd173e24d4b0 |
| business_rule:Service Push Notification Subscriptions(005a98d2d7111200a9addd173e24d4b0) | table:cmn_notif_device | new GlideRecord('cmn_notif_device') | 005a98d2d7111200a9addd173e24d4b0 |
| business_rule:Update Consumable Swaps(008125411b7891105eeb7ea5464bcbdd) | table:sys_user | new GlideRecord('sys_user') | 008125411b7891105eeb7ea5464bcbdd |
| business_rule:Parent Bumper(00f8c005c611227600860dabe3db3393) | table:sc_cat_item_delivery_task | new GlideRecord('sc_cat_item_delivery_task') | 00f8c005c611227600860dabe3db3393 |
| business_rule:Maintain order when step made inactive(0109da6573ed3300abdeedcc5ef6a730) | table:sys_embedded_tour_step | new GlideRecord('sys_embedded_tour_step') | 0109da6573ed3300abdeedcc5ef6a730 |
| business_rule:Create default level upon type creation(0110818a770000100f7a72f9691061bf) | table:cmn_skill_level | new GlideRecord('cmn_skill_level') | 0110818a770000100f7a72f9691061bf |
| business_rule:Generate parallelism Orchestrator action(01214f8643f33110adb4e3d3dab8f265) | table:sysevent_queue | new GlideRecord('sysevent_queue') | 01214f8643f33110adb4e3d3dab8f265 |
| business_rule:Generate parallelism Orchestrator action(01214f8643f33110adb4e3d3dab8f265) | table:sys_orchestrator_action | new GlideRecord('sys_orchestrator_action') | 01214f8643f33110adb4e3d3dab8f265 |
| business_rule:Live Agent Topic Should be Visible(0139bbb35b622010ca256ada1d81c745) | table:sys_cs_topic | new GlideRecord("sys_cs_topic") | 0139bbb35b622010ca256ada1d81c745 |
| business_rule:Notify Subscribed Users(014989b6d701120023c84f80de6103e3) | table:sqanda_subscribe | new GlideRecord("sqanda_subscribe") | 014989b6d701120023c84f80de6103e3 |
| business_rule:Role Delegation Functions(0149c9930a0a0b300041ce2777564999) | table:sys_user_role | new GlideRecord("sys_user_role") | 0149c9930a0a0b300041ce2777564999 |
| business_rule:Role Delegation Functions(0149c9930a0a0b300041ce2777564999) | table:sys_user_has_role | new GlideRecord("sys_user_has_role") | 0149c9930a0a0b300041ce2777564999 |
| business_rule:Role Delegation Functions(0149c9930a0a0b300041ce2777564999) | table:sys_user_grmember | new GlideRecord('sys_user_grmember') | 0149c9930a0a0b300041ce2777564999 |
| business_rule:Check scope in solution name(01d4473353e33300d1dcddeeff7b122d) | table:ml_capability_definition_base | new GlideRecord('ml_capability_definition_base') | 01d4473353e33300d1dcddeeff7b122d |
| business_rule:Set intent name same as primary(0206c9c3eb0220105de665fcc8522801) | table:sys_nlu_intent | new GlideRecord("sys_nlu_intent") | 0206c9c3eb0220105de665fcc8522801 |
| business_rule:Auto dispatch if wo task has appointment(0262406ad7e33200811300285e610363) | table:wm_task | new GlideRecord("wm_task") | 0262406ad7e33200811300285e610363 |
| business_rule:Check related records on update(02ae591093010200c5fa372e457ffbf7) | table:sys_ui_hp_group | new GlideRecord("sys_ui_hp_group") | 02ae591093010200c5fa372e457ffbf7 |
| business_rule:Check related records on update(02ae591093010200c5fa372e457ffbf7) | table:sys_ui_hp_reference | new GlideRecord("sys_ui_hp_reference") | 02ae591093010200c5fa372e457ffbf7 |
| business_rule:Polaris follow event queue(02af2d1f77aa1110866ea2059f5a99c8) | table:live_group_profile | new GlideRecord('live_group_profile') | 02af2d1f77aa1110866ea2059f5a99c8 |
| business_rule:Polaris follow event queue(02af2d1f77aa1110866ea2059f5a99c8) | event:polaris.follow.update | gs.eventQueue("polaris.follow.update" | 02af2d1f77aa1110866ea2059f5a99c8 |
| business_rule:Initial State: Reassign on delete(02e041195323101034d1ddeeff7b1240) | table:sttrm_state | new GlideRecord("sttrm_state") | 02e041195323101034d1ddeeff7b1240 |
| business_rule:Delete update set after push back out(0312853397212100a61d10aa1c297567) | table:sys_update_set | new GlideRecord("sys_update_set") | 0312853397212100a61d10aa1c297567 |
| business_rule:Calculate full address(034195f21b1dcc50ea17dd3fbd4bcb3f) | table:cmn_location | new GlideRecord("cmn_location") | 034195f21b1dcc50ea17dd3fbd4bcb3f |
| business_rule:Close skip previous tasks(034e053014ac3300964f04747c5954f2) | table:alm_transfer_order_line_task | new GlideRecord('alm_transfer_order_line_task') | 034e053014ac3300964f04747c5954f2 |
| business_rule:Unset default all other models(03598278c3406010cc343f52c1d3aea9) | table:chg_model | new GlideRecord("chg_model") | 03598278c3406010cc343f52c1d3aea9 |
| business_rule:delete orphan multi row question answers(036ed6560b2310106b80482393673a65) | event:sc_cart_item.multi_row.orphan.delete | gs.eventQueue('sc_cart_item.multi_row.orphan.delete' | 036ed6560b2310106b80482393673a65 |
| business_rule:sc_task_events(037d66e0c0a801020161091ecbd08f41) | event:sc_task.commented | gs.eventQueue("sc_task.commented" | 037d66e0c0a801020161091ecbd08f41 |
| business_rule:sc_task_events(037d66e0c0a801020161091ecbd08f41) | event:sc_task.worknoted | gs.eventQueue("sc_task.worknoted" | 037d66e0c0a801020161091ecbd08f41 |
| business_rule:sc_task_events(037d66e0c0a801020161091ecbd08f41) | event:sc_task.updated | gs.eventQueue("sc_task.updated" | 037d66e0c0a801020161091ecbd08f41 |
| business_rule:sc_task_events(037d66e0c0a801020161091ecbd08f41) | event:sc_task.state.changed | gs.eventQueue("sc_task.state.changed" | 037d66e0c0a801020161091ecbd08f41 |
| business_rule:sc_task_events(037d66e0c0a801020161091ecbd08f41) | event:sc_task.assigned.to.user | gs.eventQueue("sc_task.assigned.to.user" | 037d66e0c0a801020161091ecbd08f41 |
| business_rule:sc_task_events(037d66e0c0a801020161091ecbd08f41) | event:sc_task.assigned.to.group | gs.eventQueue("sc_task.assigned.to.group" | 037d66e0c0a801020161091ecbd08f41 |
| business_rule:Appointment Booking is Cancelled(03c2b7f25bf28010f22b6e533381c745) | event:sn_apptmnt_booking.cancelled | gs.eventQueue('sn_apptmnt_booking.cancelled' | 03c2b7f25bf28010f22b6e533381c745 |
| business_rule:Insert Order(03d689b273322300a9fa795a4cf6a741) | table:sys_aw_my_list | new GlideRecord('sys_aw_my_list') | 03d689b273322300a9fa795a4cf6a741 |
| business_rule:Delete Dictionary(03fbbea35b730110cc35c0d42d81c7e0) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 03fbbea35b730110cc35c0d42d81c7e0 |
| business_rule:getGroupMembersM2M(041646cb0a4700d0016ac02258c25645) | table:sys_user_grmember | new GlideRecord('sys_user_grmember') | 041646cb0a4700d0016ac02258c25645 |
| business_rule:Prevent dup key and key table records(044afcea537220103738ddeeff7b12d5) | table:sys_sg_custom_map_provider | new GlideRecord("sys_sg_custom_map_provider") | 044afcea537220103738ddeeff7b12d5 |
| business_rule:Remove member from live group(04643f829f101200fc55b73f957fcf8d) | table:live_group_profile | new GlideRecord("live_group_profile") | 04643f829f101200fc55b73f957fcf8d |
| business_rule:Remove member from live group(04643f829f101200fc55b73f957fcf8d) | table:live_group_member | new GlideRecord("live_group_member") | 04643f829f101200fc55b73f957fcf8d |
| business_rule:Create outbound Interaction(047c36a21b40d610bb2786a3604bcbe6) | table:sys_user | new GlideRecord("sys_user") | 047c36a21b40d610bb2786a3604bcbe6 |
| business_rule:Flush probe cache(0492c67053d4320023bdae4a16dc3439) | table:discovery_probe_results_cache | new GlideRecord("discovery_probe_results_cache") | 0492c67053d4320023bdae4a16dc3439 |
| business_rule:Avoid Duplicate Entry(04c124d6536b00103a2eddeeff7b121a) | table:sn_prod_cat_rel_m2m_product_catalog_item | new GlideRecord('sn_prod_cat_rel_m2m_product_catalog_item') | 04c124d6536b00103a2eddeeff7b121a |
| business_rule:Prevent application inconsistency(04ec6e23d7222100600949d48e6103e6) | table:sys_update_xml | new GlideRecord('sys_update_xml') | 04ec6e23d7222100600949d48e6103e6 |
| business_rule:Update TimeZone on Personal Schedule(04f1a234c3a83200467f10c422d3aef5) | table:cmn_schedule | new GlideRecord("cmn_schedule") | 04f1a234c3a83200467f10c422d3aef5 |
| business_rule:Sync default value(054585c85f220100a9ad2572f2b47713) | table:sys_filter_option_dynamic | new GlideRecord('sys_filter_option_dynamic') | 054585c85f220100a9ad2572f2b47713 |
| business_rule:Reorder test parameter sets order(0552e6b4532313008cd9ddeeff7b125d) | table:sys_atf_test | new GlideRecord("sys_atf_test") | 0552e6b4532313008cd9ddeeff7b125d |
| business_rule:Sync csm_consumer_user  to  consumer(0557fcdbc303120071d07bfaa2d3ae29) | table:csm_consumer | new GlideRecord('csm_consumer') | 0557fcdbc303120071d07bfaa2d3ae29 |
| business_rule:Cascade delete records(05712f9277352110b15a31cd6b5a998a) | table:sys_ih_external_trigger_definition | new GlideRecord("sys_ih_external_trigger_definition") | 05712f9277352110b15a31cd6b5a998a |
| business_rule:Cascade delete records(05712f9277352110b15a31cd6b5a998a) | table:sys_api_operation | new GlideRecord("sys_api_operation") | 05712f9277352110b15a31cd6b5a998a |
| business_rule:Cascade delete records(05712f9277352110b15a31cd6b5a998a) | table:sys_api_collection | new GlideRecord("sys_api_collection") | 05712f9277352110b15a31cd6b5a998a |
| business_rule:Cascade delete records(05712f9277352110b15a31cd6b5a998a) | table:sys_api_access_policy | new GlideRecord("sys_api_access_policy") | 05712f9277352110b15a31cd6b5a998a |
| business_rule:Cascade delete records(05712f9277352110b15a31cd6b5a998a) | table:sys_auth_profile_mapping | new GlideRecord("sys_auth_profile_mapping") | 05712f9277352110b15a31cd6b5a998a |
| business_rule:Cascade delete records(05712f9277352110b15a31cd6b5a998a) | table:inbound_auth_profile | new GlideRecord("inbound_auth_profile") | 05712f9277352110b15a31cd6b5a998a |
| business_rule:Cascade delete records(05712f9277352110b15a31cd6b5a998a) | table:http_key_auth | new GlideRecord("http_key_auth") | 05712f9277352110b15a31cd6b5a998a |
| business_rule:Cascade delete records(05712f9277352110b15a31cd6b5a998a) | table:sys_token_auth_parameter | new GlideRecord("sys_token_auth_parameter") | 05712f9277352110b15a31cd6b5a998a |
| business_rule:Cascade delete records(05712f9277352110b15a31cd6b5a998a) | table:http_hmac_auth | new GlideRecord("http_hmac_auth") | 05712f9277352110b15a31cd6b5a998a |
| business_rule:Cascade delete records(05712f9277352110b15a31cd6b5a998a) | table:hmac_config | new GlideRecord("hmac_config") | 05712f9277352110b15a31cd6b5a998a |
| business_rule:Cascade delete records(05712f9277352110b15a31cd6b5a998a) | table:token_auth_credential | new GlideRecord("token_auth_credential") | 05712f9277352110b15a31cd6b5a998a |
| business_rule:Uniqueness check for RDN and Filter(05ed5e2f9ff582105760e6073b0a1c40) | table:ldap_ou_config | new GlideRecord("ldap_ou_config") | 05ed5e2f9ff582105760e6073b0a1c40 |
| business_rule:Prevent EFC Activation on Inactive Field(05f3bf59c3b94210e5055b12b940dd71) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 05f3bf59c3b94210e5055b12b940dd71 |
| business_rule:Group Manager Change(0672c9970a0a0bad01d7ddbff9d08d1f) | table:sys_user_role | new GlideRecord("sys_user_role") | 0672c9970a0a0bad01d7ddbff9d08d1f |
| business_rule:Group Manager Change(0672c9970a0a0bad01d7ddbff9d08d1f) | table:sys_user_has_role | GlideRecord("sys_user_has_role") | 0672c9970a0a0bad01d7ddbff9d08d1f |
| business_rule:Group Manager Change(0672c9970a0a0bad01d7ddbff9d08d1f) | table:sys_user_has_role | new GlideRecord("sys_user_has_role") | 0672c9970a0a0bad01d7ddbff9d08d1f |
| business_rule:Set active field in ts_index_group(068804f653132300d0baddeeff7b123b) | table:ts_index_group | new GlideRecord('ts_index_group') | 068804f653132300d0baddeeff7b123b |
| business_rule:Password Reset Property Validation(06a6c0b2eb2001006a668c505206fe63) | table:pwd_verification_param | new GlideRecord('pwd_verification_param') | 06a6c0b2eb2001006a668c505206fe63 |
| business_rule:Password Reset Property Validation(06a6c0b2eb2001006a668c505206fe63) | table:pwd_verification | new GlideRecord('pwd_verification') | 06a6c0b2eb2001006a668c505206fe63 |
| business_rule:Password Reset Property Validation(06a6c0b2eb2001006a668c505206fe63) | table:pwd_verification_type | new GlideRecord('pwd_verification_type') | 06a6c0b2eb2001006a668c505206fe63 |
| business_rule:Password Reset Property Validation(06a6c0b2eb2001006a668c505206fe63) | table:sys_properties | new GlideRecord('sys_properties') | 06a6c0b2eb2001006a668c505206fe63 |
| business_rule:Password Reset Property Validation(06a6c0b2eb2001006a668c505206fe63) | table:pwd_activity_monitor | new GlideRecord('pwd_activity_monitor') | 06a6c0b2eb2001006a668c505206fe63 |
| business_rule:Password Reset Property Validation(06a6c0b2eb2001006a668c505206fe63) | table:sysevent_email_template | new GlideRecord('sysevent_email_template') | 06a6c0b2eb2001006a668c505206fe63 |
| business_rule:Source Instance Validate(06c33c50371120004f6a80f7bcbe5d80) | table:instance | new GlideRecord("instance") | 06c33c50371120004f6a80f7bcbe5d80 |
| business_rule:Sync dynamic default value on display(06e096a45f220100a9ad2572f2b47760) | table:sys_filter_option_dynamic | new GlideRecord("sys_filter_option_dynamic") | 06e096a45f220100a9ad2572f2b47760 |
| business_rule:Synch user language(06ea0e7bb7232110a3cd911cde11a958) | table:sys_user | new GlideRecord('sys_user') | 06ea0e7bb7232110a3cd911cde11a958 |
| business_rule:Check only one default(072bef188f03110040f82ab2f0f923dc) | table:asmt_bubble_chart | new GlideRecord("asmt_bubble_chart") | 072bef188f03110040f82ab2f0f923dc |
| business_rule:Email Interaction record updated(0747fa53831a12102e3a23e4822bc051) | table:interaction_context | new GlideRecord("interaction_context") | 0747fa53831a12102e3a23e4822bc051 |
| business_rule:Email Interaction record updated(0747fa53831a12102e3a23e4822bc051) | table:sys_user | new GlideRecord("sys_user") | 0747fa53831a12102e3a23e4822bc051 |
| business_rule:Add members to live group(076f62c1d70331002ae9602b6e610311) | table:live_group_profile | new GlideRecord("live_group_profile") | 076f62c1d70331002ae9602b6e610311 |
| business_rule:Prevent duplicate active per table(0770d05b7f1313007f005212bdfa91db) | table:sys_email_client_configuration | new GlideRecord('sys_email_client_configuration') | 0770d05b7f1313007f005212bdfa91db |
| business_rule:Validate CI class hierarchy(0786218d5bd10110693e7da52d81c72f) | table:sn_cmdb_ws_ms_class_metadata | new GlideRecord('sn_cmdb_ws_ms_class_metadata') | 0786218d5bd10110693e7da52d81c72f |
| business_rule:Validate Table Creation(078b26200a0a0b24008811ca72aeb0b9) | table:sys_dictionary | new GlideRecord("sys_dictionary") | 078b26200a0a0b24008811ca72aeb0b9 |
| business_rule:Validate Table Creation(078b26200a0a0b24008811ca72aeb0b9) | table:v_field_creator | new GlideRecord("v_field_creator") | 078b26200a0a0b24008811ca72aeb0b9 |
| business_rule:Create TemplateDetails Record(079502400f2310108c9c5019c4767e10) | table:sys_app_template_detail | new GlideRecord('sys_app_template_detail') | 079502400f2310108c9c5019c4767e10 |
| business_rule:Mobile - Alert Mappings Variable Change(07ad6712eb5011105220a2d4285228f5) | table:sys_sg_write_back_action_item | new GlideRecord("sys_sg_write_back_action_item") | 07ad6712eb5011105220a2d4285228f5 |
| business_rule:Duplicate Run Level Mapping Check(07ae7934b78320104c75ccf78e11a98e) | table:sys_run_level_op_toggle_m2m | new GlideRecord('sys_run_level_op_toggle_m2m') | 07ae7934b78320104c75ccf78e11a98e |
| business_rule:Recalculate availability on update(07f746be90118610f877eafe577206bc) | event:spm.availability.calculate | gs.eventQueue('spm.availability.calculate' | 07f746be90118610f877eafe577206bc |
| business_rule:delete report_stats_execution on delete(0808f00bd7211200bd4a4ebfae61035d) | table:report_stats_executions | new GlideRecord('report_stats_executions') | 0808f00bd7211200bd4a4ebfae61035d |
| business_rule:delete report_stats_execution on delete(0808f00bd7211200bd4a4ebfae61035d) | table:report_executions | new GlideRecord('report_executions') | 0808f00bd7211200bd4a4ebfae61035d |
| business_rule:Provision queue Orchestrator action(0814a03c43d77110adb4e3d3dab8f2c6) | table:sysevent_queue | new GlideRecord('sysevent_queue') | 0814a03c43d77110adb4e3d3dab8f2c6 |
| business_rule:Create m2m_kb_task record(08273a2fb750001016e908a9ee11a9d3) | table:m2m_kb_task | new GlideRecord("m2m_kb_task") | 08273a2fb750001016e908a9ee11a9d3 |
| business_rule:Survey recipients list types(085318c787131300fa0166d107cb0b78) | table:asmt_m2m_recipientslist_survey | new GlideRecord('asmt_m2m_recipientslist_survey') | 085318c787131300fa0166d107cb0b78 |
| business_rule:Validate duplicate Language mapping(0887a72f73032300c62441244ef6a701) | table:translator_mapping | new GlideRecord('translator_mapping') | 0887a72f73032300c62441244ef6a701 |
| business_rule:Prevent Duplicate Test Parameter Names(08c0dd16a7131300cf2daae21879013e) | table:sys_atf_parameter_set | new GlideRecord('sys_atf_parameter_set') | 08c0dd16a7131300cf2daae21879013e |
| business_rule:Check unique target context pair(08cc9a68736700109234c346c4f6a77e) | table:sn_customercentral_cust_info_config | new GlideRecord('sn_customercentral_cust_info_config') | 08cc9a68736700109234c346c4f6a77e |
| business_rule:Send notification when assigned to group(08e6b1ba4fc22600bb5e89bf0210c7fa) | event:wo.task.assigned.to.group | gs.eventQueue('wo.task.assigned.to.group' | 08e6b1ba4fc22600bb5e89bf0210c7fa |
| business_rule:Handle updates moving between sets(0914e5b9ef001100a61d5a3615c0fb4e) | table:sys_update_set | new GlideRecord('sys_update_set') | 0914e5b9ef001100a61d5a3615c0fb4e |
| business_rule:Handle updates moving between sets(0914e5b9ef001100a61d5a3615c0fb4e) | table:sys_update_version | new GlideRecord('sys_update_version') | 0914e5b9ef001100a61d5a3615c0fb4e |
| business_rule:Approval Publication(092a735ac30112004bd67bfaa2d3ae19) | table:sn_publications_publication | new GlideRecord('sn_publications_publication') | 092a735ac30112004bd67bfaa2d3ae19 |
| business_rule:Web Service Access Only for MID Role(0952d4e8ff202210cd8affffffffff11) | table:sys_user | new GlideRecord('sys_user') | 0952d4e8ff202210cd8affffffffff11 |
| business_rule:Web Service Access Only for MID Role(0952d4e8ff202210cd8affffffffff11) | table:sys_user_role | new GlideRecord('sys_user_role') | 0952d4e8ff202210cd8affffffffff11 |
| business_rule:Web Service Access Only for MID Role(0952d4e8ff202210cd8affffffffff11) | table:sys_user_has_role | new GlideRecord('sys_user_has_role') | 0952d4e8ff202210cd8affffffffff11 |
| business_rule:Set Variable Display Name Field(09591c8d0a0006d401e8e00feb665679) | table:expert_variable | new GlideRecord("expert_variable") | 09591c8d0a0006d401e8e00feb665679 |
| business_rule:Enforce one policy per table(095f778beb3371100dba9147c15228f4) | table:sys_dm_policy | new GlideRecord('sys_dm_policy') | 095f778beb3371100dba9147c15228f4 |
| business_rule:Update Checklist(0985c8fe0f01330005113694ba767ec7) | table:checklist | new GlideRecord('checklist') | 0985c8fe0f01330005113694ba767ec7 |
| business_rule:Add Approver If Process Guide running(09a01cc10a0a0b06004eca96095dc87f) | table:state_binding | new GlideRecord('state_binding') | 09a01cc10a0a0b06004eca96095dc87f |
| business_rule:Add Approver If Process Guide running(09a01cc10a0a0b06004eca96095dc87f) | table:sysapproval_approver | new GlideRecord('sysapproval_approver') | 09a01cc10a0a0b06004eca96095dc87f |
| business_rule:Set Interaction Context(09b88b90431c921050286548b9b8f2fb) | table:sys_pd_context | new GlideRecordSecure('sys_pd_context') | 09b88b90431c921050286548b9b8f2fb |
| business_rule:Affected ci notifications(09fa6af10a0a0b1d00c6605ebe45bc26) | event:ci.notification.for.task | gs.eventQueue('ci.notification.for.task' | 09fa6af10a0a0b1d00c6605ebe45bc26 |
| business_rule:Add Default Verification To Process(0a07c3c3f5bbb410f877a38b203bb984) | table:pwd_map_proc_to_verification | new GlideRecord('pwd_map_proc_to_verification') | 0a07c3c3f5bbb410f877a38b203bb984 |
| business_rule:REST Method: Check Variables(0a14a3165333020048ae0f0c36dc3479) | table:sys_rest_message | new GlideRecord('sys_rest_message') | 0a14a3165333020048ae0f0c36dc3479 |
| business_rule:Reset participant fields on table change(0a3e40eab7c30010e15bf597ee11a91b) | table:sn_doc_participant | new GlideRecord('sn_doc_participant') | 0a3e40eab7c30010e15bf597ee11a91b |
| business_rule:Delete Attached nodes if invalid(0a43d121779a211006331b56ba5a9933) | table:promin_activity_def | new GlideRecord('promin_activity_def') | 0a43d121779a211006331b56ba5a9933 |
| business_rule:Adjust MFA Enforcement Banner EndDate(0a6715e57f201210114d91fadc86655e) | table:sys_ux_banner_announcement | new GlideRecord('sys_ux_banner_announcement') | 0a6715e57f201210114d91fadc86655e |
| business_rule:Show msg if content is source of a cont.(0a6cb2fac7432010ec17148c95c26016) | table:sn_doc_template_block_content | new GlideRecord('sn_doc_template_block_content') | 0a6cb2fac7432010ec17148c95c26016 |
| business_rule:Affected group notifications(0a6ea4aa0a0a0b1d006b92f265683131) | table:task_group | new GlideRecord('task_group') | 0a6ea4aa0a0a0b1d006b92f265683131 |
| business_rule:Affected group notifications(0a6ea4aa0a0a0b1d006b92f265683131) | event:group.affected | gs.eventQueue('group.affected' | 0a6ea4aa0a0a0b1d006b92f265683131 |
| business_rule:Affected location notifications(0a7daca70a0a0b1d00b156b6b953267b) | table:task_location | new GlideRecord('task_location') | 0a7daca70a0a0b1d00b156b6b953267b |
| business_rule:Affected location notifications(0a7daca70a0a0b1d00b156b6b953267b) | event:location.affected | gs.eventQueue('location.affected' | 0a7daca70a0a0b1d00b156b6b953267b |
| business_rule:Update VTB Card-Labels Count On Insert(0aa0c4207370330000282dc2c4f6a7cb) | table:vtb_card | new GlideRecord("vtb_card") | 0aa0c4207370330000282dc2c4f6a7cb |
| business_rule:Update Contract Lifetime Cost(0ad77d1647e0300042bd757f2ede278b) | table:fm_expense_line | new GlideRecord('fm_expense_line') | 0ad77d1647e0300042bd757f2ede278b |
| business_rule:Update Contract Lifetime Cost(0ad77d1647e0300042bd757f2ede278b) | table:ast_contract | new GlideRecord('ast_contract') | 0ad77d1647e0300042bd757f2ede278b |
| business_rule:Check duplicate for responsibility(0b49a2f1c3021200e94a9f2974d3aef0) | table:sn_customerservice_contact_relationship | new GlideRecord("sn_customerservice_contact_relationship") | 0b49a2f1c3021200e94a9f2974d3aef0 |
| business_rule:Delete m2m_kb_task record on remove(0b53a522ef22210066fc36caa5c0fb4f) | table:m2m_kb_task | new GlideRecord('m2m_kb_task') | 0b53a522ef22210066fc36caa5c0fb4f |
| business_rule:Able to disable parameterized testing(0b6d2974530313008cd9ddeeff7b12b2) | table:sys_atf_parameter_set | new GlideRecord('sys_atf_parameter_set') | 0b6d2974530313008cd9ddeeff7b12b2 |
| business_rule:Delete bi_direction relationship(0b93cb16c33202003a657bfaa2d3aef4) | table:account_relationship | new GlideRecord('account_relationship') | 0b93cb16c33202003a657bfaa2d3aef4 |
| business_rule:Sync Reference Qual(0bb57d5e4733110005c7d8966c9a71fc) | table:sys_filter_option_dynamic | new GlideRecord("sys_filter_option_dynamic") | 0bb57d5e4733110005c7d8966c9a71fc |
| business_rule:Prevent duplicate relation types(0bcd3b62eb2012007c94efc9a206fe8a) | table:cmdb_rel_type | new GlideRecord('cmdb_rel_type') | 0bcd3b62eb2012007c94efc9a206fe8a |
| business_rule:Delete MID Server File Attachments(0bdabb37a0154610f877aa583ca3fb17) | table:sys_attachment | new GlideRecord('sys_attachment') | 0bdabb37a0154610f877aa583ca3fb17 |
| business_rule:Delete sys_hub_pill_compound records(0c0634410fa33300b599bca2ff767e82) | table:sys_hub_pill_compound | new GlideRecord("sys_hub_pill_compound") | 0c0634410fa33300b599bca2ff767e82 |
| business_rule:Validate Delete Data Class(0c1e04c8436131105f6b55560bb8f239) | table:dp_configuration | new GlideRecord('dp_configuration') | 0c1e04c8436131105f6b55560bb8f239 |
| business_rule:Flag terms and conditions(0c2c7e2737a43000158bbfc8bcbe5d62) | table:clm_terms_and_conditions | new GlideRecord('clm_terms_and_conditions') | 0c2c7e2737a43000158bbfc8bcbe5d62 |
| business_rule:clear preferences(0c45b215c7100010ed6cdd34f2c260be) | table:pa_m2m_dashboard_sources | new GlideRecord('pa_m2m_dashboard_sources') | 0c45b215c7100010ed6cdd34f2c260be |
| business_rule:clear preferences(0c45b215c7100010ed6cdd34f2c260be) | table:sys_user_preference | new GlideRecord('sys_user_preference') | 0c45b215c7100010ed6cdd34f2c260be |
| business_rule:Populate model component field(0cb58be153213110b52fddeeff7b1209) | table:alm_asset | new GlideRecord('alm_asset') | 0cb58be153213110b52fddeeff7b1209 |
| business_rule:Populate model component field(0cb58be153213110b52fddeeff7b1209) | table:cmdb_m2m_model_component | new GlideRecord('cmdb_m2m_model_component') | 0cb58be153213110b52fddeeff7b1209 |
| business_rule:Set Project status based on permission(0cb701eca350311011ecb18c26fcda7b) | table:promin_project | new GlideRecord("promin_project") | 0cb701eca350311011ecb18c26fcda7b |
| business_rule:Flush TableDescriptor cache(0cd044af43401210b39307dcc4b8f26a) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 0cd044af43401210b39307dcc4b8f26a |
| business_rule:Social QA accepts an answer(0d038355c3033100bde4beae82d3ae81) | table:kb_social_qa_question | new GlideRecord('kb_social_qa_question') | 0d038355c3033100bde4beae82d3ae81 |
| business_rule:Social QA accepts an answer(0d038355c3033100bde4beae82d3ae81) | table:kb_social_qa_answer | new GlideRecord('kb_social_qa_answer') | 0d038355c3033100bde4beae82d3ae81 |
| business_rule:Clean up UIB Metadata on delete(0d116ee80723301051ff3342cfd30025) | table:sys_ux_screen | new GlideRecord('sys_ux_screen') | 0d116ee80723301051ff3342cfd30025 |
| business_rule:Clean up UIB Metadata on delete(0d116ee80723301051ff3342cfd30025) | table:sys_ux_macroponent | new GlideRecord('sys_ux_macroponent') | 0d116ee80723301051ff3342cfd30025 |
| business_rule:Clean up UIB Metadata on delete(0d116ee80723301051ff3342cfd30025) | table:sys_ux_app_route | new GlideRecord('sys_ux_app_route') | 0d116ee80723301051ff3342cfd30025 |
| business_rule:Cascade Delete - UX Page Metadata(0d1a8bc3b702211068a694e0be11a9e9) | table:sys_ux_page_property | new GlideRecord("sys_ux_page_property") | 0d1a8bc3b702211068a694e0be11a9e9 |
| business_rule:Cascade Delete - UX Page Metadata(0d1a8bc3b702211068a694e0be11a9e9) | table:sys_ux_list | new GlideRecord("sys_ux_list") | 0d1a8bc3b702211068a694e0be11a9e9 |
| business_rule:Cascade Delete - UX Page Metadata(0d1a8bc3b702211068a694e0be11a9e9) | table:sys_ux_list_category | new GlideRecord("sys_ux_list_category") | 0d1a8bc3b702211068a694e0be11a9e9 |
| business_rule:Cascade Delete - UX Page Metadata(0d1a8bc3b702211068a694e0be11a9e9) | table:sys_ux_list_menu_config | new GlideRecord("sys_ux_list_menu_config") | 0d1a8bc3b702211068a694e0be11a9e9 |
| business_rule:Cascade Delete - UX Page Metadata(0d1a8bc3b702211068a694e0be11a9e9) | table:sys_ux_applicability_m2m_list | new GlideRecord("sys_ux_applicability_m2m_list") | 0d1a8bc3b702211068a694e0be11a9e9 |
| business_rule:Cascade Delete - UX Page Metadata(0d1a8bc3b702211068a694e0be11a9e9) | table:sys_ux_applicability | new GlideRecord("sys_ux_applicability") | 0d1a8bc3b702211068a694e0be11a9e9 |
| business_rule:Update workflow version(0d2cdba1735103006715b45a4cf6a762) | table:wf_workflow_version | new GlideRecord("wf_workflow_version") | 0d2cdba1735103006715b45a4cf6a762 |
| business_rule:Detect Controller Circular Dependency(0d2e08bf77b01110c9d933c1fa5a99f2) | table:sys_ux_controller | new GlideRecord('sys_ux_controller') | 0d2e08bf77b01110c9d933c1fa5a99f2 |
| business_rule:Prevent Duplicates(0d6578783b0210103f09080044efc4f8) | table:wm_work_type | new GlideRecord('wm_work_type') | 0d6578783b0210103f09080044efc4f8 |
| business_rule:Dispatch Survey Notification Event(0d6981bac7323010e028dc8703c26064) | event:record.send_survey | gs.eventQueue("record.send_survey" | 0d6981bac7323010e028dc8703c26064 |
| business_rule:certification task events(0d7a8304ac100b32720d578f22cb04e5) | event:cert_task.inserted | gs.eventQueue("cert_task.inserted" | 0d7a8304ac100b32720d578f22cb04e5 |
| business_rule:certification task events(0d7a8304ac100b32720d578f22cb04e5) | event:cert_task.completed | gs.eventQueue("cert_task.completed" | 0d7a8304ac100b32720d578f22cb04e5 |
| business_rule:certification task events(0d7a8304ac100b32720d578f22cb04e5) | event:cert_task.cancelled | gs.eventQueue("cert_task.cancelled" | 0d7a8304ac100b32720d578f22cb04e5 |
| business_rule:Update related question record on create(0d805843ff033100fa2effffffffffbf) | table:kb_social_qa_question | new GlideRecord('kb_social_qa_question') | 0d805843ff033100fa2effffffffffbf |
| business_rule:Update last deactivated on(0d84085a4310221026fcb4e2ffb8f244) | table:par_dashboard_user_metadata | new GlideRecordSecure('par_dashboard_user_metadata') | 0d84085a4310221026fcb4e2ffb8f244 |
| business_rule:clean consumer address fields via delete(0d989441c3b0220071d07bfaa2d3ae84) | table:csm_consumer | new GlideRecord("csm_consumer") | 0d989441c3b0220071d07bfaa2d3ae84 |
| business_rule:Update sys_certificate attributes(0daec0920a0a0b6100bd30ccba6e6db5) | table:sys_certificate | new GlideRecord("sys_certificate") | 0daec0920a0a0b6100bd30ccba6e6db5 |
| business_rule:Set product instance for model category(0dbefacac3113110a6b73af3b140dde7) | table:cmdb_model_category | new GlideRecord('cmdb_model_category') | 0dbefacac3113110a6b73af3b140dde7 |
| business_rule:SNC Release Insert Phases(0df9cd1d0a0a0a0a01443628846898c7) | table:release_phase | new GlideRecord('release_phase') | 0df9cd1d0a0a0a0a01443628846898c7 |
| business_rule:SNC Release Delete Phases(0dfa169e0a0a0a0a01bab2a6fae138a9) | table:release_phase | new GlideRecord('release_phase') | 0dfa169e0a0a0a0a01bab2a6fae138a9 |
| business_rule:SNC Release Complete(0dfa51c30a0a0a0a007e942f5e62d3c9) | table:release_feature | new GlideRecord('release_feature') | 0dfa51c30a0a0a0a007e942f5e62d3c9 |
| business_rule:SNC Release Complete(0dfa51c30a0a0a0a007e942f5e62d3c9) | table:change_request | new GlideRecord('change_request') | 0dfa51c30a0a0a0a007e942f5e62d3c9 |
| business_rule:SNC Release Complete(0dfa51c30a0a0a0a007e942f5e62d3c9) | table:problem | new GlideRecord('problem') | 0dfa51c30a0a0a0a007e942f5e62d3c9 |
| business_rule:SNC Release Complete(0dfa51c30a0a0a0a007e942f5e62d3c9) | table:release_cis | new GlideRecord('release_cis') | 0dfa51c30a0a0a0a007e942f5e62d3c9 |
| business_rule:SNC Release Complete(0dfa51c30a0a0a0a007e942f5e62d3c9) | table:cmdb_ci | new GlideRecord('cmdb_ci') | 0dfa51c30a0a0a0a007e942f5e62d3c9 |
| business_rule:SNC Release Complete(0dfa51c30a0a0a0a007e942f5e62d3c9) | table:dsl | new GlideRecord('dsl') | 0dfa51c30a0a0a0a007e942f5e62d3c9 |
| business_rule:Set default values(0e388384d7010200e5eb83e80e6103f2) | table:sm_config | new GlideRecord('sm_config') | 0e388384d7010200e5eb83e80e6103f2 |
| business_rule:Validate unique REST API path for insert(0e524751c381011089a7dd5c2840dd56) | table:sys_api_access_scope | new GlideRecord('sys_api_access_scope') | 0e524751c381011089a7dd5c2840dd56 |
| business_rule:Text Index remove stop word family(0e80c7a3b3331300170ba884c6a8dd48) | table:ts_index_name | new GlideRecord('ts_index_name') | 0e80c7a3b3331300170ba884c6a8dd48 |
| business_rule:Deactivate OE Usage on Parent Capability(0e894dbc7f71121046719fbefc86658f) | table:sys_one_extend_capability_definition | new GlideRecord("sys_one_extend_capability_definition") | 0e894dbc7f71121046719fbefc86658f |
| business_rule:Deactivate OE Usage on Parent Capability(0e894dbc7f71121046719fbefc86658f) | table:sys_one_extend_usage | new GlideRecord("sys_one_extend_usage") | 0e894dbc7f71121046719fbefc86658f |
| business_rule:Delete business service preferences(0ee8ec33f30131002e6bae4716612b37) | table:sa_business_service_user_prefs | new GlideRecord("sa_business_service_user_prefs") | 0ee8ec33f30131002e6bae4716612b37 |
| business_rule:Promoted Topic Limit(0ef808ac53351010a813ddeeff7b1230) | table:sys_cs_context_profile_promotion | new GlideRecord("sys_cs_context_profile_promotion") | 0ef808ac53351010a813ddeeff7b1230 |
| business_rule:Change Phase Events(0f0ca5fec61122780019d6886ee2e0ef) | table:change_request | new GlideRecord('change_request') | 0f0ca5fec61122780019d6886ee2e0ef |
| business_rule:Change Phase Events(0f0ca5fec61122780019d6886ee2e0ef) | table:change_phase | new GlideRecord('change_phase') | 0f0ca5fec61122780019d6886ee2e0ef |
| business_rule:Change Phase Events(0f0ca5fec61122780019d6886ee2e0ef) | event:task.approved | gs.eventQueue("task.approved" | 0f0ca5fec61122780019d6886ee2e0ef |
| business_rule:Change Phase Events(0f0ca5fec61122780019d6886ee2e0ef) | event:task.rejected | gs.eventQueue("task.rejected" | 0f0ca5fec61122780019d6886ee2e0ef |
| business_rule:Update display value for topic tables(0f21b18f77d61110cd1b756f1b5a9992) | table:unconnected_category_content | new GlideRecord("unconnected_category_content") | 0f21b18f77d61110cd1b756f1b5a9992 |
| business_rule:Create or Update Suggestion Reader Group(0f2f678e5bd31010d9a5ce1a8581c714) | table:sys_suggestion_reader_group | new GlideRecord('sys_suggestion_reader_group') | 0f2f678e5bd31010d9a5ce1a8581c714 |
| business_rule:Check for duplicate work parameter(0f530aad230323002dd6cb0a56bf651e) | table:wm_agent_work_configuration | new GlideRecord('wm_agent_work_configuration') | 0f530aad230323002dd6cb0a56bf651e |
| business_rule:Update rule and profile state(0f58374d5b3210100977ca225681c7a3) | table:ais_rule | new GlideRecord('ais_rule') | 0f58374d5b3210100977ca225681c7a3 |
| business_rule:Update rule and profile state(0f58374d5b3210100977ca225681c7a3) | table:ais_search_profile | new GlideRecord('ais_search_profile') | 0f58374d5b3210100977ca225681c7a3 |
| business_rule:Update par_dashboard name(0f5acbefc7a20110f376a0736cc26044) | table:sys_ux_screen | new GlideRecord('sys_ux_screen') | 0f5acbefc7a20110f376a0736cc26044 |
| business_rule:Update par_dashboard name(0f5acbefc7a20110f376a0736cc26044) | table:par_dashboard | new GlideRecord('par_dashboard') | 0f5acbefc7a20110f376a0736cc26044 |
| business_rule:Enable Sidebar Prop(0f60d397c70121100c2c770bf4c26003) | table:sys_properties | new GlideRecord("sys_properties") | 0f60d397c70121100c2c770bf4c26003 |
| business_rule:Delete Account Contacts and Assets(0f934d50eb1012003e97afcef106fe07) | table:sn_customerservice_contact_relationship | new GlideRecord('sn_customerservice_contact_relationship') | 0f934d50eb1012003e97afcef106fe07 |
| business_rule:Delete Account Contacts and Assets(0f934d50eb1012003e97afcef106fe07) | table:sn_customerservice_m2m_asset_contact | new GlideRecord('sn_customerservice_m2m_asset_contact') | 0f934d50eb1012003e97afcef106fe07 |
| business_rule:Create Images and properties(0f983727b7320110e0969e68ee11a98a) | table:sys_cs_custom_adapter_property | new GlideRecord("sys_cs_custom_adapter_property") | 0f983727b7320110e0969e68ee11a98a |
| business_rule:Create Images and properties(0f983727b7320110e0969e68ee11a98a) | table:sys_cs_custom_adapter_property | new GlideRecord('sys_cs_custom_adapter_property') | 0f983727b7320110e0969e68ee11a98a |
| business_rule:Create Images and properties(0f983727b7320110e0969e68ee11a98a) | table:db_image | new GlideRecord('db_image') | 0f983727b7320110e0969e68ee11a98a |
| business_rule:Put No Archive Tables in Scratchpad(0fcb6ec5eb5321100dba9147c15228e2) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 0fcb6ec5eb5321100dba9147c15228e2 |
| business_rule:Put No Archive Tables in Scratchpad(0fcb6ec5eb5321100dba9147c15228e2) | table:sys_db_object | new GlideRecord('sys_db_object') | 0fcb6ec5eb5321100dba9147c15228e2 |
| business_rule:Validate MFA Browser FP Cookie Life Span(0fea19be730f3300fdbd04fbc4f6a7dd) | table:sys_auto_flush | new GlideRecord("sys_auto_flush") | 0fea19be730f3300fdbd04fbc4f6a7dd |
| business_rule:Add dirty flag in scratch pad(0ffa90db77033010f64307930d5a993a) | table:promin_model_def_version | new GlideRecord('promin_model_def_version') | 0ffa90db77033010f64307930d5a993a |
| business_rule:SNC Baseline Filter(10273615a9fe3dba00612154ff36846c) | table:cmdb_baseline | new GlideRecord('cmdb_baseline') | 10273615a9fe3dba00612154ff36846c |
| business_rule:Remove Scheduled Job(104b86a1d7210100fceaa6859e610322) | table:sys_trigger | new GlideRecord("sys_trigger") | 104b86a1d7210100fceaa6859e610322 |
| business_rule:Announce Tokyo Suggestion Reader Changes(10cd796cd18f0110f877986100e2fb20) | table:sys_upgrade_history | new GlideRecord('sys_upgrade_history') | 10cd796cd18f0110f877986100e2fb20 |
| business_rule:Announce Tokyo Suggestion Reader Changes(10cd796cd18f0110f877986100e2fb20) | table:sys_suggestion_reader_group | new GlideRecord('sys_suggestion_reader_group') | 10cd796cd18f0110f877986100e2fb20 |
| business_rule:Find Profiles Without Assertion Producer(10d21e79b721011044d59564ae11a939) | table:oauth_entity_profile | new GlideRecord("oauth_entity_profile") | 10d21e79b721011044d59564ae11a939 |
| business_rule:Delete Trigger and Plan(10db4b1ec30003002841b63b12d3ae30) | table:sys_hub_trigger_instance | new GlideRecord("sys_hub_trigger_instance") | 10db4b1ec30003002841b63b12d3ae30 |
| business_rule:Delete Trigger and Plan(10db4b1ec30003002841b63b12d3ae30) | table:sys_flow_trigger_plan | new GlideRecord("sys_flow_trigger_plan") | 10db4b1ec30003002841b63b12d3ae30 |
| business_rule:Delete Trigger and Plan(10db4b1ec30003002841b63b12d3ae30) | table:sys_flow_trigger | new GlideRecord("sys_flow_trigger") | 10db4b1ec30003002841b63b12d3ae30 |
| business_rule:table + workspace + view must unique(10df5df4c7320010cff9337bf4c26041) | table:sys_aw_form_uiaction_layout | new GlideRecord('sys_aw_form_uiaction_layout') | 10df5df4c7320010cff9337bf4c26041 |
| business_rule:Generate agent presence history(10e7632cb3003300fcfb6e5f26a8dc59) | table:awa_agent_presence | new GlideRecord('awa_agent_presence') | 10e7632cb3003300fcfb6e5f26a8dc59 |
| business_rule:Generate agent presence history(10e7632cb3003300fcfb6e5f26a8dc59) | table:awa_agent_channel_availability | new GlideRecord('awa_agent_channel_availability') | 10e7632cb3003300fcfb6e5f26a8dc59 |
| business_rule:Generate agent presence history(10e7632cb3003300fcfb6e5f26a8dc59) | table:awa_agent_presence_history | new GlideRecord('awa_agent_presence_history') | 10e7632cb3003300fcfb6e5f26a8dc59 |
| business_rule:Name field unique(10ec743a0fd333007049f140ff767e25) | table:sys_api_operation | new GlideRecord("sys_api_operation") | 10ec743a0fd333007049f140ff767e25 |
| business_rule:Validate Profile Capabilities(11851a787703301036a2cb90dc5a9986) | table:mid_profile_capability_m2m | new GlideRecord('mid_profile_capability_m2m') | 11851a787703301036a2cb90dc5a9986 |
| business_rule:WFApplyDatabusID(119ab623d7332100c0db6f14ce6103c6) | table:wf_activity | new GlideRecord('wf_activity') | 119ab623d7332100c0db6f14ce6103c6 |
| business_rule:Restrict duplicate filter name(11a0d9c3eb030110226ed5c1525228a9) | table:sn_ex_sp_todo_filter | new GlideRecord("sn_ex_sp_todo_filter") | 11a0d9c3eb030110226ed5c1525228a9 |
| business_rule:Limit tables for DWS resource views(11c3ddf178ddd210f8778a57f2947816) | table:sys_db_view_table | new GlideRecord("sys_db_view_table") | 11c3ddf178ddd210f8778a57f2947816 |
| business_rule:Maint Attribute Protection(11c47463bf3221000ba9dc2ecf0739bb) | table:sys_schema_attribute | new GlideRecord('sys_schema_attribute') | 11c47463bf3221000ba9dc2ecf0739bb |
| business_rule:Maint Attribute Protection(11c47463bf3221000ba9dc2ecf0739bb) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 11c47463bf3221000ba9dc2ecf0739bb |
| business_rule:Make is_mlb_enabled to false(11c7cdf0ff0022101471ffffffffffcf) | table:pa_indicators | new GlideRecord('pa_indicators') | 11c7cdf0ff0022101471ffffffffffcf |
| business_rule:Start publication workflow(11eb8390c3a012004bd67bfaa2d3aeb8) | table:sn_publications_workflow_config | new GlideRecord('sn_publications_workflow_config') | 11eb8390c3a012004bd67bfaa2d3aeb8 |
| business_rule:Display:Storage Server(11f4520b8f90120010340b5437bdee85) | table:cmdb_rel_ci | new GlideRecord('cmdb_rel_ci') | 11f4520b8f90120010340b5437bdee85 |
| business_rule:Delete Widget Navigation entry(1268cc7667002300f55f4d9e1585ef40) | table:widget_navigation | new GlideRecord('widget_navigation') | 1268cc7667002300f55f4d9e1585ef40 |
| business_rule:Fetch AI Search Allow List of Portals(129b5b13c7531010393d265c95c2605a) | table:sys_update_version | new GlideRecord('sys_update_version') | 129b5b13c7531010393d265c95c2605a |
| business_rule:Put Preview Count and Link on Scratchpad(12cc48e25b3650100977ca225681c7b7) | table:ais_child_table | new GlideRecord('ais_child_table') | 12cc48e25b3650100977ca225681c7b7 |
| business_rule:Avoid duplicate subscriptions(1321371467121300d358bb2d07415a95) | table:kb_social_qa_subscribe | new GlideRecord('kb_social_qa_subscribe') | 1321371467121300d358bb2d07415a95 |
| business_rule:Received email_unread Last Read(136238578b551210f2775bdfe22395a9) | table:messaging_unread | new GlideRecord("messaging_unread") | 136238578b551210f2775bdfe22395a9 |
| business_rule:PA Has Managed Indicator(137faa70eb10020065deac6aa206fea8) | table:pa_indicators | new GlideRecord('pa_indicators') | 137faa70eb10020065deac6aa206fea8 |
| business_rule:Abort changes  on group(13a621d8532c0010833addeeff7b12e7) | table:sys_user_grmember | new GlideRecord('sys_user_grmember') | 13a621d8532c0010833addeeff7b12e7 |
| business_rule:call Security API(13a62b85c33220100687e0dd9740ddfe) | table:sys_tiny_url | new GlideRecord("sys_tiny_url") | 13a62b85c33220100687e0dd9740ddfe |
| business_rule:Abort duplicate definition configs(13b6cb2077dab5106e2ff2e81e5a99f9) | table:sys_one_extend_definition_config | new GlideRecord('sys_one_extend_definition_config') | 13b6cb2077dab5106e2ff2e81e5a99f9 |
| script_include:ScheduledInstallService(000b82eb93312010ebd4f157b67ffb86) | table:sys_installation_schedule | new GlideRecord("sys_installation_schedule") | 000b82eb93312010ebd4f157b67ffb86 |
| script_include:ScheduledInstallService(000b82eb93312010ebd4f157b67ffb86) | table:sys_installation_schedule_item | new GlideRecord("sys_installation_schedule_item") | 000b82eb93312010ebd4f157b67ffb86 |
| script_include:ScheduledInstallService(000b82eb93312010ebd4f157b67ffb86) | table:sys_app_version | new GlideRecord("sys_app_version") | 000b82eb93312010ebd4f157b67ffb86 |
| script_include:ScheduledInstallService(000b82eb93312010ebd4f157b67ffb86) | table:sys_store_app | new GlideRecord("sys_store_app") | 000b82eb93312010ebd4f157b67ffb86 |
| script_include:ScheduledInstallService(000b82eb93312010ebd4f157b67ffb86) | event:sn_appclient.install.scheduled.plugins | gs.eventQueueScheduled("sn_appclient.install.scheduled.plugins" | 000b82eb93312010ebd4f157b67ffb86 |
| script_include:EmailClientRecipientListHandlerSNC(0017a9e277a11110398a45cfbd5a99e6) | table:sn_publications_recipients_list | new GlideRecord("sn_publications_recipients_list") | 0017a9e277a11110398a45cfbd5a99e6 |
| script_include:EmailClientRecipientListHandlerSNC(0017a9e277a11110398a45cfbd5a99e6) | table:sys_email | new GlideRecord("sys_email") | 0017a9e277a11110398a45cfbd5a99e6 |
| script_include:EmailClientRecipientListHandlerSNC(0017a9e277a11110398a45cfbd5a99e6) | table:sys_user | new GlideRecord('sys_user') | 0017a9e277a11110398a45cfbd5a99e6 |
| script_include:ProminFindingsDefUtilSNC(001df27a43d40210a829bf5ff7b8f267) | table:promin_automated_finding | new GlideRecordSecure('promin_automated_finding') | 001df27a43d40210a829bf5ff7b8f267 |
| script_include:ProminFindingsDefUtilSNC(001df27a43d40210a829bf5ff7b8f267) | table:promin_automated_finding_configuration | new GlideRecordSecure('promin_automated_finding_configuration') | 001df27a43d40210a829bf5ff7b8f267 |
| script_include:ProminFindingsDefUtilSNC(001df27a43d40210a829bf5ff7b8f267) | table:promin_project_entity | new GlideRecord('promin_project_entity') | 001df27a43d40210a829bf5ff7b8f267 |
| script_include:ProminFindingsDefUtilSNC(001df27a43d40210a829bf5ff7b8f267) | table:promin_activity_def | new GlideRecord('promin_activity_def') | 001df27a43d40210a829bf5ff7b8f267 |
| script_include:ProminFindingsDefUtilSNC(001df27a43d40210a829bf5ff7b8f267) | table:promin_process_def | new GlideRecord('promin_process_def') | 001df27a43d40210a829bf5ff7b8f267 |
| script_include:ProminFindingsDefUtilSNC(001df27a43d40210a829bf5ff7b8f267) | table:promin_finding_def | new GlideRecordSecure('promin_finding_def') | 001df27a43d40210a829bf5ff7b8f267 |
| script_include:ProminFindingsDefUtilSNC(001df27a43d40210a829bf5ff7b8f267) | table:promin_finding_def_rule | new GlideRecord('promin_finding_def_rule') | 001df27a43d40210a829bf5ff7b8f267 |
| script_include:ProminFindingsDefUtilSNC(001df27a43d40210a829bf5ff7b8f267) | table:promin_finding_def_constraint | new GlideRecord('promin_finding_def_constraint') | 001df27a43d40210a829bf5ff7b8f267 |
| script_include:ProminFindingsDefUtilSNC(001df27a43d40210a829bf5ff7b8f267) | table:promin_finding_def_condition | new GlideRecord('promin_finding_def_condition') | 001df27a43d40210a829bf5ff7b8f267 |
| script_include:MatchingRuleForAssignment(0036d3d8d732120058c92cf65e61038c) | table:matching_dimension | new GlideRecord("matching_dimension") | 0036d3d8d732120058c92cf65e61038c |
| script_include:CloneProfileUtil(00c74fc13b1333001b420896c3efc4f2) | table:clone_profile_exclusions | new GlideRecord('clone_profile_exclusions') | 00c74fc13b1333001b420896c3efc4f2 |
| script_include:CloneProfileUtil(00c74fc13b1333001b420896c3efc4f2) | table:clone_profile_preservers | new GlideRecord('clone_profile_preservers') | 00c74fc13b1333001b420896c3efc4f2 |
| script_include:CloneProfileUtil(00c74fc13b1333001b420896c3efc4f2) | table:clone_profile_cleanup_scripts | new GlideRecord('clone_profile_cleanup_scripts') | 00c74fc13b1333001b420896c3efc4f2 |
| script_include:CloneProfileUtil(00c74fc13b1333001b420896c3efc4f2) | table:clone_profile | new GlideRecord('clone_profile') | 00c74fc13b1333001b420896c3efc4f2 |
| script_include:Auth_IsScopeInDefaultProfile(00da16b053133300a91ccd2323dc3425) | table:oauth_entity_profile | new GlideRecord('oauth_entity_profile') | 00da16b053133300a91ccd2323dc3425 |
| script_include:Auth_IsScopeInDefaultProfile(00da16b053133300a91ccd2323dc3425) | table:oauth_entity | new GlideRecord('oauth_entity') | 00da16b053133300a91ccd2323dc3425 |
| script_include:MLSolutionDefinitionUtils(01528a057ff303009da45ac47dfa9190) | table:ml_autotrain_solution | new GlideRecord("ml_autotrain_solution") | 01528a057ff303009da45ac47dfa9190 |
| script_include:MLSolutionDefinitionUtils(01528a057ff303009da45ac47dfa9190) | table:ml_capability_definition_base | new GlideRecord('ml_capability_definition_base') | 01528a057ff303009da45ac47dfa9190 |
| script_include:MLSolutionDefinitionUtils(01528a057ff303009da45ac47dfa9190) | table:ml_capability | new GlideRecord('ml_capability') | 01528a057ff303009da45ac47dfa9190 |
| script_include:IndexCreator(017681d20a2581030070eb488bee3fb8) | table:sys_update_set | new GlideRecord('sys_update_set') | 017681d20a2581030070eb488bee3fb8 |
| script_include:IndexCreator(017681d20a2581030070eb488bee3fb8) | table:sys_db_object | new GlideRecord('sys_db_object') | 017681d20a2581030070eb488bee3fb8 |
| script_include:IndexCreator(017681d20a2581030070eb488bee3fb8) | table:sys_index | new GlideRecord('sys_index') | 017681d20a2581030070eb488bee3fb8 |
| script_include:HierarchicalFilterSelectorUtilSNC(01906a7919c15210f877d8fe9b306a3a) | table:sn_tp_territory | new GlideRecord("sn_tp_territory") | 01906a7919c15210f877d8fe9b306a3a |
| script_include:SCMetricsUtil(01e39eb5772031101b803a91fa5a9922) | table:sys_user | new GlideRecordSecure('sys_user') | 01e39eb5772031101b803a91fa5a9922 |
| script_include:SCMetricsUtil(01e39eb5772031101b803a91fa5a9922) | table:sysauto_pa | new GlideRecordSecure('sysauto_pa') | 01e39eb5772031101b803a91fa5a9922 |
| script_include:MLApplyClassificationTargetValues(021d065d73333300cddda4fa54f6a7f0) | table:ml_class | new GlideRecordSecure("ml_class") | 021d065d73333300cddda4fa54f6a7f0 |
| script_include:MLApplyClassificationTargetValues(021d065d73333300cddda4fa54f6a7f0) | table:ml_pc_lookup | new GlideRecordSecure("ml_pc_lookup") | 021d065d73333300cddda4fa54f6a7f0 |
| script_include:MLApplyClassificationTargetValues(021d065d73333300cddda4fa54f6a7f0) | table:ml_solution | new GlideRecordSecure('ml_solution') | 021d065d73333300cddda4fa54f6a7f0 |
| script_include:AppointmentBookingAjaxUtil(02a4d235d7804300811300285e61030a) | table:sn_apptmnt_booking_config_rule | new GlideRecord("sn_apptmnt_booking_config_rule") | 02a4d235d7804300811300285e61030a |
| script_include:AppointmentBookingAjaxUtil(02a4d235d7804300811300285e61030a) | table:sn_apptmnt_booking_appointment_booking | new GlideRecordSecure("sn_apptmnt_booking_appointment_booking") | 02a4d235d7804300811300285e61030a |
| script_include:AppointmentBookingAjaxUtil(02a4d235d7804300811300285e61030a) | table:sn_apptmnt_booking_service_config | new GlideRecordSecure("sn_apptmnt_booking_service_config") | 02a4d235d7804300811300285e61030a |
| script_include:UpdateSetAutoPreview(02ba7cd747103200a03a19fbac9a71bc) | table:sys_remote_update_set | new GlideRecord("sys_remote_update_set") | 02ba7cd747103200a03a19fbac9a71bc |
| script_include:UpdateSetAutoPreview(02ba7cd747103200a03a19fbac9a71bc) | table:sys_execution_tracker | new GlideRecord('sys_execution_tracker') | 02ba7cd747103200a03a19fbac9a71bc |
| script_include:ScopeCheck(02bbc79d37521200612747efbe41f1c5) | table:sys_scope | new GlideRecord('sys_scope') | 02bbc79d37521200612747efbe41f1c5 |
| script_include:CPIARUtils(02cd16d3eb0b01102b57e530695228e3) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 02cd16d3eb0b01102b57e530695228e3 |
| script_include:CPIARUtils(02cd16d3eb0b01102b57e530695228e3) | table:sysevent_email_action | new GlideRecord('sysevent_email_action') | 02cd16d3eb0b01102b57e530695228e3 |
| script_include:CPIARUtils(02cd16d3eb0b01102b57e530695228e3) | table:notify_sms_template | new GlideRecord('notify_sms_template') | 02cd16d3eb0b01102b57e530695228e3 |
| script_include:CPIARUtils(02cd16d3eb0b01102b57e530695228e3) | table:sys_cs_topic | new GlideRecord('sys_cs_topic') | 02cd16d3eb0b01102b57e530695228e3 |
| script_include:CPIARUtils(02cd16d3eb0b01102b57e530695228e3) | table:contract_sla | new GlideRecord('contract_sla') | 02cd16d3eb0b01102b57e530695228e3 |
| script_include:CPIARUtils(02cd16d3eb0b01102b57e530695228e3) | table:sys_plugins | new GlideRecord('sys_plugins') | 02cd16d3eb0b01102b57e530695228e3 |
| script_include:CPIARUtils(02cd16d3eb0b01102b57e530695228e3) | table:sys_cs_auto_resolution_configuration | new GlideRecord('sys_cs_auto_resolution_configuration') | 02cd16d3eb0b01102b57e530695228e3 |
| script_include:SNMapPageUtil(02db47afe77f330078d86188d2f6a988) | table:m2m_map_page_map_marker | new GlideRecord("m2m_map_page_map_marker") | 02db47afe77f330078d86188d2f6a988 |
| script_include:SOWChangeUtilsSNC(02e123a553615110532cddeeff7b129e) | table:change_request | new GlideRecord('change_request') | 02e123a553615110532cddeeff7b129e |
| script_include:SOWChangeUtilsSNC(02e123a553615110532cddeeff7b129e) | table:asmt_assessment_instance | new GlideRecord('asmt_assessment_instance') | 02e123a553615110532cddeeff7b129e |
| script_include:SOWChangeUtilsSNC(02e123a553615110532cddeeff7b129e) | table:change_risk_details | new GlideRecord('change_risk_details') | 02e123a553615110532cddeeff7b129e |
| script_include:SOWChangeUtilsSNC(02e123a553615110532cddeeff7b129e) | table:sysapproval_approver | new GlideRecord('sysapproval_approver') | 02e123a553615110532cddeeff7b129e |
| script_include:SOWChangeUtilsSNC(02e123a553615110532cddeeff7b129e) | table:chg_model | new GlideRecordSecure('chg_model') | 02e123a553615110532cddeeff7b129e |
| script_include:SOWChangeUtilsSNC(02e123a553615110532cddeeff7b129e) | table:sys_user_preference | new GlideRecordSecure('sys_user_preference') | 02e123a553615110532cddeeff7b129e |
| script_include:SOWChangeUtilsSNC(02e123a553615110532cddeeff7b129e) | table:sys_user_delegate | new GlideRecord('sys_user_delegate') | 02e123a553615110532cddeeff7b129e |
| script_include:CSMDefaultResourceHelper(02fd77107fc12300a8b1bdc8adfa9172) | table:ml_solution | new GlideRecord('ml_solution') | 02fd77107fc12300a8b1bdc8adfa9172 |
| script_include:CSMDefaultResourceHelper(02fd77107fc12300a8b1bdc8adfa9172) | table:ml_solution_definition | new GlideRecord('ml_solution_definition') | 02fd77107fc12300a8b1bdc8adfa9172 |
| script_include:CSMDefaultResourceHelper(02fd77107fc12300a8b1bdc8adfa9172) | table:cxs_search_res_config | new GlideRecord('cxs_search_res_config') | 02fd77107fc12300a8b1bdc8adfa9172 |
| script_include:CSMDefaultResourceHelper(02fd77107fc12300a8b1bdc8adfa9172) | table:cxs_res_context_config | new GlideRecord('cxs_res_context_config') | 02fd77107fc12300a8b1bdc8adfa9172 |
| script_include:GenAILargeInputPostprocessor(03007681433231101ed803295bb8f263) | table:sys_one_extend_definition_attribute | new GlideRecord("sys_one_extend_definition_attribute") | 03007681433231101ed803295bb8f263 |
| script_include:CABDefinitionSNC(0325a6f3eb32120034d1eeea1206fe9a) | table:cmn_schedule_span | new GlideRecord('cmn_schedule_span') | 0325a6f3eb32120034d1eeea1206fe9a |
| script_include:AgentScheduleAjax(0328a950c37312001c845cb981d3ae5c) | table:agent_events | new GlideRecord("agent_events") | 0328a950c37312001c845cb981d3ae5c |
| script_include:AgentScheduleAjax(0328a950c37312001c845cb981d3ae5c) | table:cmn_schedule_span | new GlideRecord("cmn_schedule_span") | 0328a950c37312001c845cb981d3ae5c |
| script_include:AgentScheduleAjax(0328a950c37312001c845cb981d3ae5c) | table:sys_user | new GlideRecord("sys_user") | 0328a950c37312001c845cb981d3ae5c |
| script_include:AgentScheduleAjax(0328a950c37312001c845cb981d3ae5c) | table:cmn_schedule | new GlideRecord('cmn_schedule') | 0328a950c37312001c845cb981d3ae5c |
| script_include:AgentScheduleAjax(0328a950c37312001c845cb981d3ae5c) | table:agent_events | new GlideRecord('agent_events') | 0328a950c37312001c845cb981d3ae5c |
| script_include:AgentScheduleAjax(0328a950c37312001c845cb981d3ae5c) | table:agent_schedule_user_pref | new GlideRecordSecure("agent_schedule_user_pref") | 0328a950c37312001c845cb981d3ae5c |
| script_include:AgentScheduleAjax(0328a950c37312001c845cb981d3ae5c) | table:agent_schedule_task_config_rel_user_pref | new GlideRecordSecure("agent_schedule_task_config_rel_user_pref") | 0328a950c37312001c845cb981d3ae5c |
| script_include:AgentScheduleAjax(0328a950c37312001c845cb981d3ae5c) | table:agent_schedule_task_config | new GlideRecord("agent_schedule_task_config") | 0328a950c37312001c845cb981d3ae5c |
| script_include:AgentScheduleAjax(0328a950c37312001c845cb981d3ae5c) | table:agent_schedule_user_pref | new GlideRecord('agent_schedule_user_pref') | 0328a950c37312001c845cb981d3ae5c |
| script_include:AgentScheduleAjax(0328a950c37312001c845cb981d3ae5c) | table:agent_schedule_task_config_rel_user_pref | new GlideRecord("agent_schedule_task_config_rel_user_pref") | 0328a950c37312001c845cb981d3ae5c |
| script_include:NowAssistDiagnosticsPackageInstallValidator(033516bd7fc0121005eb0ee66d8665d5) | table:v_plugin | new GlideRecord('v_plugin') | 033516bd7fc0121005eb0ee66d8665d5 |
| script_include:NowAssistDiagnosticsPackageInstallValidator(033516bd7fc0121005eb0ee66d8665d5) | table:sn_nowassist_diagn_package | new GlideRecord('sn_nowassist_diagn_package') | 033516bd7fc0121005eb0ee66d8665d5 |
| script_include:AisMigrationTableConfigHandler(0351f5e1531201107f03ddeeff7b1234) | table:ts_table_attribute_map | new GlideRecord('ts_table_attribute_map') | 0351f5e1531201107f03ddeeff7b1234 |
| script_include:AisMigrationTableConfigHandler(0351f5e1531201107f03ddeeff7b1234) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 0351f5e1531201107f03ddeeff7b1234 |
| script_include:WorkflowApprovalUtils(0360b36d0a0a0b260a89dfec60c339c4) | table:sysapproval_approver | new GlideRecord('sysapproval_approver') | 0360b36d0a0a0b260a89dfec60c339c4 |
| script_include:WorkflowApprovalUtils(0360b36d0a0a0b260a89dfec60c339c4) | table:sysapproval_group | new GlideRecord('sysapproval_group') | 0360b36d0a0a0b260a89dfec60c339c4 |
| script_include:WorkflowApprovalUtils(0360b36d0a0a0b260a89dfec60c339c4) | table:sys_user_grmember | new GlideRecord('sys_user_grmember') | 0360b36d0a0a0b260a89dfec60c339c4 |
| script_include:WorkflowApprovalUtils(0360b36d0a0a0b260a89dfec60c339c4) | table:wf_activity | new GlideRecord('wf_activity') | 0360b36d0a0a0b260a89dfec60c339c4 |
| script_include:WorkflowApprovalUtils(0360b36d0a0a0b260a89dfec60c339c4) | table:wf_executing | new GlideRecord('wf_executing') | 0360b36d0a0a0b260a89dfec60c339c4 |
| script_include:WorkflowApprovalUtils(0360b36d0a0a0b260a89dfec60c339c4) | table:sys_user | new GlideRecord("sys_user") | 0360b36d0a0a0b260a89dfec60c339c4 |
| script_include:WorkflowApprovalUtils(0360b36d0a0a0b260a89dfec60c339c4) | table:sys_user_group | new GlideRecord("sys_user_group") | 0360b36d0a0a0b260a89dfec60c339c4 |
| script_include:WorkflowApprovalUtils(0360b36d0a0a0b260a89dfec60c339c4) | table:task | new GlideRecord('task') | 0360b36d0a0a0b260a89dfec60c339c4 |
| script_include:WorkflowApprovalUtils(0360b36d0a0a0b260a89dfec60c339c4) | table:sys_user | new GlideRecord('sys_user') | 0360b36d0a0a0b260a89dfec60c339c4 |
| script_include:TestExecutorAjax(0380e2605b2212006f23efe5f0f91abd) | table:sys_atf_performance_run | new GlideRecord('sys_atf_performance_run') | 0380e2605b2212006f23efe5f0f91abd |
| script_include:TestExecutorAjax(0380e2605b2212006f23efe5f0f91abd) | table:sys_atf_test_result | new GlideRecord('sys_atf_test_result') | 0380e2605b2212006f23efe5f0f91abd |
| script_include:TestExecutorAjax(0380e2605b2212006f23efe5f0f91abd) | table:sys_atf_test_suite_result | new GlideRecord('sys_atf_test_suite_result') | 0380e2605b2212006f23efe5f0f91abd |
| script_include:TestExecutorAjax(0380e2605b2212006f23efe5f0f91abd) | table:sys_atf_test_suite | new GlideRecord('sys_atf_test_suite') | 0380e2605b2212006f23efe5f0f91abd |
| script_include:TestExecutorAjax(0380e2605b2212006f23efe5f0f91abd) | table:sys_atf_test | new GlideRecord('sys_atf_test') | 0380e2605b2212006f23efe5f0f91abd |
| script_include:TestExecutorAjax(0380e2605b2212006f23efe5f0f91abd) | table:sys_template | new GlideRecord("sys_template") | 0380e2605b2212006f23efe5f0f91abd |
| script_include:TestExecutorAjax(0380e2605b2212006f23efe5f0f91abd) | table:sys_aw_master_config | new GlideRecord('sys_aw_master_config') | 0380e2605b2212006f23efe5f0f91abd |
| script_include:TestExecutorAjax(0380e2605b2212006f23efe5f0f91abd) | table:sys_atf_test_result_item | new GlideRecord("sys_atf_test_result_item") | 0380e2605b2212006f23efe5f0f91abd |
| script_include:SubscriptionDetailDao(03e974afffd9a110468365d7d3b8fe9e) | table:subscription_detail | new GlideRecord('subscription_detail') | 03e974afffd9a110468365d7d3b8fe9e |
| script_include:ISCEventsUtil(03ee950514189300964fa81e247aa80b) | table:appsec_security_notifications | new GlideRecord("appsec_security_notifications") | 03ee950514189300964fa81e247aa80b |
| script_include:ISCEventsUtil(03ee950514189300964fa81e247aa80b) | table:cmn_notif_device | new GlideRecord("cmn_notif_device") | 03ee950514189300964fa81e247aa80b |
| script_include:ISCEventsUtil(03ee950514189300964fa81e247aa80b) | table:cmn_notif_message | new GlideRecord("cmn_notif_message") | 03ee950514189300964fa81e247aa80b |
| script_include:ISCEventsUtil(03ee950514189300964fa81e247aa80b) | table:appsec_security_dashboard_event_logs | new GlideRecord("appsec_security_dashboard_event_logs") | 03ee950514189300964fa81e247aa80b |
| script_include:LDAPClientUtils(03f911531b310100227e5581be0713d7) | table:ldap_ou_config | new GlideRecord("ldap_ou_config") | 03f911531b310100227e5581be0713d7 |
| script_include:VTBBoardSecurity(0429f513eb2311001c13abf11206fe08) | table:vtb_board_member | new GlideRecord('vtb_board_member') | 0429f513eb2311001c13abf11206fe08 |
| script_include:CABAbstractDefMeetSNC(0466d2a9eb2022002a7a666cd206fefc) | table:sys_user | new GlideRecord("sys_user") | 0466d2a9eb2022002a7a666cd206fefc |
| script_include:SCComparisonUtil(046c1a8653301110dd8eddeeff7b126e) | table:sn_vsc_hardening_compliance_scores | new GlideRecord('sn_vsc_hardening_compliance_scores') | 046c1a8653301110dd8eddeeff7b126e |
| script_include:SCComparisonUtil(046c1a8653301110dd8eddeeff7b126e) | table:pa_job_logs | new GlideRecord('pa_job_logs') | 046c1a8653301110dd8eddeeff7b126e |
| script_include:SCComparisonUtil(046c1a8653301110dd8eddeeff7b126e) | table:pa_indicators | new GlideRecord('pa_indicators') | 046c1a8653301110dd8eddeeff7b126e |
| script_include:SCComparisonUtil(046c1a8653301110dd8eddeeff7b126e) | table:sn_vsc_instance_hardening_settings | new GlideRecord('sn_vsc_instance_hardening_settings') | 046c1a8653301110dd8eddeeff7b126e |
| script_include:SCComparisonUtil(046c1a8653301110dd8eddeeff7b126e) | table:sn_vsc_user_comparisons | new GlideRecord("sn_vsc_user_comparisons") | 046c1a8653301110dd8eddeeff7b126e |
| script_include:SCComparisonUtil(046c1a8653301110dd8eddeeff7b126e) | table:sn_vsc_changed_hardening_settings | new GlideRecord("sn_vsc_changed_hardening_settings") | 046c1a8653301110dd8eddeeff7b126e |
| script_include:SCComparisonUtil(046c1a8653301110dd8eddeeff7b126e) | event:sn_vsc.sec.hardening.comparison | gs.eventQueue('sn_vsc.sec.hardening.comparison' | 046c1a8653301110dd8eddeeff7b126e |
| script_include:TemplateIOValidator(047517a45b53101001fb0c370581c75b) | table:sys_app_template_input_var | new GlideRecord("sys_app_template_input_var") | 047517a45b53101001fb0c370581c75b |
| script_include:TemplateIOValidator(047517a45b53101001fb0c370581c75b) | table:sys_app_template_output_var | new GlideRecord("sys_app_template_output_var") | 047517a45b53101001fb0c370581c75b |
| script_include:ViewConfigMetadata(04827ed667823110f6c7f0270af9220e) | table:sys_sg_view_config | new GlideRecordSecure('sys_sg_view_config') | 04827ed667823110f6c7f0270af9220e |
| script_include:ViewConfigMetadata(04827ed667823110f6c7f0270af9220e) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 04827ed667823110f6c7f0270af9220e |
| script_include:ViewConfigMetadata(04827ed667823110f6c7f0270af9220e) | table:sys_sg_view_template_slot | new GlideRecordSecure('sys_sg_view_template_slot') | 04827ed667823110f6c7f0270af9220e |
| script_include:ViewConfigMetadata(04827ed667823110f6c7f0270af9220e) | table:sys_sg_view_config_field | new GlideRecordSecure('sys_sg_view_config_field') | 04827ed667823110f6c7f0270af9220e |
| script_include:CISETReprocessCheck(04ac19509f802300487df84bc42e7033) | table:sys_import_set | new GlideRecord("sys_import_set") | 04ac19509f802300487df84bc42e7033 |
| script_include:cxs_ResourceContextConfig(04b365f35377130005ecddeeff7b1246) | table:cxs_res_context_config | new GlideRecord("cxs_res_context_config") | 04b365f35377130005ecddeeff7b1246 |
| script_include:PartRequirementStageHandler(04bfec47c33b10007304072a1fba8fc6) | table:sm_part_requirement | new GlideRecord('sm_part_requirement') | 04bfec47c33b10007304072a1fba8fc6 |
| script_include:PartRequirementStageHandler(04bfec47c33b10007304072a1fba8fc6) | table:alm_transfer_order_line | new GlideRecord('alm_transfer_order_line') | 04bfec47c33b10007304072a1fba8fc6 |
| script_include:RTBIUtilAjaxSNC(05016ab79f4c0210df2476308a0a1cc0) | table:m2m_dictionary_dataclass | new GlideRecordSecure('m2m_dictionary_dataclass') | 05016ab79f4c0210df2476308a0a1cc0 |
| script_include:RTBIUtilAjaxSNC(05016ab79f4c0210df2476308a0a1cc0) | table:sn_rtbi_classified_field | new GlideRecord('sn_rtbi_classified_field') | 05016ab79f4c0210df2476308a0a1cc0 |
| script_include:RTBIUtilAjaxSNC(05016ab79f4c0210df2476308a0a1cc0) | table:sn_rtbi_primary_reference | new GlideRecord('sn_rtbi_primary_reference') | 05016ab79f4c0210df2476308a0a1cc0 |
| script_include:RTBIUtilAjaxSNC(05016ab79f4c0210df2476308a0a1cc0) | table:sn_rtbi_report_template | new GlideRecordSecure('sn_rtbi_report_template') | 05016ab79f4c0210df2476308a0a1cc0 |
| script_include:DefaultRoleUtils(0507037e93310200288679b4f47ffbf5) | table:sys_user_role | new GlideRecord('sys_user_role') | 0507037e93310200288679b4f47ffbf5 |
| script_include:ExportDefinitionHelper(05086ed3471331004695d7527c9a7194) | table:sys_ui_view | new GlideRecord('sys_ui_view') | 05086ed3471331004695d7527c9a7194 |
| script_include:ExportDefinitionHelper(05086ed3471331004695d7527c9a7194) | table:sys_ui_list | new GlideRecord('sys_ui_list') | 05086ed3471331004695d7527c9a7194 |
| script_include:ExportDefinitionHelper(05086ed3471331004695d7527c9a7194) | table:sys_ui_list_element | new GlideRecord('sys_ui_list_element') | 05086ed3471331004695d7527c9a7194 |
| script_include:CIListRecordPropsMetadata(0510a08ceb5e0110da1861c59c522841) | table:sys_cs_context_profile | new GlideRecord('sys_cs_context_profile') | 0510a08ceb5e0110da1861c59c522841 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:sc_cat_item | new GlideRecord('sc_cat_item') | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:checklist_template | new GlideRecord('checklist_template') | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:checklist | new GlideRecord('checklist') | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:checklist_item | new GlideRecord('checklist_item') | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:sm_template_definition | new GlideRecord('sm_template_definition') | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:sm_config | new GlideRecord('sm_config') | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:sm_m2m_task_dependency | new GlideRecord('sm_m2m_task_dependency') | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:sm_m2m_task_template_dependency | new GlideRecord('sm_m2m_task_template_dependency') | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:sm_part_requirement | new GlideRecord('sm_part_requirement') | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:cmdb_model_part_requirement | new GlideRecord('cmdb_model_part_requirement') | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:sm_m2m_somodel_stmodel | new GlideRecord("sm_m2m_somodel_stmodel") | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:hr_case | new GlideRecord("hr_case") | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:cmdb_hr_task_product_model | new GlideRecord('cmdb_hr_task_product_model') | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:hr_task | new GlideRecord('hr_task') | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:cmdb_model_part_requirement | new GlideRecord("cmdb_model_part_requirement") | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:sm_part_requirement | new GlideRecord("sm_part_requirement") | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:servicetask_model_skill | new GlideRecord("servicetask_model_skill") | 0530d0f0d7311100158ba6859e610384 |
| script_include:SMTemplates(0530d0f0d7311100158ba6859e610384) | table:task_m2m_skill | new GlideRecord("task_m2m_skill") | 0530d0f0d7311100158ba6859e610384 |
| script_include:ScriptedJournalValueProvider(05393c0297091110ca2671571153af24) | table:sys_journal_field | new GlideRecord('sys_journal_field') | 05393c0297091110ca2671571153af24 |
| script_include:MultiSSOv2_SAML2_internal(055e19b20b21230001d36c4d37673ae9) | table:sys_user | new GlideRecord("sys_user") | 055e19b20b21230001d36c4d37673ae9 |
| script_include:MultiSSOv2_SAML2_internal(055e19b20b21230001d36c4d37673ae9) | table:core_company | new GlideRecord("core_company") | 055e19b20b21230001d36c4d37673ae9 |
| script_include:CSMLookupVerifyUtil(05683ab8b7302300992561c8ee11a92f) | table:sn_lookup_verify_config | new GlideRecord('sn_lookup_verify_config') | 05683ab8b7302300992561c8ee11a92f |
| script_include:STTRMConditionTypeSNC(058c66d45303101034d1ddeeff7b1295) | table:sttrm_condition_type_field | new GlideRecord('sttrm_condition_type_field') | 058c66d45303101034d1ddeeff7b1295 |
| script_include:SearchMetadata(05b0c68867732200b133956c33415a9e) | table:sys_user_preference | new GlideRecord("sys_user_preference") | 05b0c68867732200b133956c33415a9e |
| script_include:SearchMetadata(05b0c68867732200b133956c33415a9e) | table:sys_properties | new GlideRecord("sys_properties") | 05b0c68867732200b133956c33415a9e |
| script_include:SearchMetadata(05b0c68867732200b133956c33415a9e) | table:ts_group | new GlideRecord("ts_group") | 05b0c68867732200b133956c33415a9e |
| script_include:SearchMetadata(05b0c68867732200b133956c33415a9e) | table:ts_table | new GlideRecord("ts_table") | 05b0c68867732200b133956c33415a9e |
| script_include:NoteTemplate(05b971650b32320036e62c7885673afd) | table:sn_m2m_note_template_for_table | new GlideRecord('sn_m2m_note_template_for_table') | 05b971650b32320036e62c7885673afd |
| script_include:ConnectionAndCredentialHelper(05bf438a872233001bf5bd6ec7cb0b65) | table:sys_connection | new GlideRecord('sys_connection') | 05bf438a872233001bf5bd6ec7cb0b65 |
| script_include:ConnectionAndCredentialHelper(05bf438a872233001bf5bd6ec7cb0b65) | table:oauth_2_0_credentials | new GlideRecord('oauth_2_0_credentials') | 05bf438a872233001bf5bd6ec7cb0b65 |
| script_include:ConnectionAndCredentialHelper(05bf438a872233001bf5bd6ec7cb0b65) | table:oauth_entity_profile | new GlideRecord('oauth_entity_profile') | 05bf438a872233001bf5bd6ec7cb0b65 |
| script_include:AutoResolutionSimulationHelper(05e30d60ff9a2010635f056d793bf1b4) | table:sysauto_script | new GlideRecord('sysauto_script') | 05e30d60ff9a2010635f056d793bf1b4 |
| script_include:UserRoleDaoV1(05ee3976ff612110468365d7d3b8fed5) | table:license_details_assoc_roles | new GlideRecord('license_details_assoc_roles') | 05ee3976ff612110468365d7d3b8fed5 |
| script_include:ScriptDetails(0613b1a39f1202107c0e2305fa0a1ca8) | table:sys_script_include | new GlideRecord('sys_script_include') | 0613b1a39f1202107c0e2305fa0a1ca8 |
| script_include:ScriptDetails(0613b1a39f1202107c0e2305fa0a1ca8) | table:sys_store_app | new GlideRecord('sys_store_app') | 0613b1a39f1202107c0e2305fa0a1ca8 |
| script_include:GenAIProviderUtil(0624dc3affe4b210a3aeffffffffffe8) | table:sn_ns_provider_configuration | new GlideRecord('sn_ns_provider_configuration') | 0624dc3affe4b210a3aeffffffffffe8 |
| script_include:GenAIProviderUtil(0624dc3affe4b210a3aeffffffffffe8) | table:sn_ns_manage_llm_change_history | new GlideRecord('sn_ns_manage_llm_change_history') | 0624dc3affe4b210a3aeffffffffffe8 |
| script_include:GenAIProviderUtil(0624dc3affe4b210a3aeffffffffffe8) | table:sys_gen_ai_provider_preference | new GlideRecord('sys_gen_ai_provider_preference') | 0624dc3affe4b210a3aeffffffffffe8 |
| script_include:GenAIProviderUtil(0624dc3affe4b210a3aeffffffffffe8) | table:sn_nowassist_skill_config | new GlideRecord('sn_nowassist_skill_config') | 0624dc3affe4b210a3aeffffffffffe8 |
| script_include:GenAIProviderUtil(0624dc3affe4b210a3aeffffffffffe8) | table:sn_ns_config_m2m_skill | new GlideRecord('sn_ns_config_m2m_skill') | 0624dc3affe4b210a3aeffffffffffe8 |
| script_include:GenAIProviderUtil(0624dc3affe4b210a3aeffffffffffe8) | table:sys_generative_ai_provider_mapping | new GlideRecord('sys_generative_ai_provider_mapping') | 0624dc3affe4b210a3aeffffffffffe8 |
| script_include:GenAIProviderUtil(0624dc3affe4b210a3aeffffffffffe8) | table:sys_one_extend_capability_definition | new GlideRecord('sys_one_extend_capability_definition') | 0624dc3affe4b210a3aeffffffffffe8 |
| script_include:GenAIProviderUtil(0624dc3affe4b210a3aeffffffffffe8) | table:sys_one_extend_definition_config | new GlideRecord('sys_one_extend_definition_config') | 0624dc3affe4b210a3aeffffffffffe8 |
| script_include:GenAIProviderUtil(0624dc3affe4b210a3aeffffffffffe8) | table:sys_gen_ai_provider_preference_audit | new GlideRecord('sys_gen_ai_provider_preference_audit') | 0624dc3affe4b210a3aeffffffffffe8 |
| script_include:ep_Licensing(062556a077911110a956b9999a5a99bf) | table:sn_employee_app_access | new GlideRecord('sn_employee_app_access') | 062556a077911110a956b9999a5a99bf |
| script_include:ep_Licensing(062556a077911110a956b9999a5a99bf) | table:sn_employee_app | new GlideRecord('sn_employee_app') | 062556a077911110a956b9999a5a99bf |
| script_include:ep_Licensing(062556a077911110a956b9999a5a99bf) | table:sn_employee_app_access_criteria | new GlideRecord("sn_employee_app_access_criteria") | 062556a077911110a956b9999a5a99bf |
| script_include:DynamicSchedulingAgentRecommendationNew(066437bcc32132001c845cb981d3ae3d) | table:cmn_location | new GlideRecord("cmn_location") | 066437bcc32132001c845cb981d3ae3d |
| script_include:DynamicSchedulingAgentRecommendationNew(066437bcc32132001c845cb981d3ae3d) | table:sys_user | new GlideRecord('sys_user') | 066437bcc32132001c845cb981d3ae3d |
| script_include:DynamicSchedulingAgentRecommendationNew(066437bcc32132001c845cb981d3ae3d) | table:sm_task | new GlideRecord("sm_task") | 066437bcc32132001c845cb981d3ae3d |
| script_include:DynamicSchedulingAgentRecommendationNew(066437bcc32132001c845cb981d3ae3d) | table:sm_m2m_task_dependency | new GlideRecord("sm_m2m_task_dependency") | 066437bcc32132001c845cb981d3ae3d |
| script_include:LinkRecordProducerToIncident(0694bcc267230300fa50775617415a19) | table:incident | new GlideRecord("incident") | 0694bcc267230300fa50775617415a19 |
| script_include:LinkRecordProducerToIncident(0694bcc267230300fa50775617415a19) | table:interaction | new GlideRecord("interaction") | 0694bcc267230300fa50775617415a19 |
| script_include:AssetNumberAbbreviation(06997dc1a1172010fa9b12d16d68eb5d) | table:fx_currency | new GlideRecord('fx_currency') | 06997dc1a1172010fa9b12d16d68eb5d |
| script_include:DiscoveryCMDBUtil(06a8b503c3b73100d8d4bea192d3ae2d) | table:cmdb_ci | new GlideRecord("cmdb_ci") | 06a8b503c3b73100d8d4bea192d3ae2d |
| script_include:DiscoveryCMDBUtil(06a8b503c3b73100d8d4bea192d3ae2d) | table:cmdb_ie_run | new GlideRecord('cmdb_ie_run') | 06a8b503c3b73100d8d4bea192d3ae2d |
| script_include:TrendRecommendation(06ac564453d323004acaddeeff7b12ce) | table:trend_definition | new GlideRecord("trend_definition") | 06ac564453d323004acaddeeff7b12ce |
| script_include:WFStageSet(06b405e91b010100adca1e094f07132f) | table:stage_set | new GlideRecord('stage_set') | 06b405e91b010100adca1e094f07132f |
| script_include:WFStageSet(06b405e91b010100adca1e094f07132f) | table:wf_stage | new GlideRecord('wf_stage') | 06b405e91b010100adca1e094f07132f |
| script_include:WFStageSet(06b405e91b010100adca1e094f07132f) | table:stage_set_entry | new GlideRecord('stage_set_entry') | 06b405e91b010100adca1e094f07132f |
| script_include:WFStageSet(06b405e91b010100adca1e094f07132f) | table:sys_translated | new GlideRecord('sys_translated') | 06b405e91b010100adca1e094f07132f |
| script_include:WFStageSet(06b405e91b010100adca1e094f07132f) | table:wf_workflow_version | new GlideRecord("wf_workflow_version") | 06b405e91b010100adca1e094f07132f |
| script_include:WFStageSet(06b405e91b010100adca1e094f07132f) | table:sys_choice | new GlideRecord("sys_choice") | 06b405e91b010100adca1e094f07132f |
| script_include:WFStageSet(06b405e91b010100adca1e094f07132f) | table:stage_set_table | new GlideRecord('stage_set_table') | 06b405e91b010100adca1e094f07132f |
| script_include:AppointmentBookingDao(06e69b52d7433200811300285e6103f8) | table:sc_cat_item_producer | new GlideRecord("sc_cat_item_producer") | 06e69b52d7433200811300285e6103f8 |
| script_include:AppointmentBookingDao(06e69b52d7433200811300285e6103f8) | table:sm_template_definition | new GlideRecord("sm_template_definition") | 06e69b52d7433200811300285e6103f8 |
| script_include:AppointmentBookingDao(06e69b52d7433200811300285e6103f8) | table:sm_m2m_somodel_stmodel | new GlideRecord("sm_m2m_somodel_stmodel") | 06e69b52d7433200811300285e6103f8 |
| script_include:AppointmentBookingDao(06e69b52d7433200811300285e6103f8) | table:sys_choice | new GlideRecord("sys_choice") | 06e69b52d7433200811300285e6103f8 |
| script_include:MobileThemeStyleValuePairs(06f379c43b4000101a2d47e573efc473) | table:sys_sg_theme_style | new GlideRecord("sys_sg_theme_style") | 06f379c43b4000101a2d47e573efc473 |
| script_include:HubAjaxProcessor(071c450293203100a61db530967ffb38) | table:sys_update_set_source | GlideRecord("sys_update_set_source") | 071c450293203100a61db530967ffb38 |
| script_include:ScopeChecker(074b4b33d720020092610eca5e6103a7) | table:sys_store_app | new GlideRecord("sys_store_app") | 074b4b33d720020092610eca5e6103a7 |
| script_include:ProminUtils(078d0838536500109e9eddeeff7b128b) | table:promin_project_entity | new GlideRecord("promin_project_entity") | 078d0838536500109e9eddeeff7b128b |
| script_include:ProminUtils(078d0838536500109e9eddeeff7b128b) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 078d0838536500109e9eddeeff7b128b |
| script_include:ProminUtils(078d0838536500109e9eddeeff7b128b) | table:promin_model_def_version | new GlideRecord("promin_model_def_version") | 078d0838536500109e9eddeeff7b128b |
| script_include:ProminUtils(078d0838536500109e9eddeeff7b128b) | table:promin_child_table_config | new GlideRecordSecure('promin_child_table_config') | 078d0838536500109e9eddeeff7b128b |
| script_include:ProminUtils(078d0838536500109e9eddeeff7b128b) | table:promin_process_def | new GlideRecordSecure('promin_process_def') | 078d0838536500109e9eddeeff7b128b |
| script_include:ProminUtils(078d0838536500109e9eddeeff7b128b) | table:promin_playbook | new GlideRecord('promin_playbook') | 078d0838536500109e9eddeeff7b128b |
| script_include:ProminUtils(078d0838536500109e9eddeeff7b128b) | table:promin_view_field_config | new GlideRecord('promin_view_field_config') | 078d0838536500109e9eddeeff7b128b |
| script_include:ProminUtils(078d0838536500109e9eddeeff7b128b) | table:promin_activity_def | new GlideRecord("promin_activity_def") | 078d0838536500109e9eddeeff7b128b |
| script_include:UpdateVersionAPI(07a9e54393210200a738941e867ffb78) | table:sys_update_version | new GlideRecord('sys_update_version') | 07a9e54393210200a738941e867ffb78 |
| script_include:ImportSetRowHelper(07ad84c073940010952d31d7caf6a78e) | table:sys_import_set | new GlideRecordSecure("sys_import_set") | 07ad84c073940010952d31d7caf6a78e |
| script_include:ImportSetRowHelper(07ad84c073940010952d31d7caf6a78e) | table:sys_transform_map | new GlideRecordSecure("sys_transform_map") | 07ad84c073940010952d31d7caf6a78e |
| script_include:ImportSetRowHelper(07ad84c073940010952d31d7caf6a78e) | table:sys_import_set_run | new GlideRecordSecure("sys_import_set_run") | 07ad84c073940010952d31d7caf6a78e |
| script_include:DelegatedDevUserPermissions(07cb2e9667f302006cc275f557415a63) | table:sys_scope_permission_set_role_assignment | new GlideRecord('sys_scope_permission_set_role_assignment') | 07cb2e9667f302006cc275f557415a63 |
| script_include:DelegatedDevUserPermissions(07cb2e9667f302006cc275f557415a63) | table:sys_user_has_role | new GlideRecord('sys_user_has_role') | 07cb2e9667f302006cc275f557415a63 |
| script_include:CancelProcessesAjax(0809f57a434661104e75fcc5fbb8f2a3) | table:sys_pd_context | new GlideRecord('sys_pd_context') | 0809f57a434661104e75fcc5fbb8f2a3 |
| script_include:UninstallValidator(0830fa950f012110aaefc6b1df767e13) | table:sys_store_app | new GlideRecord('sys_store_app') | 0830fa950f012110aaefc6b1df767e13 |
| script_include:UninstallValidator(0830fa950f012110aaefc6b1df767e13) | table:sys_scoped_plugin | new GlideRecord('sys_scoped_plugin') | 0830fa950f012110aaefc6b1df767e13 |
| script_include:UninstallValidator(0830fa950f012110aaefc6b1df767e13) | table:sys_scoped_plugin | new GlideRecord("sys_scoped_plugin") | 0830fa950f012110aaefc6b1df767e13 |
| script_include:UninstallValidator(0830fa950f012110aaefc6b1df767e13) | table:sys_store_app | new GlideRecord("sys_store_app") | 0830fa950f012110aaefc6b1df767e13 |
| script_include:KeylinesBsmAJAX(0833cd52bf211100eae043fada0739c8) | table:cmdb_rel_ci | new GlideRecordSecure('cmdb_rel_ci') | 0833cd52bf211100eae043fada0739c8 |
| script_include:KeylinesBsmAJAX(0833cd52bf211100eae043fada0739c8) | table:cmdb_rel_type | new GlideRecordSecure('cmdb_rel_type') | 0833cd52bf211100eae043fada0739c8 |
| script_include:TemplateFlowModel(083f005e5b10101001fb0c370581c7a4) | table:sys_app_template_type | new GlideRecord('sys_app_template_type') | 083f005e5b10101001fb0c370581c7a4 |
| script_include:ServiceMappingAjaxUtils(085d06ada311311013c5265765fcda2f) | table:service_table_config | new GlideRecord('service_table_config') | 085d06ada311311013c5265765fcda2f |
| script_include:MIDServerAjax(08751bed0a0a0bb400d923b4595ceca4) | table:ecc_agent | new GlideRecord("ecc_agent") | 08751bed0a0a0bb400d923b4595ceca4 |
| script_include:MIDServerAjax(08751bed0a0a0bb400d923b4595ceca4) | table:automation_status_set | new GlideRecord("automation_status_set") | 08751bed0a0a0bb400d923b4595ceca4 |
| script_include:StudioUtils(089ff2821b7f8a90cb682f092a4bcb8c) | table:sys_scope | new GlideRecord('sys_scope') | 089ff2821b7f8a90cb682f092a4bcb8c |
| script_include:GeneralWOForm(08f481067f231200068712f44efa919d) | table:db_image | new GlideRecord("db_image") | 08f481067f231200068712f44efa919d |
| script_include:GeneralWOForm(08f481067f231200068712f44efa919d) | table:sys_attachment | new GlideRecord("sys_attachment") | 08f481067f231200068712f44efa919d |
| script_include:GeneralWOForm(08f481067f231200068712f44efa919d) | table:wm_order | new GlideRecord("wm_order") | 08f481067f231200068712f44efa919d |
| script_include:GeneralWOForm(08f481067f231200068712f44efa919d) | table:wm_task | new GlideRecord("wm_task") | 08f481067f231200068712f44efa919d |
| script_include:GeneralWOForm(08f481067f231200068712f44efa919d) | table:task_time_worked | new GlideRecord("task_time_worked") | 08f481067f231200068712f44efa919d |
| script_include:GeneralWOForm(08f481067f231200068712f44efa919d) | table:sm_asset_usage | new GlideRecord("sm_asset_usage") | 08f481067f231200068712f44efa919d |
| script_include:GeneralWOForm(08f481067f231200068712f44efa919d) | table:sm_incidentals | new GlideRecord("sm_incidentals") | 08f481067f231200068712f44efa919d |
| script_include:GeneralWOForm(08f481067f231200068712f44efa919d) | table:signature_image | new GlideRecord('signature_image') | 08f481067f231200068712f44efa919d |
| script_include:GeneralWOForm(08f481067f231200068712f44efa919d) | table:sys_attachment | new GlideRecord('sys_attachment') | 08f481067f231200068712f44efa919d |
| script_include:SubscriptionApplicationUsersDao(090e2c85b7a90210ad650481de11a9d0) | table:license_role_type | new GlideRecord('license_role_type') | 090e2c85b7a90210ad650481de11a9d0 |
| script_include:SubscriptionApplicationUsersDao(090e2c85b7a90210ad650481de11a9d0) | table:license_role | new GlideRecord('license_role') | 090e2c85b7a90210ad650481de11a9d0 |
| script_include:SubscriptionApplicationUsersDao(090e2c85b7a90210ad650481de11a9d0) | table:sys_user_role | new GlideRecord('sys_user_role') | 090e2c85b7a90210ad650481de11a9d0 |
| script_include:SubscriptionApplicationUsersDao(090e2c85b7a90210ad650481de11a9d0) | table:sys_user | new GlideRecord('sys_user') | 090e2c85b7a90210ad650481de11a9d0 |
| script_include:DiscoveryStatus(0923b5ee0ab30150007c408f74342949) | table:discovery_status | new GlideRecord('discovery_status') | 0923b5ee0ab30150007c408f74342949 |
| script_include:DiscoveryStatus(0923b5ee0ab30150007c408f74342949) | table:ecc_queue | new GlideRecord('ecc_queue') | 0923b5ee0ab30150007c408f74342949 |
| script_include:DiscoveryStatus(0923b5ee0ab30150007c408f74342949) | table:sysevent | new GlideRecord('sysevent') | 0923b5ee0ab30150007c408f74342949 |
| script_include:DiscoveryStatus(0923b5ee0ab30150007c408f74342949) | table:discovery_status | GlideRecord('discovery_status') | 0923b5ee0ab30150007c408f74342949 |
| script_include:MIDServer(0924b3600ab301500055eba755a623a1) | table:ecc_agent | new GlideRecord('ecc_agent') | 0924b3600ab301500055eba755a623a1 |
| script_include:MIDServer(0924b3600ab301500055eba755a623a1) | table:ecc_agent_application | new GlideRecord('ecc_agent_application') | 0924b3600ab301500055eba755a623a1 |
| script_include:CentralDispatchConfigRESTHelper(093e36450bd232008141ab5c37673ab0) | table:central_dispatch_config | new GlideRecordSecure("central_dispatch_config") | 093e36450bd232008141ab5c37673ab0 |
| script_include:CentralDispatchConfigRESTHelper(093e36450bd232008141ab5c37673ab0) | table:wm_task | new GlideRecordSecure("wm_task") | 093e36450bd232008141ab5c37673ab0 |
| script_include:CentralDispatchConfigRESTHelper(093e36450bd232008141ab5c37673ab0) | table:sys_choice | new GlideRecord("sys_choice") | 093e36450bd232008141ab5c37673ab0 |
| script_include:CentralDispatchConfigRESTHelper(093e36450bd232008141ab5c37673ab0) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 093e36450bd232008141ab5c37673ab0 |
| script_include:ManageSkillsUtils(0946b5a987fb51101bf7a64d0ebb35bd) | table:sys_user | new GlideRecordSecure("sys_user") | 0946b5a987fb51101bf7a64d0ebb35bd |
| script_include:ManageSkillsUtils(0946b5a987fb51101bf7a64d0ebb35bd) | table:cmn_skill | new GlideRecordSecure("cmn_skill") | 0946b5a987fb51101bf7a64d0ebb35bd |
| script_include:ManageSkillsUtils(0946b5a987fb51101bf7a64d0ebb35bd) | table:cmn_skill_level_type | new GlideRecordSecure("cmn_skill_level_type") | 0946b5a987fb51101bf7a64d0ebb35bd |
| script_include:ManageSkillsUtils(0946b5a987fb51101bf7a64d0ebb35bd) | table:cmn_skill_level | new GlideRecordSecure("cmn_skill_level") | 0946b5a987fb51101bf7a64d0ebb35bd |
| script_include:ManageSkillsUtils(0946b5a987fb51101bf7a64d0ebb35bd) | table:cmn_department | new GlideRecordSecure("cmn_department") | 0946b5a987fb51101bf7a64d0ebb35bd |
| script_include:ManageSkillsUtils(0946b5a987fb51101bf7a64d0ebb35bd) | table:sys_user_has_skill | new GlideRecordSecure("sys_user_has_skill") | 0946b5a987fb51101bf7a64d0ebb35bd |
| script_include:ExpertUIPolicyBuilder(094fde740a0006d4014100237cf8bbe1) | table:expert_ui_policy_action | new GlideRecord('expert_ui_policy_action') | 094fde740a0006d4014100237cf8bbe1 |
| script_include:ScopedAppPackageSuppressor(097f1a8193210200d9b9941e867ffb4e) | table:wf_workflow_version | new GlideRecord('wf_workflow_version') | 097f1a8193210200d9b9941e867ffb4e |
| script_include:ScopedAppPackageSuppressor(097f1a8193210200d9b9941e867ffb4e) | table:sys_choice_set | new GlideRecord('sys_choice_set') | 097f1a8193210200d9b9941e867ffb4e |
| script_include:ScopedAppPackageSuppressor(097f1a8193210200d9b9941e867ffb4e) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 097f1a8193210200d9b9941e867ffb4e |
| script_include:cxs_DefSearcherUtils(0986285b5382201034d1ddeeff7b124d) | table:cxs_search_res_config | new GlideRecord("cxs_search_res_config") | 0986285b5382201034d1ddeeff7b124d |
| script_include:cxs_DefSearcherUtils(0986285b5382201034d1ddeeff7b124d) | table:cxs_res_context_config | new GlideRecord("cxs_res_context_config") | 0986285b5382201034d1ddeeff7b124d |
| script_include:ContextualSidePanelListTransformScript(098fe26c4343021091ea7ebba7b8f225) | table:sys_ux_app_route | new GlideRecord('sys_ux_app_route') | 098fe26c4343021091ea7ebba7b8f225 |
| script_include:ContextualSidePanelListTransformScript(098fe26c4343021091ea7ebba7b8f225) | table:sys_ux_screen | new GlideRecord('sys_ux_screen') | 098fe26c4343021091ea7ebba7b8f225 |
| script_include:MobilePushNotificationHelper(09cee175531130103296ddeeff7b1234) | table:sys_cs_message_notification | new GlideRecord('sys_cs_message_notification') | 09cee175531130103296ddeeff7b1234 |
| script_include:MobilePushNotificationHelper(09cee175531130103296ddeeff7b1234) | table:sysevent_email_action | new GlideRecord('sysevent_email_action') | 09cee175531130103296ddeeff7b1234 |
| script_include:MobilePushNotificationHelper(09cee175531130103296ddeeff7b1234) | table:sys_push_notif_msg | new GlideRecord('sys_push_notif_msg') | 09cee175531130103296ddeeff7b1234 |
| script_include:MobilePushNotificationHelper(09cee175531130103296ddeeff7b1234) | table:sys_push_application | new GlideRecord('sys_push_application') | 09cee175531130103296ddeeff7b1234 |
| script_include:MobilePushNotificationHelper(09cee175531130103296ddeeff7b1234) | table:sys_push_notif_app_install | new GlideRecord('sys_push_notif_app_install') | 09cee175531130103296ddeeff7b1234 |
| script_include:MobilePushNotificationHelper(09cee175531130103296ddeeff7b1234) | table:sys_cs_consumer | new GlideRecord('sys_cs_consumer') | 09cee175531130103296ddeeff7b1234 |
| script_include:MobilePushNotificationHelper(09cee175531130103296ddeeff7b1234) | table:sys_cs_consumer_account | new GlideRecord('sys_cs_consumer_account') | 09cee175531130103296ddeeff7b1234 |
| script_include:CIIdentifier(0a1b69430a0a0b1c3dfe47a73b725038) | table:ci_identifier | new GlideRecord('ci_identifier') | 0a1b69430a0a0b1c3dfe47a73b725038 |
| script_include:LifeCycleFieldsAlignmentJobUtil(0a295651530d02101da8ddeeff7b1207) | table:sys_trigger | new GlideRecord("sys_trigger") | 0a295651530d02101da8ddeeff7b1207 |
| script_include:GenAILargeInputHandler(0a5b5649433a31101ed803295bb8f202) | table:sys_script_include | new GlideRecord("sys_script_include") | 0a5b5649433a31101ed803295bb8f202 |
| script_include:EmailFileImportUtils(0a5d86081ba660103c0ffc4e0d4bcb80) | table:sys_trigger | new GlideRecord("sys_trigger") | 0a5d86081ba660103c0ffc4e0d4bcb80 |
| script_include:EmailFileImportUtils(0a5d86081ba660103c0ffc4e0d4bcb80) | table:sys_data_source | new GlideRecord("sys_data_source") | 0a5d86081ba660103c0ffc4e0d4bcb80 |
| script_include:EmailFileImportUtils(0a5d86081ba660103c0ffc4e0d4bcb80) | table:sys_attachment | new GlideRecord("sys_attachment") | 0a5d86081ba660103c0ffc4e0d4bcb80 |
| script_include:BusinessCalendarSpanUtils(0a7bcdebe8014210f87772ce355c6774) | table:business_calendar_span | new GlideRecord("business_calendar_span") | 0a7bcdebe8014210f87772ce355c6774 |
| script_include:BusinessCalendarSpanUtils(0a7bcdebe8014210f87772ce355c6774) | table:sys_trigger | new GlideRecord("sys_trigger") | 0a7bcdebe8014210f87772ce355c6774 |
| script_include:CMDBDynamicIREProcessor(0a90d4700b50201099b8ea7885673aa4) | table:sys_db_object | new GlideRecord('sys_db_object') | 0a90d4700b50201099b8ea7885673aa4 |
| script_include:CMDBDynamicIREProcessor(0a90d4700b50201099b8ea7885673aa4) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 0a90d4700b50201099b8ea7885673aa4 |
| script_include:CustomerPushActionUtils(0aa3df1011f18210f877fb5045d0c4ed) | table:sys_ux_banner_announcement | new GlideRecord("sys_ux_banner_announcement") | 0aa3df1011f18210f877fb5045d0c4ed |
| script_include:CustomerPushActionUtils(0aa3df1011f18210f877fb5045d0c4ed) | table:sys_ux_m2m_banner_announcement | new GlideRecord("sys_ux_m2m_banner_announcement") | 0aa3df1011f18210f877fb5045d0c4ed |
| script_include:CustomerPushActionUtils(0aa3df1011f18210f877fb5045d0c4ed) | table:cds_client_schedule | new GlideRecord("cds_client_schedule") | 0aa3df1011f18210f877fb5045d0c4ed |
| script_include:CustomerPushActionUtils(0aa3df1011f18210f877fb5045d0c4ed) | table:sn_vsc_client_push_notifications | new GlideRecord('sn_vsc_client_push_notifications') | 0aa3df1011f18210f877fb5045d0c4ed |
| script_include:CustomerPushActionUtils(0aa3df1011f18210f877fb5045d0c4ed) | table:sysauto_script | new GlideRecord("sysauto_script") | 0aa3df1011f18210f877fb5045d0c4ed |
| script_include:McbOpenModalUtil(0ac2f515eb683110bd5afd0052522802) | table:sys_scope | new GlideRecordSecure("sys_scope") | 0ac2f515eb683110bd5afd0052522802 |
| script_include:McbOpenModalUtil(0ac2f515eb683110bd5afd0052522802) | table:sys_sg_list_screen | new GlideRecordSecure("sys_sg_list_screen") | 0ac2f515eb683110bd5afd0052522802 |
| script_include:McbOpenModalUtil(0ac2f515eb683110bd5afd0052522802) | table:sys_sg_map_screen | new GlideRecordSecure("sys_sg_map_screen") | 0ac2f515eb683110bd5afd0052522802 |
| script_include:McbOpenModalUtil(0ac2f515eb683110bd5afd0052522802) | table:sys_sg_master_item | new GlideRecordSecure("sys_sg_master_item") | 0ac2f515eb683110bd5afd0052522802 |
| script_include:McbOpenModalUtil(0ac2f515eb683110bd5afd0052522802) | table:sys_sg_form_screen | new GlideRecordSecure("sys_sg_form_screen") | 0ac2f515eb683110bd5afd0052522802 |
| script_include:RestCatalogUtil(0ae1e780c3001200d68d3b0ac3d3ae4e) | table:catalog_script_client | new GlideRecord('catalog_script_client') | 0ae1e780c3001200d68d3b0ac3d3ae4e |
| script_include:RestCatalogUtil(0ae1e780c3001200d68d3b0ac3d3ae4e) | table:item_option_new | new GlideRecord('item_option_new') | 0ae1e780c3001200d68d3b0ac3d3ae4e |
| script_include:RestCatalogUtil(0ae1e780c3001200d68d3b0ac3d3ae4e) | table:sc_cat_item_catalog | new GlideRecord("sc_cat_item_catalog") | 0ae1e780c3001200d68d3b0ac3d3ae4e |
| script_include:WMTask(0b26c0721bbb0010985ba64fad4bcbcd) | table:sm_part_requirement | new GlideRecord("sm_part_requirement") | 0b26c0721bbb0010985ba64fad4bcbcd |
| script_include:WMTask(0b26c0721bbb0010985ba64fad4bcbcd) | table:sf_state_flow | new GlideRecord("sf_state_flow") | 0b26c0721bbb0010985ba64fad4bcbcd |
| script_include:WMTask(0b26c0721bbb0010985ba64fad4bcbcd) | table:wm_task | new GlideRecord("wm_task") | 0b26c0721bbb0010985ba64fad4bcbcd |
| script_include:LicensingEngineGlideRecordHelper(0b505a36ff210210ad65ffffffffffce) | table:subscription_has_family | new GlideRecord("subscription_has_family") | 0b505a36ff210210ad65ffffffffffce |
| script_include:PublicationAjax(0b628eb4c30112004bd67bfaa2d3aeef) | table:sn_publications_publication | new GlideRecord('sn_publications_publication') | 0b628eb4c30112004bd67bfaa2d3aeef |
| script_include:ChangeInfoSNC(0b7dcfbca700011003396c94d17901c7) | table:chg_ctx_sidebar_card | new GlideRecord('chg_ctx_sidebar_card') | 0b7dcfbca700011003396c94d17901c7 |
| script_include:ChangeInfoSNC(0b7dcfbca700011003396c94d17901c7) | table:sn_chg_probability_details | new GlideRecord('sn_chg_probability_details') | 0b7dcfbca700011003396c94d17901c7 |
| script_include:ChangeInfoSNC(0b7dcfbca700011003396c94d17901c7) | table:sys_user_grmember | new GlideRecord('sys_user_grmember') | 0b7dcfbca700011003396c94d17901c7 |
| script_include:ChangeInfoSNC(0b7dcfbca700011003396c94d17901c7) | table:cab_agenda_item | new GlideRecord('cab_agenda_item') | 0b7dcfbca700011003396c94d17901c7 |
| script_include:ChangeInfoSNC(0b7dcfbca700011003396c94d17901c7) | table:cab_meeting | new GlideRecord('cab_meeting') | 0b7dcfbca700011003396c94d17901c7 |
| script_include:PwdEnrollEmailProcessor(0bad75020b400300572a6f3ef6673a4c) | table:pwd_device | new GlideRecord('pwd_device') | 0bad75020b400300572a6f3ef6673a4c |
| script_include:ChecklistUtil(0bcbe951c31202004e44dccdf3d3ae2a) | table:checklist_item | new GlideRecord("checklist_item") | 0bcbe951c31202004e44dccdf3d3ae2a |
| script_include:ChecklistUtil(0bcbe951c31202004e44dccdf3d3ae2a) | table:checklist_template | new GlideRecord("checklist_template") | 0bcbe951c31202004e44dccdf3d3ae2a |
| script_include:ChecklistUtil(0bcbe951c31202004e44dccdf3d3ae2a) | table:checklist_template | new GlideRecord('checklist_template') | 0bcbe951c31202004e44dccdf3d3ae2a |
| script_include:ChecklistUtil(0bcbe951c31202004e44dccdf3d3ae2a) | table:checklist | new GlideRecord('checklist') | 0bcbe951c31202004e44dccdf3d3ae2a |
| script_include:ChecklistUtil(0bcbe951c31202004e44dccdf3d3ae2a) | table:checklist_item | new GlideRecord('checklist_item') | 0bcbe951c31202004e44dccdf3d3ae2a |
| script_include:KBPortalSitemapGeneratorUtil(0bea6d45382a9110f8778af503189ee4) | table:sp_page | new GlideRecord('sp_page') | 0bea6d45382a9110f8778af503189ee4 |
| script_include:KBPortalSitemapGeneratorUtil(0bea6d45382a9110f8778af503189ee4) | table:m2m_sp_portal_knowledge_base | new GlideRecord('m2m_sp_portal_knowledge_base') | 0bea6d45382a9110f8778af503189ee4 |
| script_include:KBPortalSitemapGeneratorUtil(0bea6d45382a9110f8778af503189ee4) | table:kb_knowledge | new GlideRecord('kb_knowledge') | 0bea6d45382a9110f8778af503189ee4 |
| script_include:KBPortalSitemapGeneratorUtil(0bea6d45382a9110f8778af503189ee4) | table:m2m_sp_portal_catalog | new GlideRecord('m2m_sp_portal_catalog') | 0bea6d45382a9110f8778af503189ee4 |
| script_include:KBPortalSitemapGeneratorUtil(0bea6d45382a9110f8778af503189ee4) | table:sc_cat_item | new GlideRecord('sc_cat_item') | 0bea6d45382a9110f8778af503189ee4 |
| script_include:SCSecurityPolicyUtil(0c086b4989b98210f8774e7712acff95) | table:sn_vsc_security_policy | new GlideRecord("sn_vsc_security_policy") | 0c086b4989b98210f8774e7712acff95 |
| script_include:SCSecurityPolicyUtil(0c086b4989b98210f8774e7712acff95) | table:sys_hub_action_input | new GlideRecord("sys_hub_action_input") | 0c086b4989b98210f8774e7712acff95 |
| script_include:SCSecurityPolicyUtil(0c086b4989b98210f8774e7712acff95) | table:sys_hub_action_type_definition | new GlideRecord("sys_hub_action_type_definition") | 0c086b4989b98210f8774e7712acff95 |
| script_include:SCSecurityPolicyUtil(0c086b4989b98210f8774e7712acff95) | table:sn_vsc_hub_action_restriction | new GlideRecord("sn_vsc_hub_action_restriction") | 0c086b4989b98210f8774e7712acff95 |
| script_include:AWAStatsUtils(0c13aac253320010a0bdddeeff7b1229) | table:awa_service_channel | new GlideRecordSecure('awa_service_channel') | 0c13aac253320010a0bdddeeff7b1229 |
| script_include:AWAStatsUtils(0c13aac253320010a0bdddeeff7b1229) | table:sys_rw_action | new GlideRecordSecure('sys_rw_action') | 0c13aac253320010a0bdddeeff7b1229 |
| script_include:AWAStatsUtils(0c13aac253320010a0bdddeeff7b1229) | table:awa_agent_channel_availability | new GlideRecordSecure('awa_agent_channel_availability') | 0c13aac253320010a0bdddeeff7b1229 |
| script_include:AWAStatsUtils(0c13aac253320010a0bdddeeff7b1229) | table:awa_queue | new GlideRecordSecure('awa_queue') | 0c13aac253320010a0bdddeeff7b1229 |
| script_include:AWAStatsUtils(0c13aac253320010a0bdddeeff7b1229) | table:awa_eligibility_pool | new GlideRecordSecure('awa_eligibility_pool') | 0c13aac253320010a0bdddeeff7b1229 |
| script_include:AWAStatsUtils(0c13aac253320010a0bdddeeff7b1229) | table:sys_user_grmember | new GlideRecordSecure('sys_user_grmember') | 0c13aac253320010a0bdddeeff7b1229 |
| script_include:AWAStatsUtils(0c13aac253320010a0bdddeeff7b1229) | table:awa_agent_presence | new GlideRecordSecure('awa_agent_presence') | 0c13aac253320010a0bdddeeff7b1229 |
| script_include:AWAStatsUtils(0c13aac253320010a0bdddeeff7b1229) | table:awa_presence_state | new GlideRecordSecure('awa_presence_state') | 0c13aac253320010a0bdddeeff7b1229 |
| script_include:AWAStatsUtils(0c13aac253320010a0bdddeeff7b1229) | table:awa_agent_capacity | new GlideRecordSecure('awa_agent_capacity') | 0c13aac253320010a0bdddeeff7b1229 |
| script_include:AisMigrationTitleTextHandler(0c1cb724531201107f03ddeeff7b1265) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 0c1cb724531201107f03ddeeff7b1265 |
| script_include:AisMigrationTitleTextHandler(0c1cb724531201107f03ddeeff7b1265) | table:sys_ui_list | new GlideRecord('sys_ui_list') | 0c1cb724531201107f03ddeeff7b1265 |
| script_include:AisMigrationTitleTextHandler(0c1cb724531201107f03ddeeff7b1265) | table:sys_ui_list_element | new GlideRecord('sys_ui_list_element') | 0c1cb724531201107f03ddeeff7b1265 |
| script_include:CSMRelationshipService_CaseRelatedParty(0c47f904eb523010bbd186de4252281a) | table:sys_user_has_role | new GlideRecord('sys_user_has_role') | 0c47f904eb523010bbd186de4252281a |
| script_include:CMDBIdentifierUtil(0c496b700f51201024b63ab1df767e79) | table:cmdb_identifier_entry | new GlideRecord('cmdb_identifier_entry') | 0c496b700f51201024b63ab1df767e79 |
| script_include:EntitlementAttachmentReader(0c51d81a7ff45610d6492e4cfc8665e4) | table:sys_attachment | new GlideRecord('sys_attachment') | 0c51d81a7ff45610d6492e4cfc8665e4 |
| script_include:VSCScanAjaxProcessor(0c628f8053a60110a8edddeeff7b124d) | table:scan_table_check | new GlideRecord("scan_table_check") | 0c628f8053a60110a8edddeeff7b124d |
| script_include:VSCScanAjaxProcessor(0c628f8053a60110a8edddeeff7b124d) | table:scan_column_type_check | new GlideRecord("scan_column_type_check") | 0c628f8053a60110a8edddeeff7b124d |
| script_include:FieldEncryptionConfigurationUtil(0c6412e2a3831210dbc28964851e6143) | table:sys_encrypted_field_row_configuration | new GlideRecordSecure("sys_encrypted_field_row_configuration") | 0c6412e2a3831210dbc28964851e6143 |
| script_include:pwdEnrollmentReminderHelper(0c7c54b00b06030031a567bff6673ac0) | table:sysevent_register | GlideRecord("sysevent_register") | 0c7c54b00b06030031a567bff6673ac0 |
| script_include:pwdEnrollmentReminderHelper(0c7c54b00b06030031a567bff6673ac0) | table:pwd_map_proc_to_group | new GlideRecord("pwd_map_proc_to_group") | 0c7c54b00b06030031a567bff6673ac0 |
| script_include:pwdEnrollmentReminderHelper(0c7c54b00b06030031a567bff6673ac0) | table:sys_user | new GlideRecord("sys_user") | 0c7c54b00b06030031a567bff6673ac0 |
| script_include:pwdEnrollmentReminderHelper(0c7c54b00b06030031a567bff6673ac0) | table:pwd_process | new GlideRecord("pwd_process") | 0c7c54b00b06030031a567bff6673ac0 |
| script_include:pwdEnrollmentReminderHelper(0c7c54b00b06030031a567bff6673ac0) | table:sys_trigger | new GlideRecord("sys_trigger") | 0c7c54b00b06030031a567bff6673ac0 |
| script_include:pwdEnrollmentReminderHelper(0c7c54b00b06030031a567bff6673ac0) | event:pwd.enrollment_reminder.trigger | gs.eventQueue("pwd.enrollment_reminder.trigger" | 0c7c54b00b06030031a567bff6673ac0 |
| script_include:SchemaCompare(0cd6fd2d07301000be32a04ff1021e90) | table:sys_schema_check | new GlideRecord('sys_schema_check') | 0cd6fd2d07301000be32a04ff1021e90 |
| script_include:SchemaCompare(0cd6fd2d07301000be32a04ff1021e90) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 0cd6fd2d07301000be32a04ff1021e90 |
| script_include:SchemaCompare(0cd6fd2d07301000be32a04ff1021e90) | table:sys_schema_check_table | new GlideRecord('sys_schema_check_table') | 0cd6fd2d07301000be32a04ff1021e90 |
| script_include:SchemaCompare(0cd6fd2d07301000be32a04ff1021e90) | table:sys_schema_check_detail | new GlideRecord('sys_schema_check_detail') | 0cd6fd2d07301000be32a04ff1021e90 |
| script_include:MatchingDimensionPreferredSecondaryTechnicians(0ce48110932d0210b262772efaba1038) | table:sys_user | new GlideRecord('sys_user') | 0ce48110932d0210b262772efaba1038 |
| script_include:SNHelpSetupMigrationUtil(0d32cd9beb3002107626211f1a52286c) | table:help_user_interaction | new GlideRecord('help_user_interaction') | 0d32cd9beb3002107626211f1a52286c |
| script_include:GetUIPolicyTable(0d46ada1b7321300897725cbde11a949) | table:sys_sg_ui_policy | new GlideRecord('sys_sg_ui_policy') | 0d46ada1b7321300897725cbde11a949 |
| script_include:GenAIAssistsCountDAO(0de8afb043ac0210482439a56cb8f277) | table:sn_entitlement_genai_assist_counts | new GlideRecord('sn_entitlement_genai_assist_counts') | 0de8afb043ac0210482439a56cb8f277 |
| script_include:KBAnswerFieldsValidationAjax(0de8c573ff4072103670ffffffffff59) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 0de8c573ff4072103670ffffffffff59 |
| script_include:KBAnswerFieldsValidationAjax(0de8c573ff4072103670ffffffffff59) | table:sys_db_object | new GlideRecord('sys_db_object') | 0de8c573ff4072103670ffffffffff59 |
| script_include:WorkflowStageDef(0e1748329f102000dada207c7f4bcc7a) | table:wf_stage | new GlideRecord('wf_stage') | 0e1748329f102000dada207c7f4bcc7a |
| script_include:VCSAppAccessCheck(0e1e124f673012006cc295f557415adf) | table:sys_app | new GlideRecord("sys_app") | 0e1e124f673012006cc295f557415adf |
| script_include:IncidentUtils2SNC(0ebbe74fc7001010c24ae122c7c26009) | table:incident | new GlideRecord("incident") | 0ebbe74fc7001010c24ae122c7c26009 |
| script_include:VAAISearchHelperYokohama(0eec0b4bffb0321006574f5f8f3bf188) | table:sc_cat_item_content | new GlideRecord("sc_cat_item_content") | 0eec0b4bffb0321006574f5f8f3bf188 |
| script_include:SPMUtilsFoundationImpl(0ef1f659b3403300f224a72256a8dc5e) | table:spm_taxonomy_node | new GlideRecord('spm_taxonomy_node') | 0ef1f659b3403300f224a72256a8dc5e |
| script_include:SPMUtilsFoundationImpl(0ef1f659b3403300f224a72256a8dc5e) | table:spm_taxonomy_node | new GlideRecord("spm_taxonomy_node") | 0ef1f659b3403300f224a72256a8dc5e |
| script_include:SPMUtilsFoundationImpl(0ef1f659b3403300f224a72256a8dc5e) | table:cmdb_ci_service | new GlideRecord("cmdb_ci_service") | 0ef1f659b3403300f224a72256a8dc5e |
| script_include:SPMUtilsFoundationImpl(0ef1f659b3403300f224a72256a8dc5e) | table:service_offering | new GlideRecord("service_offering") | 0ef1f659b3403300f224a72256a8dc5e |
| script_include:SPMUtilsFoundationImpl(0ef1f659b3403300f224a72256a8dc5e) | table:life_cycle_mapping | new GlideRecord('life_cycle_mapping') | 0ef1f659b3403300f224a72256a8dc5e |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:cmdb_ci_service_calculated | new GlideRecord('cmdb_ci_service_calculated') | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:cmdb_ci_service | new GlideRecord('cmdb_ci_service') | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:cmdb_ci_service_by_tags | new GlideRecord('cmdb_ci_service_by_tags') | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:sys_db_object | new GlideRecord('sys_db_object') | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:sa_m2m_service_entry_point | new GlideRecord('sa_m2m_service_entry_point') | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:cmdb_ci_endpoint_manual | new GlideRecord('cmdb_ci_endpoint_manual') | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:cmdb_ci_service_auto | new GlideRecord('cmdb_ci_service_auto') | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:cmdb_identifier_entry | new GlideRecord("cmdb_identifier_entry") | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:service_process_task | new GlideRecord("service_process_task") | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:cmdb_ci_service_discovered | new GlideRecordSecure('cmdb_ci_service_discovered') | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:cmdb_ci_query_based_service | new GlideRecord('cmdb_ci_query_based_service') | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:svc_by_tags_candidates | new GlideRecord('svc_by_tags_candidates') | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:sa_entry_point_ui_card | new GlideRecord('sa_entry_point_ui_card') | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:CSDMAppServiceHelper(0ef3fd1d73c30010ee4dd3c72bf6a704) | table:cmdb_ci_service_auto | new GlideRecordSecure('cmdb_ci_service_auto') | 0ef3fd1d73c30010ee4dd3c72bf6a704 |
| script_include:ServiceMappingRelationUtil(0f015cc77f1322008f1c3b19befa910b) | table:cmdb_rel_type | new GlideRecord('cmdb_rel_type') | 0f015cc77f1322008f1c3b19befa910b |
| script_include:ServiceMappingRelationUtil(0f015cc77f1322008f1c3b19befa910b) | table:cmdb_rel_ci | new GlideRecord('cmdb_rel_ci') | 0f015cc77f1322008f1c3b19befa910b |
| script_include:SDSelfServiceAnalyticsUtils(0f086cf953d8421066e3ddeeff7b12b9) | table:sys_cb_topic_category | new GlideRecord('sys_cb_topic_category') | 0f086cf953d8421066e3ddeeff7b12b9 |
| script_include:SDSelfServiceAnalyticsUtils(0f086cf953d8421066e3ddeeff7b12b9) | table:ssa_deflection_pattern | new GlideRecord('ssa_deflection_pattern') | 0f086cf953d8421066e3ddeeff7b12b9 |
| script_include:SDSelfServiceAnalyticsUtils(0f086cf953d8421066e3ddeeff7b12b9) | table:sn_actsub_source_context_mapping | new GlideRecord('sn_actsub_source_context_mapping') | 0f086cf953d8421066e3ddeeff7b12b9 |
| script_include:SDSelfServiceAnalyticsUtils(0f086cf953d8421066e3ddeeff7b12b9) | table:ssa_pattern_m2m_element | new GlideRecord('ssa_pattern_m2m_element') | 0f086cf953d8421066e3ddeeff7b12b9 |
| script_include:CSMLookupVerifyAjaxUtil(0f2d078a733600106dfdbd49faf6a737) | table:sn_lookup_verify_config | new GlideRecord('sn_lookup_verify_config') | 0f2d078a733600106dfdbd49faf6a737 |
| script_include:ChangeModelChgReqAPISNC(0f41f8eb5303101034d1ddeeff7b12fd) | table:change_request | new GlideRecord("change_request") | 0f41f8eb5303101034d1ddeeff7b12fd |
| script_include:ChangeModelChgReqAPISNC(0f41f8eb5303101034d1ddeeff7b12fd) | table:chg_model | new GlideRecord("chg_model") | 0f41f8eb5303101034d1ddeeff7b12fd |
| script_include:UpgradeHistoryLogPriority(0f43a330c3333100f25d174292d3ae07) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 0f43a330c3333100f25d174292d3ae07 |
| script_include:UpgradeHistoryLogPriority(0f43a330c3333100f25d174292d3ae07) | table:sys_app_file_type | new GlideRecord('sys_app_file_type') | 0f43a330c3333100f25d174292d3ae07 |
| script_include:VaCallbackPropertyUtil(0fa68d6a53130110657addeeff7b12cc) | table:sys_properties | new GlideRecord("sys_properties") | 0fa68d6a53130110657addeeff7b12cc |
| script_include:cxs_FltrConfig(0fbf18a6d773220034d145bcce6103f3) | table:cxs_ui_config_base | new GlideRecord("cxs_ui_config_base") | 0fbf18a6d773220034d145bcce6103f3 |
| script_include:cxs_FltrConfig(0fbf18a6d773220034d145bcce6103f3) | table:cxs_search_res_config | new GlideRecord("cxs_search_res_config") | 0fbf18a6d773220034d145bcce6103f3 |
| script_include:cxs_FltrConfig(0fbf18a6d773220034d145bcce6103f3) | table:cxs_table_fltr_config | new GlideRecord("cxs_table_fltr_config") | 0fbf18a6d773220034d145bcce6103f3 |
| script_include:cxs_FltrConfig(0fbf18a6d773220034d145bcce6103f3) | table:cxs_res_context_config | new GlideRecord('cxs_res_context_config') | 0fbf18a6d773220034d145bcce6103f3 |
| script_include:cxs_FltrConfig(0fbf18a6d773220034d145bcce6103f3) | table:cxs_rp_fltr_config | new GlideRecord("cxs_rp_fltr_config") | 0fbf18a6d773220034d145bcce6103f3 |
| script_include:UIRuleOperationService(0fc48c0643311110e24e7075dbb8f2d6) | table:sys_sg_ui_rule_operation | new GlideRecord('sys_sg_ui_rule_operation') | 0fc48c0643311110e24e7075dbb8f2d6 |
| script_include:PluginDependency(0fd60b2e0b500300894181a037673ad6) | table:sn_dependentclient_app_plugin_map | new GlideRecord("sn_dependentclient_app_plugin_map") | 0fd60b2e0b500300894181a037673ad6 |
| script_include:PluginDependency(0fd60b2e0b500300894181a037673ad6) | event:sn_dependentclient.check.dependent_apps | gs.eventQueue('sn_dependentclient.check.dependent_apps' | 0fd60b2e0b500300894181a037673ad6 |
| script_include:GetRelatedLists(100a63e4b7021300897725cbde11a9c3) | table:sys_sg_related_lists_screen | new GlideRecord("sys_sg_related_lists_screen") | 100a63e4b7021300897725cbde11a9c3 |
| script_include:UserHasSubscriptionInMemoryCache(101243fbffa36110468365d7d3b8fe70) | table:user_has_subscription | new GlideRecord('user_has_subscription') | 101243fbffa36110468365d7d3b8fe70 |
| script_include:FMUtils(10421b0bc0a80a6865d83dff7013ba76) | table:fm_ci_rate_card_cmdb_ci_m2m | new GlideRecord("fm_ci_rate_card_cmdb_ci_m2m") | 10421b0bc0a80a6865d83dff7013ba76 |
| script_include:FMUtils(10421b0bc0a80a6865d83dff7013ba76) | table:cmdb_ci | new GlideRecord("cmdb_ci") | 10421b0bc0a80a6865d83dff7013ba76 |
| script_include:FMUtils(10421b0bc0a80a6865d83dff7013ba76) | table:task_ci | new GlideRecord("task_ci") | 10421b0bc0a80a6865d83dff7013ba76 |
| script_include:TimelineGeneratorSchedulePage(10a70a220a0a0b7707666ebc6055267c) | table:cmn_timeline_page | new GlideRecord('cmn_timeline_page') | 10a70a220a0a0b7707666ebc6055267c |
| script_include:TimelineGeneratorSchedulePage(10a70a220a0a0b7707666ebc6055267c) | table:cmn_timeline_sub_item | new GlideRecord('cmn_timeline_sub_item') | 10a70a220a0a0b7707666ebc6055267c |
| script_include:TaskSLA(10d0c7590a0a2c394e2b1766a6e5fbad) | table:task_sla | new GlideRecord('task_sla') | 10d0c7590a0a2c394e2b1766a6e5fbad |
| script_include:TaskSLA(10d0c7590a0a2c394e2b1766a6e5fbad) | table:task | new GlideRecord('task') | 10d0c7590a0a2c394e2b1766a6e5fbad |
| script_include:TaskSLA(10d0c7590a0a2c394e2b1766a6e5fbad) | table:cmn_schedule | new GlideRecord('cmn_schedule') | 10d0c7590a0a2c394e2b1766a6e5fbad |
| script_include:TaskSLA(10d0c7590a0a2c394e2b1766a6e5fbad) | table:contract_sla | new GlideRecord("contract_sla") | 10d0c7590a0a2c394e2b1766a6e5fbad |
| script_include:TaskSLA(10d0c7590a0a2c394e2b1766a6e5fbad) | table:sys_trigger | new GlideRecord('sys_trigger') | 10d0c7590a0a2c394e2b1766a6e5fbad |
| script_include:ImportedEntitlementDataProcessAction(11358c9aff3512103611ffffffffff58) | table:sys_attachment | new GlideRecord("sys_attachment") | 11358c9aff3512103611ffffffffff58 |
| script_include:QuestionnaireDaoSNC(114964765375521084d6ddeeff7b1277) | table:asmt_metric_type | new GlideRecord('asmt_metric_type') | 114964765375521084d6ddeeff7b1277 |
| script_include:QuestionnaireDaoSNC(114964765375521084d6ddeeff7b1277) | table:asmt_assessment_instance | new GlideRecord("asmt_assessment_instance") | 114964765375521084d6ddeeff7b1277 |
| script_include:CMDBWorkspaceUtil(114ce4a553a720102365ddeeff7b122a) | table:sn_cmdb_ws_config_identifier | new GlideRecord('sn_cmdb_ws_config_identifier') | 114ce4a553a720102365ddeeff7b122a |
| script_include:TimelineParentReferenceFields(11abe222ff321000dadaefff0efe1ef0) | table:cmn_timeline_page | new GlideRecord("cmn_timeline_page") | 11abe222ff321000dadaefff0efe1ef0 |
| script_include:RelatedListChoice(11bfdfd1b3430300f7d1a13816a8dcef) | table:sys_ui_policy | new GlideRecord('sys_ui_policy') | 11bfdfd1b3430300f7d1a13816a8dcef |
| script_include:NotificationUnsubscribe(11d170917f0312005f58108c3ffa9118) | table:sysevent_email_action | new GlideRecord('sysevent_email_action') | 11d170917f0312005f58108c3ffa9118 |
| script_include:NotificationUnsubscribe(11d170917f0312005f58108c3ffa9118) | table:sys_notif_subscription | new GlideRecord('sys_notif_subscription') | 11d170917f0312005f58108c3ffa9118 |
| script_include:NotificationUnsubscribe(11d170917f0312005f58108c3ffa9118) | table:cmn_notif_device | new GlideRecord('cmn_notif_device') | 11d170917f0312005f58108c3ffa9118 |
| script_include:NotificationUnsubscribe(11d170917f0312005f58108c3ffa9118) | table:cmn_notif_message | new GlideRecord('cmn_notif_message') | 11d170917f0312005f58108c3ffa9118 |
| script_include:NotificationUnsubscribe(11d170917f0312005f58108c3ffa9118) | table:cmn_notif_device | new GlideRecord("cmn_notif_device") | 11d170917f0312005f58108c3ffa9118 |
| script_include:ExperimentationInstanceTypeChange(11d5fc0943302210d33f9c0d7ab8f219) | table:experimentation_executor_client_staging | new GlideRecord('experimentation_executor_client_staging') | 11d5fc0943302210d33f9c0d7ab8f219 |
| script_include:ExperimentationInstanceTypeChange(11d5fc0943302210d33f9c0d7ab8f219) | table:cds_client_schedule | new GlideRecord('cds_client_schedule') | 11d5fc0943302210d33f9c0d7ab8f219 |
| script_include:SMConfigUtil(11df67ee77b230109743dffecf5a99a4) | table:sm_config | new GlideRecord('sm_config') | 11df67ee77b230109743dffecf5a99a4 |
| script_include:VAFaqUtil(122926cec353101050294f877840ddac) | table:kb_template_faq | new GlideRecord('kb_template_faq') | 122926cec353101050294f877840ddac |
| script_include:LookupVerifyGenUtil(123fd398534310102c30ddeeff7b12cc) | table:interaction_related_record | new GlideRecord("interaction_related_record") | 123fd398534310102c30ddeeff7b12cc |
| script_include:LookupVerifyGenUtil(123fd398534310102c30ddeeff7b12cc) | table:interaction_related_record | new GlideRecord('interaction_related_record') | 123fd398534310102c30ddeeff7b12cc |
| script_include:ATFClientUtil(126e1b9d0f77230091d0f00c97767ef3) | table:v_atf_mutually_exclusive_test | new GlideRecord("v_atf_mutually_exclusive_test") | 126e1b9d0f77230091d0f00c97767ef3 |
| script_include:ATFClientUtil(126e1b9d0f77230091d0f00c97767ef3) | table:sys_atf_mutual_exclusion_rule | new GlideRecord("sys_atf_mutual_exclusion_rule") | 126e1b9d0f77230091d0f00c97767ef3 |
| script_include:ATFClientUtil(126e1b9d0f77230091d0f00c97767ef3) | table:sys_atf_test_result | new GlideRecord("sys_atf_test_result") | 126e1b9d0f77230091d0f00c97767ef3 |
| script_include:ATFClientUtil(126e1b9d0f77230091d0f00c97767ef3) | table:sys_atf_test | new GlideRecord("sys_atf_test") | 126e1b9d0f77230091d0f00c97767ef3 |
| script_include:ATFClientUtil(126e1b9d0f77230091d0f00c97767ef3) | table:sys_ui_action | new GlideRecord('sys_ui_action') | 126e1b9d0f77230091d0f00c97767ef3 |
| script_include:ATFClientUtil(126e1b9d0f77230091d0f00c97767ef3) | table:sys_atf_test_suite | new GlideRecord("sys_atf_test_suite") | 126e1b9d0f77230091d0f00c97767ef3 |
| script_include:LoggerUtil(12b52e547f2012103605910e9c866530) | table:licensing_error | new GlideRecord('licensing_error') | 12b52e547f2012103605910e9c866530 |
| script_include:SystemCloneUtil(12cfefda3b231010aaec0896c3efc4ac) | table:sys_db_view | new GlideRecord("sys_db_view") | 12cfefda3b231010aaec0896c3efc4ac |
| script_include:SystemCloneUtil(12cfefda3b231010aaec0896c3efc4ac) | table:sys_security_acl | new GlideRecord('sys_security_acl') | 12cfefda3b231010aaec0896c3efc4ac |
| script_include:SNHelpSetupUtil(130600a4773230106ee492b01e5a99f6) | table:help_content | new GlideRecord("help_content") | 130600a4773230106ee492b01e5a99f6 |
| script_include:AjaxUserRateTypeSetting(131ad57cc7723200a56442808e9763ff) | table:time_card | new GlideRecord('time_card') | 131ad57cc7723200a56442808e9763ff |
| script_include:DictionaryUserFields(13268625732023004a905ee515f6a706) | table:sys_dictionary | new GlideRecord("sys_dictionary") | 13268625732023004a905ee515f6a706 |
| script_include:SamModelLifecycleToProductLifecycle(132dcb310f331010a2bb13b2ff767e8f) | table:sam_custom_sw_product_lifecycle | new GlideRecord('sam_custom_sw_product_lifecycle') | 132dcb310f331010a2bb13b2ff767e8f |
| script_include:SamModelLifecycleToProductLifecycle(132dcb310f331010a2bb13b2ff767e8f) | table:sys_choice | new GlideRecord('sys_choice') | 132dcb310f331010a2bb13b2ff767e8f |
| script_include:SamModelLifecycleToProductLifecycle(132dcb310f331010a2bb13b2ff767e8f) | table:sam_sw_model_lifecycle | new GlideRecord('sam_sw_model_lifecycle') | 132dcb310f331010a2bb13b2ff767e8f |
| script_include:DiffHelper(133f0620370010008687ddb1967334e0) | table:sys_update_xml | new GlideRecord("sys_update_xml") | 133f0620370010008687ddb1967334e0 |
| script_include:DiffHelper(133f0620370010008687ddb1967334e0) | table:sys_update_diff | new GlideRecord("sys_update_diff") | 133f0620370010008687ddb1967334e0 |
| script_include:DiffHelper(133f0620370010008687ddb1967334e0) | table:sys_update_version | new GlideRecord('sys_update_version') | 133f0620370010008687ddb1967334e0 |
| script_include:AppManagerFiltersUtil(136e8d7a8767d5105045b9d8dabb3519) | table:sn_appclient_product | new GlideRecord('sn_appclient_product') | 136e8d7a8767d5105045b9d8dabb3519 |
| script_include:AppManagerFiltersUtil(136e8d7a8767d5105045b9d8dabb3519) | table:sn_admin_center_business_objective | new GlideRecord('sn_admin_center_business_objective') | 136e8d7a8767d5105045b9d8dabb3519 |
| script_include:AppManagerFiltersUtil(136e8d7a8767d5105045b9d8dabb3519) | table:sn_admin_center_solution | new GlideRecord('sn_admin_center_solution') | 136e8d7a8767d5105045b9d8dabb3519 |
| script_include:AppManagerFiltersUtil(136e8d7a8767d5105045b9d8dabb3519) | table:sn_admin_center_application | new GlideRecord('sn_admin_center_application') | 136e8d7a8767d5105045b9d8dabb3519 |
| script_include:PreferredTableAjaxUtil(1420c1797783511031e3b3c64b5a997d) | table:sys_db_object | new GlideRecord('sys_db_object') | 1420c1797783511031e3b3c64b5a997d |
| script_include:DMPolicyUtil(142370d2ebb331100dba9147c1522845) | table:sys_dm_policy | new GlideRecord('sys_dm_policy') | 142370d2ebb331100dba9147c1522845 |
| script_include:VCenterSensor(1437f6d8c3603000ed4860eb5bba8fad) | table:cmdb_ci_vcenter | new GlideRecord('cmdb_ci_vcenter') | 1437f6d8c3603000ed4860eb5bba8fad |
| script_include:VCenterSensor(1437f6d8c3603000ed4860eb5bba8fad) | table:cmdb_fc_initiator | new GlideRecord('cmdb_fc_initiator') | 1437f6d8c3603000ed4860eb5bba8fad |
| script_include:VCenterSensor(1437f6d8c3603000ed4860eb5bba8fad) | table:cmdb_fc_target | new GlideRecord('cmdb_fc_target') | 1437f6d8c3603000ed4860eb5bba8fad |
| script_include:VCenterSensor(1437f6d8c3603000ed4860eb5bba8fad) | table:cmdb_ci_iscsi_export | new GlideRecord('cmdb_ci_iscsi_export') | 1437f6d8c3603000ed4860eb5bba8fad |
| script_include:VCenterSensor(1437f6d8c3603000ed4860eb5bba8fad) | table:cmdb_model | new GlideRecord('cmdb_model') | 1437f6d8c3603000ed4860eb5bba8fad |
| script_include:VCenterSensor(1437f6d8c3603000ed4860eb5bba8fad) | table:cmdb_ci_vmware_nic | new GlideRecord('cmdb_ci_vmware_nic') | 1437f6d8c3603000ed4860eb5bba8fad |
| script_include:VCenterSensor(1437f6d8c3603000ed4860eb5bba8fad) | table:vmware_folder_type | new GlideRecord('vmware_folder_type') | 1437f6d8c3603000ed4860eb5bba8fad |
| script_include:VCenterSensor(1437f6d8c3603000ed4860eb5bba8fad) | table:vmware_vcenter_folder_type_m2m | new GlideRecord('vmware_vcenter_folder_type_m2m') | 1437f6d8c3603000ed4860eb5bba8fad |
| script_include:VCenterSensor(1437f6d8c3603000ed4860eb5bba8fad) | table:cmdb_ci_esx_resource_pool | new GlideRecord('cmdb_ci_esx_resource_pool') | 1437f6d8c3603000ed4860eb5bba8fad |
| script_include:ConsumerDao(144fbc675352030097a2ddeeff7b1238) | table:sys_user | new GlideRecord("sys_user") | 144fbc675352030097a2ddeeff7b1238 |
| script_include:UserGroup(1451ffdc7f000001015920875da9d1bc) | table:sys_user_group | new GlideRecord('sys_user_group') | 1451ffdc7f000001015920875da9d1bc |
| script_include:AJAXMessagingUtils(1452ad185364101042a9ddeeff7b12b9) | table:interaction | new GlideRecord('interaction') | 1452ad185364101042a9ddeeff7b12b9 |
| script_include:AJAXMessagingUtils(1452ad185364101042a9ddeeff7b12b9) | table:sys_attachment | new GlideRecord('sys_attachment') | 1452ad185364101042a9ddeeff7b12b9 |
| script_include:AJAXMessagingUtils(1452ad185364101042a9ddeeff7b12b9) | table:sys_cs_provider_application | new GlideRecordSecure('sys_cs_provider_application') | 1452ad185364101042a9ddeeff7b12b9 |
| script_include:AJAXMessagingUtils(1452ad185364101042a9ddeeff7b12b9) | table:sys_cs_channel_user_profile | new GlideRecordSecure('sys_cs_channel_user_profile') | 1452ad185364101042a9ddeeff7b12b9 |
| script_include:pwdEnrollmentReminder(14b8bad70b31030031a567bff6673a78) | table:sysauto_script | new GlideRecord("sysauto_script") | 14b8bad70b31030031a567bff6673a78 |
| script_include:pwdEnrollmentReminder(14b8bad70b31030031a567bff6673a78) | table:sysevent_email_action | new GlideRecord("sysevent_email_action") | 14b8bad70b31030031a567bff6673a78 |
| script_include:AiHealthStatus(14fed8967782021054df7f7c8c5a9913) | table:sys_properties | new GlideRecord('sys_properties') | 14fed8967782021054df7f7c8c5a9913 |
| script_include:AiHealthStatus(14fed8967782021054df7f7c8c5a9913) | table:sys_trigger | new GlideRecord('sys_trigger') | 14fed8967782021054df7f7c8c5a9913 |
| script_include:EmailDiagnostics(151a8bce97410100715a390ddd2975c3) | table:sys_email_account | new GlideRecordSecure("sys_email_account") | 151a8bce97410100715a390ddd2975c3 |
| script_include:EmailDiagnostics(151a8bce97410100715a390ddd2975c3) | table:sys_trigger | new GlideRecordSecure("sys_trigger") | 151a8bce97410100715a390ddd2975c3 |
| script_include:EmailDiagnostics(151a8bce97410100715a390ddd2975c3) | table:sys_email | new GlideRecordSecure("sys_email") | 151a8bce97410100715a390ddd2975c3 |
| script_include:CIIdentifierForHelpDesk(151f1e270a0a0b8b2d9cd36e7840dbf8) | table:cmdb_ci_computer | new GlideRecord("cmdb_ci_computer") | 151f1e270a0a0b8b2d9cd36e7840dbf8 |
| script_include:CIIdentifierForHelpDesk(151f1e270a0a0b8b2d9cd36e7840dbf8) | table:cmdb_ci_network_adapter | new GlideRecord("cmdb_ci_network_adapter") | 151f1e270a0a0b8b2d9cd36e7840dbf8 |
| script_include:ArchiveUtil(153c0d139f0120007aaa207c7f4bccbe) | table:sys_archive_log | new GlideRecord('sys_archive_log') | 153c0d139f0120007aaa207c7f4bccbe |
| script_include:FSMMobileUtil(1553fea4235123002ff2cb0a56bf65a3) | table:cmn_location | new GlideRecord("cmn_location") | 1553fea4235123002ff2cb0a56bf65a3 |
| script_include:FSMMobileUtil(1553fea4235123002ff2cb0a56bf65a3) | table:sys_group_covers_location | new GlideRecord("sys_group_covers_location") | 1553fea4235123002ff2cb0a56bf65a3 |
| script_include:FSMMobileUtil(1553fea4235123002ff2cb0a56bf65a3) | table:wm_task | new GlideRecord("wm_task") | 1553fea4235123002ff2cb0a56bf65a3 |
| script_include:FSMMobileUtil(1553fea4235123002ff2cb0a56bf65a3) | table:sys_user_grmember | new GlideRecord("sys_user_grmember") | 1553fea4235123002ff2cb0a56bf65a3 |
| script_include:FSMMobileUtil(1553fea4235123002ff2cb0a56bf65a3) | table:sys_user_group | new GlideRecord("sys_user_group") | 1553fea4235123002ff2cb0a56bf65a3 |
| script_include:FSMMobileUtil(1553fea4235123002ff2cb0a56bf65a3) | table:sm_m2m_group_dependency | new GlideRecord("sm_m2m_group_dependency") | 1553fea4235123002ff2cb0a56bf65a3 |
| script_include:FSMMobileUtil(1553fea4235123002ff2cb0a56bf65a3) | table:alm_transfer_order | new GlideRecord("alm_transfer_order") | 1553fea4235123002ff2cb0a56bf65a3 |
| script_include:FSMMobileUtil(1553fea4235123002ff2cb0a56bf65a3) | table:sm_part_requirement | new GlideRecord("sm_part_requirement") | 1553fea4235123002ff2cb0a56bf65a3 |
| script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d) | table:promin_project_entity | new GlideRecord("promin_project_entity") | 157a3f7b5315301025a7ddeeff7b129d |
| script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d) | table:promin_finding_def | new GlideRecord("promin_finding_def") | 157a3f7b5315301025a7ddeeff7b129d |
| script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d) | table:promin_finding_def_condition | new GlideRecord("promin_finding_def_condition") | 157a3f7b5315301025a7ddeeff7b129d |
| script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d) | table:promin_automated_finding | new GlideRecord("promin_automated_finding") | 157a3f7b5315301025a7ddeeff7b129d |
| script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d) | table:promin_automated_finding_configuration | new GlideRecord("promin_automated_finding_configuration") | 157a3f7b5315301025a7ddeeff7b129d |
| script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d) | table:promin_model_def_version | new GlideRecord('promin_model_def_version') | 157a3f7b5315301025a7ddeeff7b129d |
| script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d) | table:promin_process_def | new GlideRecord("promin_process_def") | 157a3f7b5315301025a7ddeeff7b129d |
| script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d) | table:sys_update_set | new GlideRecord("sys_update_set") | 157a3f7b5315301025a7ddeeff7b129d |
| script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d) | table:ml_word_vector_corpus | new GlideRecord("ml_word_vector_corpus") | 157a3f7b5315301025a7ddeeff7b129d |
| script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d) | table:ml_word_vector_corpus_details | new GlideRecord("ml_word_vector_corpus_details") | 157a3f7b5315301025a7ddeeff7b129d |
| script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d) | table:pa_indicators | new GlideRecord("pa_indicators") | 157a3f7b5315301025a7ddeeff7b129d |
| script_include:ProminUIActionSNC(157a3f7b5315301025a7ddeeff7b129d) | table:sys_metadata_link | new GlideRecord('sys_metadata_link') | 157a3f7b5315301025a7ddeeff7b129d |
| script_include:DispatcherWorkspaceResourceUtilSNC(15b687dcc3d40210d890587c1f40ddfd) | table:sys_user | new GlideRecord("sys_user") | 15b687dcc3d40210d890587c1f40ddfd |
| script_include:DispatcherWorkspaceResourceUtilSNC(15b687dcc3d40210d890587c1f40ddfd) | table:wm_crew | new GlideRecord("wm_crew") | 15b687dcc3d40210d890587c1f40ddfd |
| script_include:DispatcherWorkspaceResourceUtilSNC(15b687dcc3d40210d890587c1f40ddfd) | table:sm_m2m_group_dependency | new GlideRecord("sm_m2m_group_dependency") | 15b687dcc3d40210d890587c1f40ddfd |
| script_include:DispatcherWorkspaceResourceUtilSNC(15b687dcc3d40210d890587c1f40ddfd) | table:wm_crew_group | new GlideRecord("wm_crew_group") | 15b687dcc3d40210d890587c1f40ddfd |
| script_include:CSMPredictionServiceBaseImpl(15cc6424771723002bc4914f581061cb) | table:ml_pa_predicted_output | new GlideRecord("ml_pa_predicted_output") | 15cc6424771723002bc4914f581061cb |
| script_include:CSMPredictionServiceBaseImpl(15cc6424771723002bc4914f581061cb) | table:sys_db_object | new GlideRecord("sys_db_object") | 15cc6424771723002bc4914f581061cb |
| script_include:VariableUtil(15f2285773011300f49d0690fdf6a721) | table:item_option_new_set | new GlideRecord("item_option_new_set") | 15f2285773011300f49d0690fdf6a721 |
| script_include:VariableUtil(15f2285773011300f49d0690fdf6a721) | table:item_option_new | new GlideRecord("item_option_new") | 15f2285773011300f49d0690fdf6a721 |
| script_include:VariableUtil(15f2285773011300f49d0690fdf6a721) | table:sys_attachment | new GlideRecord("sys_attachment") | 15f2285773011300f49d0690fdf6a721 |
| script_include:NAAWWNAUtils(15f3747f93a512104d0a423b928918bc) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 15f3747f93a512104d0a423b928918bc |
| script_include:ChangeRequestStateHandlerAjaxSNC(166f5498cb200200d71cb9c0c24c9c46) | table:change_request | new GlideRecordSecure("change_request") | 166f5498cb200200d71cb9c0c24c9c46 |
| script_include:CatalogItemDiagnosticScore(16a7b092c3330200e44574e1c1d3ae68) | table:item_option_new | new GlideRecord("item_option_new") | 16a7b092c3330200e44574e1c1d3ae68 |
| script_include:ItemViewElementsProvider(16d81d7b73232300b8d77a2f1bf6a73d) | table:sys_sg_item_view | new GlideRecord('sys_sg_item_view') | 16d81d7b73232300b8d77a2f1bf6a73d |
| script_include:DynamicSchedulingResourceUtil(16d9e8765ba53010461b52380a81c772) | table:wm_task | new GlideRecord("wm_task") | 16d9e8765ba53010461b52380a81c772 |
| script_include:SOAPMessageGenerator(170a6cb60a0a0b114776fbaee3d46612) | table:sys_soap_message_import | new GlideRecord("sys_soap_message_import") | 170a6cb60a0a0b114776fbaee3d46612 |
| script_include:SOAPMessageGenerator(170a6cb60a0a0b114776fbaee3d46612) | table:sys_soap_message_function | new GlideRecord("sys_soap_message_function") | 170a6cb60a0a0b114776fbaee3d46612 |
| script_include:SOAPMessageGenerator(170a6cb60a0a0b114776fbaee3d46612) | table:sys_soap_message_parameters | new GlideRecord("sys_soap_message_parameters") | 170a6cb60a0a0b114776fbaee3d46612 |
| script_include:SOAPMessageGenerator(170a6cb60a0a0b114776fbaee3d46612) | table:sys_soap_message_test | new GlideRecord("sys_soap_message_test") | 170a6cb60a0a0b114776fbaee3d46612 |
| script_include:SOAPMessageGenerator(170a6cb60a0a0b114776fbaee3d46612) | table:sys_auth_profile_basic | new GlideRecord('sys_auth_profile_basic') | 170a6cb60a0a0b114776fbaee3d46612 |
| script_include:CodeSearch(1717eb60d7120200b6bddb0c825203da) | table:sn_codesearch_search_group | new GlideRecord('sn_codesearch_search_group') | 1717eb60d7120200b6bddb0c825203da |
| script_include:CodeSearch(1717eb60d7120200b6bddb0c825203da) | table:sn_codesearch_table | new GlideRecord('sn_codesearch_table') | 1717eb60d7120200b6bddb0c825203da |
| script_include:CodeSearch(1717eb60d7120200b6bddb0c825203da) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 1717eb60d7120200b6bddb0c825203da |
| script_include:PwdVerifyPersonalDataProcessor(171a3771eb1101004d7763fba206fea1) | table:sys_dictionary | new GlideRecord("sys_dictionary") | 171a3771eb1101004d7763fba206fea1 |
| script_include:SnFollowUtil(179a1c38a32502102b6a1d1fd31e61d5) | table:live_group_member | new GlideRecord("live_group_member") | 179a1c38a32502102b6a1d1fd31e61d5 |
| script_include:MultiSSO_DigestedToken(17ba7f531b121100227e5581be0713e2) | table:sys_user | new GlideRecord("sys_user") | 17ba7f531b121100227e5581be0713e2 |
| script_include:AppRegistrationUtils(17cb63077f5012103ff504866d866545) | table:sys_analytics_bucket | new GlideRecord('sys_analytics_bucket') | 17cb63077f5012103ff504866d866545 |
| script_include:AppRegistrationUtils(17cb63077f5012103ff504866d866545) | table:sys_analytics_app | new GlideRecord('sys_analytics_app') | 17cb63077f5012103ff504866d866545 |
| script_include:View Proposed Change(17f72c8cb75412107691bea0be11a937) | table:task_ci | new GlideRecord('task_ci') | 17f72c8cb75412107691bea0be11a937 |
| script_include:TableInfoService(18398e0e430121102aeb1ca57bb8f21c) | table:sys_db_object | new GlideRecord('sys_db_object') | 18398e0e430121102aeb1ca57bb8f21c |
| script_include:TableInfoService(18398e0e430121102aeb1ca57bb8f21c) | table:ua_custom_table_inventory | new GlideRecord('ua_custom_table_inventory') | 18398e0e430121102aeb1ca57bb8f21c |
| script_include:TableInfoService(18398e0e430121102aeb1ca57bb8f21c) | table:ua_exempted_table_inventory | new GlideRecord('ua_exempted_table_inventory') | 18398e0e430121102aeb1ca57bb8f21c |
| script_include:getLatestUpgradeEvent(1861c7c73b013200956c47b334efc4ba) | table:sys_performance_event | new GlideRecord('sys_performance_event') | 1861c7c73b013200956c47b334efc4ba |
| script_include:FixedAssetUtils(18b1356a37703000158bbfc8bcbe5d65) | table:alm_fixed_assets | new GlideRecord('alm_fixed_assets') | 18b1356a37703000158bbfc8bcbe5d65 |
| script_include:UserGroupDao(18cc5ef2ff302110468365d7d3b8fed3) | table:sys_user_group | new GlideRecord('sys_user_group') | 18cc5ef2ff302110468365d7d3b8fed3 |
| script_include:UserGroupDao(18cc5ef2ff302110468365d7d3b8fed3) | table:sys_group_has_role | new GlideRecord('sys_group_has_role') | 18cc5ef2ff302110468365d7d3b8fed3 |
| script_include:NluPredictOutcomeUtils(18d763a9776921101b53c5ed3c5a9933) | table:sys_cs_message | new GlideRecord("sys_cs_message") | 18d763a9776921101b53c5ed3c5a9933 |
| script_include:NluPredictOutcomeUtils(18d763a9776921101b53c5ed3c5a9933) | table:sys_cs_conversation_task | new GlideRecord("sys_cs_conversation_task") | 18d763a9776921101b53c5ed3c5a9933 |
| script_include:NluPredictOutcomeUtils(18d763a9776921101b53c5ed3c5a9933) | table:open_nlu_predict_intent_feedback | new GlideRecord("open_nlu_predict_intent_feedback") | 18d763a9776921101b53c5ed3c5a9933 |
| script_include:NluPredictOutcomeUtils(18d763a9776921101b53c5ed3c5a9933) | table:sys_ci_analytics | new GlideRecord("sys_ci_analytics") | 18d763a9776921101b53c5ed3c5a9933 |
| client_script:Warning when no destination type enabled(01e7f5925b6610103a9b51d11581c7e8) | script_include:NotificationProviderUtil | new GlideAjax('NotificationProviderUtil') | 01e7f5925b6610103a9b51d11581c7e8 |
| client_script:Mark type read only(024496277372001099792f163cf6a7b8) | script_include:SystemAddressFilterUtil | new GlideAjax('SystemAddressFilterUtil') | 024496277372001099792f163cf6a7b8 |
| client_script:Set file name extn(02aa7cbd7f42310036bfdd620efa9112) | script_include:ExportSetHelper | new GlideAjax('ExportSetHelper') | 02aa7cbd7f42310036bfdd620efa9112 |
| client_script:Zing Workspace Suggestion Limit Message(02df06bb5b044110d9a5ce1a8581c788) | script_include:WorkspaceSearchConfigurationService | new GlideAjax('WorkspaceSearchConfigurationService') | 02df06bb5b044110d9a5ce1a8581c788 |
| client_script:Instance Clone onLoad Script(03976321373120004f6a80f7bcbe5dac) | script_include:InstanceCloneManagerAjax | new GlideAjax('InstanceCloneManagerAjax') | 03976321373120004f6a80f7bcbe5dac |
| client_script:Clear Contract(0486e994bf8201007a6d257b3f073964) | table:ast_contract | new GlideRecord('ast_contract') | 0486e994bf8201007a6d257b3f073964 |
| client_script:Plugin validation for OAuth 2.0 via MID(04d69bf92165c210f877bb611ef21bbc) | script_include:OAuthConsumerSupport | new GlideAjax('OAuthConsumerSupport') | 04d69bf92165c210f877bb611ef21bbc |
| client_script:Public Knowledge Base Info(05dfe44757b01300d873ac71ef94f9f3) | script_include:KBAjax | new GlideAjax('KBAjax') | 05dfe44757b01300d873ac71ef94f9f3 |
| client_script:Diff Skipped Files(06b54c7d0a0a0b65005fe1f86022a7c5) | script_include:DiffAjax | new GlideAjax("DiffAjax") | 06b54c7d0a0a0b65005fe1f86022a7c5 |
| client_script:Validate OAuth Access Token Parent(06df78209f110200cf4696fcc67fcf04) | script_include:OAuthAccessToken | new GlideAjax('OAuthAccessToken') | 06df78209f110200cf4696fcc67fcf04 |
| client_script:Show alert on selecting KB content(07064f905302011050bdddeeff7b12c7) | script_include:TopicTemplateUtilSNC | new GlideAjax('TopicTemplateUtilSNC') | 07064f905302011050bdddeeff7b12c7 |
| client_script:Archive - Load(0743bf430f922010db5e79a7a4767efa) | script_include:NotArchivedTableList | new GlideAjax("NotArchivedTableList") | 0743bf430f922010db5e79a7a4767efa |
| client_script:Set Targets Visibility for Skill Config(07aa785f37ed2210e459a03174924bce) | script_include:UIRuleActionSkillConfigService | new GlideAjax('UIRuleActionSkillConfigService') | 07aa785f37ed2210e459a03174924bce |
| client_script:Verify Group Post Location Change(0810b45637232000158bbfc8bcbe5dc6) | script_include:SMAJAX | new GlideAjax("SMAJAX") | 0810b45637232000158bbfc8bcbe5dc6 |
| client_script:ShowHideAttributesSection(0928753fb35b0300176b051a16a8dc84) | table:connection_attributes | new GlideRecord("connection_attributes") | 0928753fb35b0300176b051a16a8dc84 |
| client_script:OnChange UIAction(093df5f29368501079f4dc2a767ffba4) | script_include:RecordFieldGetter | new GlideAjax('RecordFieldGetter') | 093df5f29368501079f4dc2a767ffba4 |
| client_script:PA Indicator Source - Report source(096747a2d71302008a854251ce610325) | table:sys_report_source | new GlideRecord('sys_report_source') | 096747a2d71302008a854251ce610325 |
| client_script:Hide/Show Participant Field(09c39c4577e23110d381bfa64b5a9962) | script_include:DocumentTemplateAjax | new GlideAjax("DocumentTemplateAjax") | 09c39c4577e23110d381bfa64b5a9962 |
| client_script:Hide word corpus for classification(0a27ec33c36211104da2a2dd8640dd4a) | script_include:FetchWorkflowClassificationCapability | new GlideAjax('FetchWorkflowClassificationCapability') | 0a27ec33c36211104da2a2dd8640dd4a |
| client_script:Invalid Mail Script Extractor(0a435d31ef1211002841f7f775c0fb95) | script_include:EmailNotificationConverter | new GlideAjax('EmailNotificationConverter') | 0a435d31ef1211002841f7f775c0fb95 |
| client_script:Warn on Close/Cancel Without Approval(0a6eec519f0102002920bde8132e70f2) | script_include:StdChangeUtils | new GlideAjax("StdChangeUtils") | 0a6eec519f0102002920bde8132e70f2 |
| client_script:Update filter tables(0a83bd9f7310330081e06502edf6a7f6) | script_include:VTBLaneFilterTable | new GlideAjax('VTBLaneFilterTable') | 0a83bd9f7310330081e06502edf6a7f6 |
| client_script:Set Manufacturer(0ad678a41b303700985ba64fad4bcb3a) | script_include:GetManufacturerFromModel | new GlideAjax('GetManufacturerFromModel') | 0ad678a41b303700985ba64fad4bcb3a |
| client_script:Pre-populate Proposal to Modify(0aee20529f8102002920bde8132e70a7) | script_include:StdChangeUtils | new GlideAjax('StdChangeUtils') | 0aee20529f8102002920bde8132e70a7 |
| client_script:check order of start date and end date(0c2a1f80d7111100ba4a83e80e61032d) | script_include:FSMDateTimeFormatAjax | new GlideAjax("FSMDateTimeFormatAjax") | 0c2a1f80d7111100ba4a83e80e61032d |
| client_script:Fill item view parts on load(0c9488b673232300b8d77a2f1bf6a723) | script_include:ItemViewElementsProvider | new GlideAjax('ItemViewElementsProvider') | 0c9488b673232300b8d77a2f1bf6a723 |
| client_script:MID Unique Logged in User Banner(0cceed1843f70210471d6692e9b8f2ba) | script_include:MIDLoggedInUserRecords | new GlideAjax('MIDLoggedInUserRecords') | 0cceed1843f70210471d6692e9b8f2ba |
| client_script:Ensure Valid Widget ID(0ce9d342d7301200a9addd173e24d406) | table:sp_widget | new GlideRecord("sp_widget") | 0ce9d342d7301200a9addd173e24d406 |
| client_script:Populate Vendor(0db62d94bf8201007a6d257b3f073905) | table:ast_contract | new GlideRecord('ast_contract') | 0db62d94bf8201007a6d257b3f073905 |
| client_script:Update Types(0df9d7bb233f33005912dc1756bf65db) | script_include:ITSMChoiceValuesAJAX | new GlideAjax('ITSMChoiceValuesAJAX') | 0df9d7bb233f33005912dc1756bf65db |
| client_script:Default Source mapping field(0e1784b373d01010e37d71ef64f6a7ab) | script_include:ActivityUtilsAJAX | new GlideAjax("ActivityUtilsAJAX") | 0e1784b373d01010e37d71ef64f6a7ab |
| client_script:Capture content created from help center(1058156177510210a71834357a5a994b) | script_include:SNHelpAnalyticsController | new GlideAjax('SNHelpAnalyticsController') | 1058156177510210a71834357a5a994b |
| client_script:CreateChildIncident(10d1fe0a531332000600e26b88dc34ee) | script_include:IncidentUtils2 | new GlideAjax('IncidentUtils2') | 10d1fe0a531332000600e26b88dc34ee |
| client_script:Empty assigned_to on group change(110ff95ec31103001488b731c1d3ae27) | table:sys_user_grmember | new GlideRecord('sys_user_grmember') | 110ff95ec31103001488b731c1d3ae27 |
| client_script:Hide AuthnRequest Protocol Binding field(1178b3c5871033008f64bd6ec7cb0bd9) | table:sys_properties | new GlideRecord('sys_properties') | 1178b3c5871033008f64bd6ec7cb0bd9 |
| client_script:Update Assigned to (Assign Group change)(119f2528c323210081d7dccdf3d3aee8) | table:sys_user_grmember | new GlideRecord("sys_user_grmember") | 119f2528c323210081d7dccdf3d3aee8 |
| client_script:Update Assigned to (Assign Group change)(119f2528c323210081d7dccdf3d3aee8) | script_include:SMAJAX | new GlideAjax('SMAJAX') | 119f2528c323210081d7dccdf3d3aee8 |
| client_script:Hide word corpus for Workflow Clustering(11faa7fbebe12110e4aaf288b5522884) | script_include:FetchWorkflowClusteringEnabler | new GlideAjax('FetchWorkflowClusteringEnabler') | 11faa7fbebe12110e4aaf288b5522884 |
| client_script:Multi element view previous period(12d726105f903300ed3926e6ee73137f) | script_include:MultiElementSelectionUtil | new GlideAjax('MultiElementSelectionUtil') | 12d726105f903300ed3926e6ee73137f |
| client_script:set table_name(1339a03b0b300300edf02bd237673a6e) | table:pa_cubes | new GlideRecord("pa_cubes") | 1339a03b0b300300edf02bd237673a6e |
| client_script:Get payload field table on change(13b970fe77131010e46abe41a9106116) | script_include:SPSearchResultActions | new GlideAjax('SPSearchResultActions') | 13b970fe77131010e46abe41a9106116 |
| client_script:Refresh Related List field(13c34fa187311200deddb882a2e3ec49) | script_include:LoadRelatedListsOnSelectAjax | new GlideAjax('LoadRelatedListsOnSelectAjax') | 13c34fa187311200deddb882a2e3ec49 |
| client_script:Hide/Show category related list(140eb43a53a611105a1eddeeff7b12c3) | script_include:TodosFilterClientUtil | new GlideAjax('TodosFilterClientUtil') | 140eb43a53a611105a1eddeeff7b12c3 |
| client_script:Validate selected fields(14162fa70b300300edf02bd237673a6f) | script_include:ValidateTextIndexFields | new GlideAjax("ValidateTextIndexFields") | 14162fa70b300300edf02bd237673a6f |
| client_script:Customize select2 for custom UI steps(14563e5373621300ac1560bdfaf6a7d1) | script_include:ATFSnapshotHelper | new GlideAjax('ATFSnapshotHelper') | 14563e5373621300ac1560bdfaf6a7d1 |
| client_script:Ci update(14a94886c320020055d9db1122d3ae0e) | script_include:SMAJAX | new GlideAjax('SMAJAX') | 14a94886c320020055d9db1122d3ae0e |
| client_script:AIS populate field list(15ec30f0c7230010d1cfd9795cc260ec) | script_include:AisConfigurationAjax | new GlideAjax('AisConfigurationAjax') | 15ec30f0c7230010d1cfd9795cc260ec |
| client_script:Hide word corpus for Workflow Clustering(16d8056eebe32110e4aaf288b552289f) | script_include:FetchWorkflowClusteringCapability | new GlideAjax('FetchWorkflowClusteringCapability') | 16d8056eebe32110e4aaf288b552289f |
| client_script:Validate Facet Type onChange(16e033a877746110be280d892c5a995f) | script_include:ValidateFacets | new GlideAjax('ValidateFacets') | 16e033a877746110be280d892c5a995f |
| client_script:Validate Facet Field name onCellEdit(1788ca29c31354509e777d127840dd6a) | script_include:ValidateFacets | new GlideAjax('ValidateFacets') | 1788ca29c31354509e777d127840dd6a |
| client_script:Hide multisource related (software inst)(17909c1273d01010a64ec3ed8ff6a786) | script_include:MultiSourceAjax | new GlideAjax('MultiSourceAjax') | 17909c1273d01010a64ec3ed8ff6a786 |
| client_script:setupValidators(17a7881c37321100f5bf1f23dfbe5d7b) | script_include:WorkflowVersionUtils | new GlideAjax('WorkflowVersionUtils') | 17a7881c37321100f5bf1f23dfbe5d7b |
| client_script:Load Variable Value in Assignments(17b8ea729323020042cf530b547ffbc8) | script_include:LoadVariableAjax | new GlideAjax('LoadVariableAjax') | 17b8ea729323020042cf530b547ffbc8 |
| client_script:Hide word corpus and advanced parameters(1809906253911110a9a8ddeeff7b127b) | script_include:FetchWorkflowRegressionEnabler | new GlideAjax('FetchWorkflowRegressionEnabler') | 1809906253911110a9a8ddeeff7b127b |
| client_script:populate refTable on refColumn change(1864c98c53820110cca8ddeeff7b127a) | script_include:TaskConfigurationClientUtil | new GlideAjax('TaskConfigurationClientUtil') | 1864c98c53820110cca8ddeeff7b127a |
| client_script:Store contact in a session(188e7758c313020095ccd02422d3ae50) | script_include:CSWizardHelper | new GlideAjax('CSWizardHelper') | 188e7758c313020095ccd02422d3ae50 |
| client_script:Dynamic Category Name Change(1916423c533422106da87f1230e5e6c2) | table:sys_scope | new GlideRecord('sys_scope') | 1916423c533422106da87f1230e5e6c2 |
| client_script:Dynamic Category Name Change(1916423c533422106da87f1230e5e6c2) | table:dynamic_namespace | new GlideRecord('dynamic_namespace') | 1916423c533422106da87f1230e5e6c2 |
| client_script:Show app install warning(193174fb7fa012102e0bb76c9c8665b5) | script_include:UpdateSetAjax | new GlideAjax('UpdateSetAjax') | 193174fb7fa012102e0bb76c9c8665b5 |
| client_script:Clear field values and set table value(193ac4f6c3202110de5da585b140ddf9) | script_include:CodeSigningUtil | new GlideAjax('CodeSigningUtil') | 193ac4f6c3202110de5da585b140ddf9 |
| client_script:Column Name Change(1ab9c2620a0a0b1f0122dbaafa6ae037) | table:sys_scope | new GlideRecord('sys_scope') | 1ab9c2620a0a0b1f0122dbaafa6ae037 |
| client_script:Set Model Fields(1acc808e37413000158bbfc8bcbe5d1d) | script_include:AssetUtilsAJAX | new GlideAjax("AssetUtilsAJAX") | 1acc808e37413000158bbfc8bcbe5d1d |
| client_script:Set Wizard Variables(1b3c579a0a0a0b310095daa53914a0f0) | script_include:ExpertPanelVariablesAjax | new GlideAjax("ExpertPanelVariablesAjax") | 1b3c579a0a0a0b310095daa53914a0f0 |
| client_script:Populate Legacy Subfield Options(1b87151a732a10109cc5aa114df6a752) | script_include:GetChoices | new GlideAjax('GetChoices') | 1b87151a732a10109cc5aa114df6a752 |
| client_script:Show Delegate Roles(1c3a098b0a0a0b1f01ebfea88dfe389b) | script_include:DelegateRolesAjax | new GlideAjax('DelegateRolesAjax') | 1c3a098b0a0a0b1f01ebfea88dfe389b |
| client_script:check onsite start(1c63405de8466910f8778dfd704f533d) | script_include:FSMDateTimeFormatAjax | new GlideAjax("FSMDateTimeFormatAjax") | 1c63405de8466910f8778dfd704f533d |
| client_script:Warn about attachments configuration(1cdc5fa8437521102d2bda5e5bb8f250) | script_include:AISAdminMessageUtils | new GlideAjax('AISAdminMessageUtils') | 1cdc5fa8437521102d2bda5e5bb8f250 |
| client_script:ShowDefaultPolicyMsgOnLoad(1d45063c73212010616ca9843cf6a736) | table:sys_authentication_policy | new GlideRecord('sys_authentication_policy') | 1d45063c73212010616ca9843cf6a736 |
| client_script:Display Pending Changes Message(1ddd5b355b6210100977ca225681c7de) | script_include:AisConfigurationAjax | new GlideAjax('AisConfigurationAjax') | 1ddd5b355b6210100977ca225681c7de |
| client_script:Multiple element view  change on type(1def343e53103300ed39ddeeff7b12f5) | script_include:MultiElementSelectionUtil | new GlideAjax('MultiElementSelectionUtil') | 1def343e53103300ed39ddeeff7b12f5 |
| client_script:CSDM - Check for empty assignment_group(1e050d15735f101061b79c0c6df6a7bd) | script_include:CSDMCMDBUtilClient | new GlideAjax('CSDMCMDBUtilClient') | 1e050d15735f101061b79c0c6df6a7bd |
| client_script:Validate Delivery by Date(1eeabd66c32b10007304072a1fba8f66) | script_include:TransferOrderDateTimeAjax | new GlideAjax('TransferOrderDateTimeAjax') | 1eeabd66c32b10007304072a1fba8f66 |
| client_script:Set Column type(1f4ffe83eb321100d4360c505206feb9) | table:sys_glide_object | new GlideRecord('sys_glide_object') | 1f4ffe83eb321100d4360c505206feb9 |
| client_script:Column Label Change(1f5d21d6c3203000bac1addbdfba8fbb) | table:sys_scope | new GlideRecord('sys_scope') | 1f5d21d6c3203000bac1addbdfba8fbb |
| client_script:Validate Scheduled Travel Start(1fe9b65b4773200042bd757f2ede27bf) | script_include:FSMDateTimeFormatAjax | new GlideAjax("FSMDateTimeFormatAjax") | 1fe9b65b4773200042bd757f2ede27bf |
| client_script:Show/Hide Display as time ago field(20a178ea73270010e37d71ef64f6a71b) | script_include:ActivityUtilsAJAX | new GlideAjax("ActivityUtilsAJAX") | 20a178ea73270010e37d71ef64f6a71b |
| client_script:Populate Contract(20ad9261c33231005f76b2c712d3ae00) | table:ast_contract | new GlideRecord("ast_contract") | 20ad9261c33231005f76b2c712d3ae00 |
| client_script:Hide word corpus and advanced parameters(20d01601c37011104da2a2dd8640ddd0) | script_include:FetchWorkflowClassificationEnabler | new GlideAjax('FetchWorkflowClassificationEnabler') | 20d01601c37011104da2a2dd8640ddd0 |
| client_script:Set SG UI Policy Rule table field(20f5ada1b7321300897725cbde11a90e) | script_include:GetUIPolicyTable | new GlideAjax('GetUIPolicyTable') | 20f5ada1b7321300897725cbde11a90e |
| client_script:Check custom adapter properties(21142a60774611100801255a1e5a9925) | script_include:AJAXCustomAdapterPropUtil | new GlideAjax('AJAXCustomAdapterPropUtil') | 21142a60774611100801255a1e5a9925 |
| client_script:SetScreenDataItemTable(21932af3b7211300897725cbde11a9ed) | script_include:GetScreenDataItemTable | new GlideAjax('GetScreenDataItemTable') | 21932af3b7211300897725cbde11a9ed |
| client_script:Recalculate choice related lists(21dcceb073701300ac1560bdfaf6a73f) | script_include:ATFRelatedListUtil | new GlideAjax('ATFRelatedListUtil') | 21dcceb073701300ac1560bdfaf6a73f |
| client_script:CSDM - Check for empty managed_by_group(22078d55735f101061b79c0c6df6a704) | script_include:CSDMCMDBUtilClient | new GlideAjax('CSDMCMDBUtilClient') | 22078d55735f101061b79c0c6df6a704 |
| client_script:Template selected(2480c830d7311100158ba6859e610305) | table:sys_user | new GlideRecord('sys_user') | 2480c830d7311100158ba6859e610305 |
| client_script:Template selected(2480c830d7311100158ba6859e610305) | script_include:SMAJAX | new GlideAjax("SMAJAX") | 2480c830d7311100158ba6859e610305 |
| client_script:Block change breakdown if exist elements(24ae8661d722110048e04ebfae6103b7) | table:pa_widget_elements | new GlideRecord('pa_widget_elements') | 24ae8661d722110048e04ebfae6103b7 |
| client_script:Edit IP access end(24af10ad5302011031b2ddeeff7b1280) | script_include:IPAccessHandler | new GlideAjax('IPAccessHandler') | 24af10ad5302011031b2ddeeff7b1280 |
| client_script:Reference Table Changed(25ab2287c3002200bde4beae82d3ae32) | script_include:ReferenceFilterTableSelection | new GlideAjax('ReferenceFilterTableSelection') | 25ab2287c3002200bde4beae82d3ae32 |
| client_script:Populate slush bucket with new condition(25f02a15c3112110de5da585b140dd11) | script_include:CodeSigningUtil | new GlideAjax('CodeSigningUtil') | 25f02a15c3112110de5da585b140dd11 |
| client_script:Hide heavy access section(268721c61ba1d490985ba64fad4bcb83) | table:cmdb_model | new GlideRecord('cmdb_model') | 268721c61ba1d490985ba64fad4bcb83 |
| client_script:Show/Hide Not Applicable OnChange(26a640a90b012200a914e17696673a27) | script_include:AssessmentUtilsAJAX | new GlideAjax('AssessmentUtilsAJAX') | 26a640a90b012200a914e17696673a27 |
| client_script:Empty assigned_to on group change(273386d1c3a32200b6dcdfdc64d3ae85) | table:sys_user_grmember | new GlideRecord('sys_user_grmember') | 273386d1c3a32200b6dcdfdc64d3ae85 |
| client_script:Enable/Disable icon upload on load(2852d7c2595b3010f8776ff4b4b3e330) | table:taxonomy | new GlideRecord('taxonomy') | 2852d7c2595b3010f8776ff4b4b3e330 |
| client_script:Add query replacement function(28542d32c31031007de15ad8cbba8f27) | script_include:QueryRewriteAjax | new GlideAjax('QueryRewriteAjax') | 28542d32c31031007de15ad8cbba8f27 |
| client_script:Populating Availlability table field(28a5d98b5b203010461b52380a81c755) | script_include:AppointmentConfigurationAjaxUtil | new GlideAjax("AppointmentConfigurationAjaxUtil") | 28a5d98b5b203010461b52380a81c755 |
| client_script:Multi element view set value onLoad(28e3d6b35f443300ed3926e6ee7313cf) | script_include:MultiElementSelectionUtil | new GlideAjax('MultiElementSelectionUtil') | 28e3d6b35f443300ed3926e6ee7313cf |
| client_script:Select template according to capablity(293850d587231300f018f7c736cb0b8e) | table:ml_trainer_definition | new GlideRecord('ml_trainer_definition') | 293850d587231300f018f7c736cb0b8e |
| client_script:Populate source(29e237ebc7311010d1cfd9795cc260cc) | script_include:AisConfigurationAjax | new GlideAjax('AisConfigurationAjax') | 29e237ebc7311010d1cfd9795cc260cc |
| client_script:Schedule Item onLoad(2a4d1a74c0a801660137c5b6cccdd65f) | script_include:TimeSpanScheduler | new GlideAjax("TimeSpanScheduler") | 2a4d1a74c0a801660137c5b6cccdd65f |
| ui_action:Set as default(0073696b93d6220064f572edb67ffb91) | table:time_sheet_policy | new GlideRecord('time_sheet_policy') | 0073696b93d6220064f572edb67ffb91 |
| ui_action:Link Existing(01d0f207b73310109fa9b381de11a9b9) | table:ais_genius_result_configuration | new GlideRecord("ais_genius_result_configuration") | 01d0f207b73310109fa9b381de11a9b9 |
| ui_action:Show warnings(02cbc9386703030091d005225685ef14) | table:sys_atf_test_result_item | new GlideRecord("sys_atf_test_result_item") | 02cbc9386703030091d005225685ef14 |
| ui_action:Preview Script Usage(03028ac107131000dada43c0d1021e28) | table:sys_rest_message_fn | new GlideRecord('sys_rest_message_fn') | 03028ac107131000dada43c0d1021e28 |
| ui_action:Sync rules to MID(035d4d77c72030102f7d69467ec26007) | table:ecc_agent | new GlideRecord("ecc_agent") | 035d4d77c72030102f7d69467ec26007 |
| ui_action:Sync rules to MID(035d4d77c72030102f7d69467ec26007) | table:ecc_queue | new GlideRecord("ecc_queue") | 035d4d77c72030102f7d69467ec26007 |
| ui_action:Drop(035e2e507f331210a358709ebc8665a0) | script_include:ExtendedStatisticsService | new GlideAjax('ExtendedStatisticsService') | 035e2e507f331210a358709ebc8665a0 |
| ui_action:Up Vote(0369fb049f233100fc6cd4b4232e70ad) | table:kb_social_qa_vote | new GlideRecord('kb_social_qa_vote') | 0369fb049f233100fc6cd4b4232e70ad |
| ui_action:New(0425a93fc7723300cff9337bf4c26064) | table:sysrule_view_workspace | new GlideRecord("sysrule_view_workspace") | 0425a93fc7723300cff9337bf4c26064 |
| ui_action:Edit(048625bf53e65010bf6bddeeff7b1240) | table:sys_cs_context_profile | new GlideRecord("sys_cs_context_profile") | 048625bf53e65010bf6bddeeff7b1240 |
| ui_action:Load Demo Data Only(0496b2f1d7300200b0b044580e6103cb) | table:v_plugin | new GlideRecord("v_plugin") | 0496b2f1d7300200b0b044580e6103cb |
| ui_action:Add Shared Parameters(064c1dae77b21300f779d4082b106197) | table:sys_db_object | new GlideRecord("sys_db_object") | 064c1dae77b21300f779d4082b106197 |
| ui_action:Add Shared Parameters(064c1dae77b21300f779d4082b106197) | table:sys_atf_test | new GlideRecord("sys_atf_test") | 064c1dae77b21300f779d4082b106197 |
| ui_action:Delete(06a2304bb7982210cc0b2ed75e11a9e3) | script_include:MIDServerAjax | new GlideAjax("MIDServerAjax") | 06a2304bb7982210cc0b2ed75e11a9e3 |
| ui_action:Delete(06a2304bb7982210cc0b2ed75e11a9e3) | script_include:DeleteRecordAjax | new GlideAjax('DeleteRecordAjax') | 06a2304bb7982210cc0b2ed75e11a9e3 |
| ui_action:New(06e59214d7000200a9ad1e173e24d4ec) | table:sp_container | new GlideRecord("sp_container") | 06e59214d7000200a9ad1e173e24d4ec |
| ui_action:New(06e59214d7000200a9ad1e173e24d4ec) | table:sp_row | new GlideRecord("sp_row") | 06e59214d7000200a9ad1e173e24d4ec |
| ui_action:New(06e59214d7000200a9ad1e173e24d4ec) | table:sp_column | new GlideRecord("sp_column") | 06e59214d7000200a9ad1e173e24d4ec |
| ui_action:Create Incident(076fc61923731300b15f110d96bf65aa) | table:incident | new GlideRecord("incident") | 076fc61923731300b15f110d96bf65aa |
| ui_action:Remove user access from table(0774a1c50b41330000ea069f56673a33) | table:sys_user_has_role | new GlideRecord("sys_user_has_role") | 0774a1c50b41330000ea069f56673a33 |
| ui_action:View Page(07b230820a0a0b12003312a51a02a238) | script_include:CMSAjax | new GlideAjax("CMSAjax") | 07b230820a0a0b12003312a51a02a238 |
| ui_action:Add(08d172a1932231002f217a75e57ffb39) | script_include:AssociateCIToTask | new GlideAjax("AssociateCIToTask") | 08d172a1932231002f217a75e57ffb39 |
| ui_action:Send activity(08d284c0eb23310023c7a9bcf106fe0c) | event:task_activity.message | gs.eventQueue("task_activity.message" | 08d284c0eb23310023c7a9bcf106fe0c |
| ui_action:Send activity(08d284c0eb23310023c7a9bcf106fe0c) | event:task_activity.appointment | gs.eventQueue("task_activity.appointment" | 08d284c0eb23310023c7a9bcf106fe0c |
| ui_action:Clean up invalid elements(08f5fbb7d7213200355683e80e610307) | event:data_cert.cleanup_invalid_cert_element | gs.eventQueue('data_cert.cleanup_invalid_cert_element' | 08f5fbb7d7213200355683e80e610307 |
| ui_action:Show ClusterInsight(091d03bdb7d71010d1dc8b91ee11a911) | script_include:MLAjax | new GlideAjax('MLAjax') | 091d03bdb7d71010d1dc8b91ee11a911 |
| ui_action:Remove Attachment From Target Record(09503b540f3323005605539ac4767e14) | table:sys_attachment | new GlideRecord('sys_attachment') | 09503b540f3323005605539ac4767e14 |
| ui_action:Remove Attachment From Target Record(09503b540f3323005605539ac4767e14) | table:sys_email | new GlideRecord('sys_email') | 09503b540f3323005605539ac4767e14 |
| ui_action:Migrate to IP Filter Criteria(09eee705db1ce010d515a5f74b9619e6) | table:sysauto_script | new GlideRecord("sysauto_script") | 09eee705db1ce010d515a5f74b9619e6 |
| ui_action:Compare Collisions(0a36965247322200a03a19fbac9a7159) | script_include:CompareCollisionAjax | new GlideAjax('CompareCollisionAjax') | 0a36965247322200a03a19fbac9a7159 |
| ui_action:Compare Collisions(0a36965247322200a03a19fbac9a7159) | script_include:DiffMergeUICheck | new GlideAjax('DiffMergeUICheck') | 0a36965247322200a03a19fbac9a7159 |
| ui_action:Show Syslog Records(0bfae0504f013110d7655741b1ce0b62) | table:syslog | new GlideRecord("syslog") | 0bfae0504f013110d7655741b1ce0b62 |
| ui_action:Order(0d3e86a5d7112200d105ef637e6103e1) | script_include:CABMeetingAjax | new GlideAjax("CABMeetingAjax") | 0d3e86a5d7112200d105ef637e6103e1 |
| ui_action:Copy Test(0e385807539500105719ddeeff7b129e) | script_include:ATFClientUtil | new GlideAjax('ATFClientUtil') | 0e385807539500105719ddeeff7b129e |
| ui_action:New(0e80284dc72d3300fc3a2aa9b8c260c8) | script_include:TableExtensionsProcessor | new GlideAjax('TableExtensionsProcessor') | 0e80284dc72d3300fc3a2aa9b8c260c8 |
| ui_action:Create Choice List(0ea094480a0a0b8c005d749c410a739a) | table:sys_choice | new GlideRecord('sys_choice') | 0ea094480a0a0b8c005d749c410a739a |
| ui_action:Create Choice List(0ea094480a0a0b8c005d749c410a739a) | table:sys_dictionary | new GlideRecord('sys_dictionary') | 0ea094480a0a0b8c005d749c410a739a |
| ui_action:Load More Results(0ee1b468732223003d3c63f7fdf6a75e) | script_include:QBBGThreadUtil | new GlideAjax('QBBGThreadUtil') | 0ee1b468732223003d3c63f7fdf6a75e |
| ui_action:Restore Record(0efdf94d9f2120007aaa207c7f4bcc79) | table:sys_archive_log | new GlideRecord('sys_archive_log') | 0efdf94d9f2120007aaa207c7f4bcc79 |
| ui_action:Commit Stash(0f9184e25b201200f1138d5511f91afe) | table:sys_repo_stash | new GlideRecord('sys_repo_stash') | 0f9184e25b201200f1138d5511f91afe |
| ui_action:Unload Dashboard (for Dev)(10278db24f02311054a65e8330ce0bd5) | table:par_dashboard_canvas | new GlideRecord('par_dashboard_canvas') | 10278db24f02311054a65e8330ce0bd5 |
| ui_action:Unload Dashboard (for Dev)(10278db24f02311054a65e8330ce0bd5) | table:par_dashboard_widget | new GlideRecord('par_dashboard_widget') | 10278db24f02311054a65e8330ce0bd5 |
| ui_action:Unload Dashboard (for Dev)(10278db24f02311054a65e8330ce0bd5) | table:par_dashboard_widget_group | new GlideRecord('par_dashboard_widget_group') | 10278db24f02311054a65e8330ce0bd5 |
| ui_action:Unload Dashboard (for Dev)(10278db24f02311054a65e8330ce0bd5) | table:par_dashboard_widget_group_mapping | new GlideRecord('par_dashboard_widget_group_mapping') | 10278db24f02311054a65e8330ce0bd5 |
| ui_action:Unload Dashboard (for Dev)(10278db24f02311054a65e8330ce0bd5) | table:par_visualization | new GlideRecord('par_visualization') | 10278db24f02311054a65e8330ce0bd5 |
| ui_action:Unload Dashboard (for Dev)(10278db24f02311054a65e8330ce0bd5) | table:par_component | new GlideRecord('par_component') | 10278db24f02311054a65e8330ce0bd5 |
| ui_action:Unload Dashboard (for Dev)(10278db24f02311054a65e8330ce0bd5) | table:par_visualization_permission | new GlideRecord('par_visualization_permission') | 10278db24f02311054a65e8330ce0bd5 |
| ui_action:Unload Dashboard (for Dev)(10278db24f02311054a65e8330ce0bd5) | table:par_component_filter_permission | new GlideRecord('par_component_filter_permission') | 10278db24f02311054a65e8330ce0bd5 |
| ui_action:Unload Dashboard (for Dev)(10278db24f02311054a65e8330ce0bd5) | table:analytics_category_m2m | new GlideRecord('analytics_category_m2m') | 10278db24f02311054a65e8330ce0bd5 |
| ui_action:Unload Dashboard (for Dev)(10278db24f02311054a65e8330ce0bd5) | table:analytics_category | new GlideRecord('analytics_category') | 10278db24f02311054a65e8330ce0bd5 |
| ui_action:View Service CIs(108e26a393113100120074aff67ffba0) | table:cmdb_ci_query_based_service | new GlideRecord('cmdb_ci_query_based_service') | 108e26a393113100120074aff67ffba0 |
| ui_action:New(119f024ad7711100158ba6859e6103fc) | table:asmt_metric_category | new GlideRecord('asmt_metric_category') | 119f024ad7711100158ba6859e6103fc |
| ui_action:Associate Record(11e322a9a71213002ae97dd218790166) | table:interaction_related_record | new GlideRecord("interaction_related_record") | 11e322a9a71213002ae97dd218790166 |
| ui_action:Update report source(13186ae3bf1302008a85d64f6c07391f) | table:sys_report_source | new GlideRecord('sys_report_source') | 13186ae3bf1302008a85d64f6c07391f |
| ui_action:Show Flow engine context(13568ad1c75d5010edc3620927c26087) | table:sys_flow_context | new GlideRecord('sys_flow_context') | 13568ad1c75d5010edc3620927c26087 |
| ui_action:New(146c8cbf7320201002ef7a2f1bf6a74f) | script_include:TableExtensionsProcessor | new GlideAjax('TableExtensionsProcessor') | 146c8cbf7320201002ef7a2f1bf6a74f |
| ui_action:Execute Software License Manager(14c11b520a0a0b8b10d5be1fe42951e6) | table:sys_trigger | new GlideRecord("sys_trigger") | 14c11b520a0a0b8b10d5be1fe42951e6 |
| ui_action:Merge Tags(150dcac3ff952100d4beffffffffff9f) | script_include:LabelMergeAjax | new GlideAjax("LabelMergeAjax") | 150dcac3ff952100d4beffffffffff9f |
| ui_action:Show SLA Timeline(15ebb274cbd11200dff9b9c0c24c9c6b) | table:task_sla | new GlideRecord("task_sla") | 15ebb274cbd11200dff9b9c0c24c9c6b |
| ui_action:Nudge Flows(162b9e17372331106dbf963174924be5) | table:sys_flow_context | new GlideRecord('sys_flow_context') | 162b9e17372331106dbf963174924be5 |
| ui_action:Transform(168486120a0a0b800000a5899766f78d) | table:sys_robust_import_set_transformer | new GlideRecord('sys_robust_import_set_transformer') | 168486120a0a0b800000a5899766f78d |
| ui_action:Transform(168486120a0a0b800000a5899766f78d) | table:sys_transform_map | new GlideRecord("sys_transform_map") | 168486120a0a0b800000a5899766f78d |
| ui_action:Source(174cf6c0df021100dca6a5f59bf26323) | script_include:WMSourcingAjax | new GlideAjax('WMSourcingAjax') | 174cf6c0df021100dca6a5f59bf26323 |
| ui_action:Resolve Conflicts(175612e00f2200104202c6b1df767e0c) | script_include:UpgradeHistoryTaskUtil | new GlideAjax("UpgradeHistoryTaskUtil") | 175612e00f2200104202c6b1df767e0c |
| ui_action:Resolve Conflicts(175612e00f2200104202c6b1df767e0c) | script_include:UpgradeCenterGCFAnalyticsAjax | new GlideAjax("UpgradeCenterGCFAnalyticsAjax") | 175612e00f2200104202c6b1df767e0c |
| ui_action:Compare with local(17794300bf110100421cdc2ecf0739f3) | script_include:DiffAjax | new GlideAjax("DiffAjax") | 17794300bf110100421cdc2ecf0739f3 |
| ui_action:Compare with local(17794300bf110100421cdc2ecf0739f3) | script_include:DiffMergeUICheck | new GlideAjax('DiffMergeUICheck') | 17794300bf110100421cdc2ecf0739f3 |
| ui_action:New Classic Mobile Module(17e85601bf230100421cdc2ecf073939) | table:sys_ui_application | new GlideRecord('sys_ui_application') | 17e85601bf230100421cdc2ecf073939 |
| ui_action:New Classic Mobile Module(17e85601bf230100421cdc2ecf073939) | table:sys_choice | new GlideRecord('sys_choice') | 17e85601bf230100421cdc2ecf073939 |
| ui_action:Delete(1815f3a1d7310100fceaa6859e61032d) | script_include:DeleteRecordAjax | new GlideAjax('DeleteRecordAjax') | 1815f3a1d7310100fceaa6859e61032d |
| ui_action:Disable Account Recovery(1987e257c32d2010559d74c3e540ddfd) | table:acr_user | GlideRecord('acr_user') | 1987e257c32d2010559d74c3e540ddfd |
| ui_action:Install(19c11d635b30111047ae122b1d81c74f) | script_include:UpgradePlanProcessor | new GlideAjax('UpgradePlanProcessor') | 19c11d635b30111047ae122b1d81c74f |
| ui_action:Edit detail in UI Builder(1aa697ba10f29110f877cb8bae2edf6e) | script_include:GuidancePreviewExpUtil | new GlideAjax('GuidancePreviewExpUtil') | 1aa697ba10f29110f877cb8bae2edf6e |
| ui_action:Copy(1abf11dc0a0a0b1500e82d9eac8172db) | table:sys_transform_entry | new GlideRecord('sys_transform_entry') | 1abf11dc0a0a0b1500e82d9eac8172db |
| ui_action:Rollback Batch(1b014e165b22101057b20f87df81c79a) | script_include:BatchRollbackHelper | new GlideAjax('BatchRollbackHelper') | 1b014e165b22101057b20f87df81c79a |
| ui_action:Add/Remove Breakpoint(1bc3a93473222010fe5311d8faf6a729) | table:atf_breakpoint | new GlideRecord("atf_breakpoint") | 1bc3a93473222010fe5311d8faf6a729 |
| ui_action:Delete(1c9a6ab0d71112004cd2a3b20e6103e9) | script_include:DeleteRecordAjax | new GlideAjax('DeleteRecordAjax') | 1c9a6ab0d71112004cd2a3b20e6103e9 |
| ui_action:Edit in Catalog Builder(1d0a149173231010ae42d31ee2f6a70d) | script_include:ServiceCatalogVersioningUtils | new GlideAjax('ServiceCatalogVersioningUtils') | 1d0a149173231010ae42d31ee2f6a70d |
| ui_action:Cancel(1df7812d3b323200956c47b334efc405) | table:ml_solution | new GlideRecord('ml_solution') | 1df7812d3b323200956c47b334efc405 |
| ui_action:Close Complete(1e9adef31b03200050fdfbcd2c071356) | script_include:GeolocationAJAX | new GlideAjax('GeolocationAJAX') | 1e9adef31b03200050fdfbcd2c071356 |
| ui_action:Email Vas Desk(1eb2b1c61b783b00985ba64fad4bcb55) | event:email_vas_desk | gs.eventQueue('email_vas_desk' | 1eb2b1c61b783b00985ba64fad4bcb55 |
| ui_action:Delete(1f12506f7f532200348ef0d8adfa9139) | script_include:DeleteRecordAjax | new GlideAjax('DeleteRecordAjax') | 1f12506f7f532200348ef0d8adfa9139 |
| ui_action:Repair non-english sys_choice records(1ffcd8fbeb990110cf2dcd016d52283d) | script_include:I18NChoiceTool | new GlideAjax('I18NChoiceTool') | 1ffcd8fbeb990110cf2dcd016d52283d |
| ui_action:Reapply Changes(212f90a40a0a0b2500bb633c2cf3e69a) | table:sys_update_xml | new GlideRecord("sys_update_xml") | 212f90a40a0a0b2500bb633c2cf3e69a |
| ui_action:Clone(22518ad2c7432010fedf0bcbe2c2600f) | script_include:TopicList | new GlideAjax('TopicList') | 22518ad2c7432010fedf0bcbe2c2600f |
| ui_action:Repeat Table Check(22d5fa1207030000be32a04ff1021e49) | table:ha_table_check | new GlideRecord('ha_table_check') | 22d5fa1207030000be32a04ff1021e49 |
| ui_action:Insert with Actions(22ee7c43c0a80a685c66d9a427b2facf) | table:sys_ui_policy_action | new GlideRecord('sys_ui_policy_action') | 22ee7c43c0a80a685c66d9a427b2facf |
| ui_action:Create and Link(235373585b7d1010d9a5ce1a8581c7af) | table:ais_search_profile_ais_dictionary_m2m | new GlideRecord('ais_search_profile_ais_dictionary_m2m') | 235373585b7d1010d9a5ce1a8581c7af |
| ui_action:Create and Link(235373585b7d1010d9a5ce1a8581c7af) | table:ais_search_profile | new GlideRecord('ais_search_profile') | 235373585b7d1010d9a5ce1a8581c7af |
| ui_action:Create and Link(235373585b7d1010d9a5ce1a8581c7af) | table:ais_search_profile | new GlideRecord("ais_search_profile") | 235373585b7d1010d9a5ce1a8581c7af |
| ui_action:Remove Destroy Rule(23706c67433231107a67e33c4ab8f275) | table:sys_archive | new GlideRecord('sys_archive') | 23706c67433231107a67e33c4ab8f275 |
| ui_action:Remove Destroy Rule(23706c67433231107a67e33c4ab8f275) | table:sys_archive_destroy | new GlideRecord('sys_archive_destroy') | 23706c67433231107a67e33c4ab8f275 |
| ui_action:Run Fix Script(239f93e187333200bb9b61fb97cb0b64) | table:sys_script_fix | new GlideRecord('sys_script_fix') | 239f93e187333200bb9b61fb97cb0b64 |
| ui_action:Export(23b6dfd0730011104fcb066a4cf6a7ab) | script_include:UpgradePlanProcessor | new GlideAjax('UpgradePlanProcessor') | 23b6dfd0730011104fcb066a4cf6a7ab |
| ui_action:Start Travel(23dadef31b03200050fdfbcd2c0713b4) | script_include:FSMAjaxUtil | new GlideAjax("FSMAjaxUtil") | 23dadef31b03200050fdfbcd2c0713b4 |
| ui_action:Start Travel(23dadef31b03200050fdfbcd2c0713b4) | script_include:GeolocationAJAX | new GlideAjax('GeolocationAJAX') | 23dadef31b03200050fdfbcd2c0713b4 |
| ui_action:Add all errors to ignored list(243115156740130091d005225685ef92) | table:sys_atf_test_result_item | new GlideRecord("sys_atf_test_result_item") | 243115156740130091d005225685ef92 |
| ui_action:Add all errors to ignored list(243115156740130091d005225685ef92) | table:sys_atf_whitelist | new GlideRecord('sys_atf_whitelist') | 243115156740130091d005225685ef92 |
| ui_action:Run Again (Debug)(246083ea8f783200a5760b5437bdee31) | table:sys_attachment | new GlideRecord('sys_attachment') | 246083ea8f783200a5760b5437bdee31 |
| ui_action:Run Again (Debug)(246083ea8f783200a5760b5437bdee31) | table:discovery_status | new GlideRecord('discovery_status') | 246083ea8f783200a5760b5437bdee31 |
| ui_action:Run Again (Debug)(246083ea8f783200a5760b5437bdee31) | table:cmdb_ci | new GlideRecord('cmdb_ci') | 246083ea8f783200a5760b5437bdee31 |
| ui_action:Run Again (Debug)(246083ea8f783200a5760b5437bdee31) | table:discovery_classifier_probe | new GlideRecord('discovery_classifier_probe') | 246083ea8f783200a5760b5437bdee31 |
| ui_action:Run Again (Debug)(246083ea8f783200a5760b5437bdee31) | table:discovery_sensor_probe | new GlideRecord('discovery_sensor_probe') | 246083ea8f783200a5760b5437bdee31 |
| ui_action:Delete(24fdbe697310101045cadfcd3bf6a7a7) | script_include:CSDMClientHelper | new GlideAjax('CSDMClientHelper') | 24fdbe697310101045cadfcd3bf6a7a7 |
| ui_action:Delete(24fdbe697310101045cadfcd3bf6a7a7) | script_include:DeleteRecordAjax | new GlideAjax('DeleteRecordAjax') | 24fdbe697310101045cadfcd3bf6a7a7 |
| ui_action:Add all client errors to ignored list(253cece56787030091d005225685ef95) | table:sys_atf_test_result_item | new GlideRecord("sys_atf_test_result_item") | 253cece56787030091d005225685ef95 |
| ui_action:Add all client errors to ignored list(253cece56787030091d005225685ef95) | table:sys_atf_whitelist | new GlideRecord('sys_atf_whitelist') | 253cece56787030091d005225685ef95 |
| ui_action:Apply Consent Policy to All Countries(25600b8e771021105679bcc8ca5a9912) | table:sys_analytics_consent_policy | new GlideRecord("sys_analytics_consent_policy") | 25600b8e771021105679bcc8ca5a9912 |
| ui_action:Up Vote(256f8b109f233100fc6cd4b4232e708e) | table:kb_social_qa_vote | new GlideRecord('kb_social_qa_vote') | 256f8b109f233100fc6cd4b4232e708e |
| ui_action:Get OAuth Token(25e84773b30b3200176b051a16a8dc95) | script_include:OAuthConsumerSupport | new GlideAjax('OAuthConsumerSupport') | 25e84773b30b3200176b051a16a8dc95 |
| ui_action:Link Existing(2623794b536020108271ddeeff7b127a) | table:sys_ux_composite_data_template_predicate | new GlideRecord("sys_ux_composite_data_template_predicate") | 2623794b536020108271ddeeff7b127a |
| ui_action:Deactivate Policy(267f85be532d3010a4d9ddeeff7b12d3) | table:sys_authentication_policy | new GlideRecord("sys_authentication_policy") | 267f85be532d3010a4d9ddeeff7b12d3 |
| ui_action:Go to definition(270b9ef7b3130300f7d1a13816a8dce7) | table:sys_extension_point | new GlideRecord("sys_extension_point") | 270b9ef7b3130300f7d1a13816a8dce7 |
| ui_action:Show SLA Timeline(271c3ead930002002c68530b547ffb08) | table:task_sla | new GlideRecord("task_sla") | 271c3ead930002002c68530b547ffb08 |
| ui_action:Revert(276400c90a00017100d9ddb0650afda8) | table:sys_update_xml | new GlideRecord("sys_update_xml") | 276400c90a00017100d9ddb0650afda8 |
| ui_action:Create and Link(27e3ebdf53e020108271ddeeff7b1214) | table:sys_ux_composite_data | new GlideRecord("sys_ux_composite_data") | 27e3ebdf53e020108271ddeeff7b1214 |
| ui_action:View Scorecard(283682c1d7110100fceaa6859e6103ab) | table:sys_db_object | new GlideRecord("sys_db_object") | 283682c1d7110100fceaa6859e6103ab |
| ui_action:Drop Off(287d701487e42110e4d510683cbb3586) | table:alm_transfer_order_line_task | new GlideRecord("alm_transfer_order_line_task") | 287d701487e42110e4d510683cbb3586 |
| ui_action:Save(289389d2d701310013ab49547e6103ea) | table:kb_knowledge_base | new GlideRecord("kb_knowledge_base") | 289389d2d701310013ab49547e6103ea |
| ui_action:Manually Exempt Table(295c7331779601109650350bee5a99c3) | table:sys_custom_db_object | new GlideRecord('sys_custom_db_object') | 295c7331779601109650350bee5a99c3 |
| ui_action:Show Table(297df363bf1320001875647fcf073906) | table:sys_db_object | new GlideRecord("sys_db_object") | 297df363bf1320001875647fcf073906 |
| ui_action:Reset Completion Records(29afbba65f4201109fa9067660731334) | table:sn_aisearch_global_job_completion | new GlideRecord('sn_aisearch_global_job_completion') | 29afbba65f4201109fa9067660731334 |
| ui_action:Create Case(29c3a377736013001923054dfff6a7e0) | table:sn_customerservice_case | new GlideRecord("sn_customerservice_case") | 29c3a377736013001923054dfff6a7e0 |
| ui_action:Analyze Discovery Performance(29f2fbef93308300f4e3705bb47ffb82) | table:ecc_queue | new GlideRecord('ecc_queue') | 29f2fbef93308300f4e3705bb47ffb82 |
| ui_action:Analyze Discovery Performance(29f2fbef93308300f4e3705bb47ffb82) | table:sys_attachment | new GlideRecord('sys_attachment') | 29f2fbef93308300f4e3705bb47ffb82 |
| ui_action:Create Application Template(2af061eb0f7010108c9c5019c4767e7c) | script_include:PayloadScannerAJAX | new GlideAjax('PayloadScannerAJAX') | 2af061eb0f7010108c9c5019c4767e7c |
| ui_action:Remove Manual Table Exemption(2baf73f1779601109650350bee5a99b4) | table:ua_exempted_table_inventory | new GlideRecord('ua_exempted_table_inventory') | 2baf73f1779601109650350bee5a99b4 |
| ui_action:Add(2bd010c8877b13005087af1e36cb0b8f) | script_include:BulkAddChangeRequest | new GlideAjax("BulkAddChangeRequest") | 2bd010c8877b13005087af1e36cb0b8f |
| ui_action:Publish(2c0e8e4553230010bca8ddeeff7b12c3) | table:ais_dictionary_term | new GlideRecord('ais_dictionary_term') | 2c0e8e4553230010bca8ddeeff7b12c3 |
| ui_action:Delete(2c2943431f001000dada97c0ed8b70a5) | script_include:DeleteUpdateSetEntryAjax | new GlideAjax('DeleteUpdateSetEntryAjax') | 2c2943431f001000dada97c0ed8b70a5 |
| ui_action:Delete(2cf8f802c30031001c13587981d3ae62) | table:sa_m2m_service_entry_point | new GlideRecord('sa_m2m_service_entry_point') | 2cf8f802c30031001c13587981d3ae62 |
| ui_action:Add Mutual Exclusion(2d31fc5b0fe3230091d0f00c97767e66) | script_include:ATFClientUtil | new GlideAjax("ATFClientUtil") | 2d31fc5b0fe3230091d0f00c97767e66 |
| ui_action:New(2f1a8302bf3121000ba9dc2ecf073956) | table:sys_db_object | new GlideRecord("sys_db_object") | 2f1a8302bf3121000ba9dc2ecf073956 |
| ui_action:Generate fields(2fcdefd2ff1001105cf343d0653bf1ee) | table:sys_rte_eb_etl_field | new GlideRecord('sys_rte_eb_etl_field') | 2fcdefd2ff1001105cf343d0653bf1ee |
| ui_action:New(2fda8d08530123004205ddeeff7b128c) | script_include:TableExtensionsProcessor | new GlideAjax('TableExtensionsProcessor') | 2fda8d08530123004205ddeeff7b128c |
| ui_action:Disable Experimentation Framework(2fe8e409932712107b4e5721848918f0) | script_include:ExperimentationFrameworkUtil | new GlideAjax("ExperimentationFrameworkUtil") | 2fe8e409932712107b4e5721848918f0 |
| scheduled_script:Process Geocoding Request(002c1e70eb11020079a62a7ac106fe26) | table:sys_geocoding_request | new GlideRecord("sys_geocoding_request") | 002c1e70eb11020079a62a7ac106fe26 |
| scheduled_script:Update Spoke Operation Activity Logs(00e00e6f53212110094eddeeff7b12b4) | table:sys_ih_spoke_operation_activity_log | new GlideRecord("sys_ih_spoke_operation_activity_log") | 00e00e6f53212110094eddeeff7b12b4 |
| scheduled_script:CMDB Update domain_directory Size(0163c4a653101110456dddeeff7b1217) | table:sys_dictionary | new GlideRecord("sys_dictionary") | 0163c4a653101110456dddeeff7b1217 |
| scheduled_script:Delete Account Records(01a4ee1d1b23d090ee26dd39cd4bcb29) | table:customer_account | new GlideRecord('customer_account') | 01a4ee1d1b23d090ee26dd39cd4bcb29 |
| scheduled_script:Manage duplicated product codes(01ae4e211b6c6090ee26dd39cd4bcb65) | table:cmdb_model | new GlideRecord('cmdb_model') | 01ae4e211b6c6090ee26dd39cd4bcb65 |
| scheduled_script:Manage duplicated product codes(01ae4e211b6c6090ee26dd39cd4bcb65) | table:alm_asset | new GlideRecord("alm_asset") | 01ae4e211b6c6090ee26dd39cd4bcb65 |
| scheduled_script:Manage duplicated product codes(01ae4e211b6c6090ee26dd39cd4bcb65) | table:sm_part_requirement | new GlideRecord("sm_part_requirement") | 01ae4e211b6c6090ee26dd39cd4bcb65 |
| scheduled_script:Manage duplicated product codes(01ae4e211b6c6090ee26dd39cd4bcb65) | table:cmdb_ci | new GlideRecord("cmdb_ci") | 01ae4e211b6c6090ee26dd39cd4bcb65 |
| scheduled_script:Manage duplicated product codes(01ae4e211b6c6090ee26dd39cd4bcb65) | table:cmdb_model | new GlideRecord("cmdb_model") | 01ae4e211b6c6090ee26dd39cd4bcb65 |
| scheduled_script:CMDB Data Certification UI View Cleanup(02019087530142106adfddeeff7b1262) | table:sys_ui_view | new GlideRecord('sys_ui_view') | 02019087530142106adfddeeff7b1262 |
| scheduled_script:VA-Adapter Update Profile(037d65c1737023008564b17afef6a7d3) | table:sys_cs_consumer_channel | new GlideRecord('sys_cs_consumer_channel') | 037d65c1737023008564b17afef6a7d3 |
| scheduled_script:SAM/CI - Populate Licensing Data(05226603b4ec1010fa9b5a04f86dbf10) | table:sys_trigger | new GlideRecord('sys_trigger') | 05226603b4ec1010fa9b5a04f86dbf10 |
| scheduled_script:SAM/CI - Populate Licensing Data(05226603b4ec1010fa9b5a04f86dbf10) | table:samp_job_log | new GlideRecord('samp_job_log') | 05226603b4ec1010fa9b5a04f86dbf10 |
| scheduled_script:Remove Orphaned Attachments(05737e64b7122010b0bea9a32e11a93f) | table:sys_attachment_cleaner_entry | new GlideRecord("sys_attachment_cleaner_entry") | 05737e64b7122010b0bea9a32e11a93f |
| scheduled_script:Convert Services Progress Refresher(0584d37f7347330061b79c0c6df6a746) | table:cmdb_convert_bulk_services | new GlideRecord('cmdb_convert_bulk_services') | 0584d37f7347330061b79c0c6df6a746 |
| scheduled_script:FlowDesigner : Cleanup Record watcher(07543d3ec7313010b59949f988c260b5) | table:sys_rw_action | new GlideRecord("sys_rw_action") | 07543d3ec7313010b59949f988c260b5 |
| scheduled_script:FlowDesigner : Cleanup Record watcher(07543d3ec7313010b59949f988c260b5) | table:sys_flow_context | new GlideRecord("sys_flow_context") | 07543d3ec7313010b59949f988c260b5 |
| scheduled_script:FlowDesigner : Cleanup Record watcher(07543d3ec7313010b59949f988c260b5) | table:sys_rw_action | new GlideRecord('sys_rw_action') | 07543d3ec7313010b59949f988c260b5 |
| scheduled_script:CSRF Violation Cleanup(08074eca93f022102d2b05001389184c) | table:sys_csrf_public_apis_violation | new GlideRecord("sys_csrf_public_apis_violation") | 08074eca93f022102d2b05001389184c |
| scheduled_script:Manage Account Validation(0a7277b21be474909e12997e0d4bcbe7) | table:customer_account | new GlideRecord("customer_account") | 0a7277b21be474909e12997e0d4bcbe7 |
| scheduled_script:Manage Account Validation(0a7277b21be474909e12997e0d4bcbe7) | table:u_tas_book_accounts | new GlideRecord("u_tas_book_accounts") | 0a7277b21be474909e12997e0d4bcbe7 |
| scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282) | table:pa_dashboards | new GlideRecord('pa_dashboards') | 0de900f3433d421050bb6e702cb8f282 |
| scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282) | table:pa_m2m_dashboard_tabs | new GlideRecord("pa_m2m_dashboard_tabs") | 0de900f3433d421050bb6e702cb8f282 |
| scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282) | table:pa_tabs | new GlideRecord("pa_tabs") | 0de900f3433d421050bb6e702cb8f282 |
| scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282) | table:sys_portal_page | new GlideRecord("sys_portal_page") | 0de900f3433d421050bb6e702cb8f282 |
| scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282) | table:sys_portal | new GlideRecord("sys_portal") | 0de900f3433d421050bb6e702cb8f282 |
| scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282) | table:sys_portal_preferences | new GlideRecord('sys_portal_preferences') | 0de900f3433d421050bb6e702cb8f282 |
| scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282) | table:sys_grid_canvas | new GlideRecord("sys_grid_canvas") | 0de900f3433d421050bb6e702cb8f282 |
| scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282) | table:sys_grid_canvas_pane | new GlideRecord('sys_grid_canvas_pane') | 0de900f3433d421050bb6e702cb8f282 |
| scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282) | table:sys_canvas_preferences | new GlideRecord('sys_canvas_preferences') | 0de900f3433d421050bb6e702cb8f282 |
| scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282) | table:pa_dashboards_permissions | new GlideRecord("pa_dashboards_permissions") | 0de900f3433d421050bb6e702cb8f282 |
| scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282) | table:sys_ui_section | new GlideRecord('sys_ui_section') | 0de900f3433d421050bb6e702cb8f282 |
| scheduled_script:Remove Servicenow Performance Dashboard(0de900f3433d421050bb6e702cb8f282) | table:sysauto_script | new GlideRecord('sysauto_script') | 0de900f3433d421050bb6e702cb8f282 |
| scheduled_script:LDAP Connection Test(0e27b960c332010016194ffe5bba8fbc) | table:ldap_server_config | new GlideRecord("ldap_server_config") | 0e27b960c332010016194ffe5bba8fbc |
| scheduled_script:LDAP Connection Test(0e27b960c332010016194ffe5bba8fbc) | table:ldap_server_url | new GlideRecord('ldap_server_url') | 0e27b960c332010016194ffe5bba8fbc |
| scheduled_script:LDAP Connection Test(0e27b960c332010016194ffe5bba8fbc) | event:ldap.connection_failed | gs.eventQueue("ldap.connection_failed" | 0e27b960c332010016194ffe5bba8fbc |
| scheduled_script:Trigger Notifications for CMDB DM Stale Tasks(0fff6af6772320108043270bba10619b) | table:cmdb_data_management_task | new GlideRecord('cmdb_data_management_task') | 0fff6af6772320108043270bba10619b |
| scheduled_script:Trigger Notifications for CMDB DM Stale Tasks(0fff6af6772320108043270bba10619b) | table:sysapproval_approver | new GlideRecord('sysapproval_approver') | 0fff6af6772320108043270bba10619b |
| scheduled_script:Trigger Notifications for CMDB DM Stale Tasks(0fff6af6772320108043270bba10619b) | event:cmdbdatamanager.task.stale | gs.eventQueue("cmdbdatamanager.task.stale" | 0fff6af6772320108043270bba10619b |
| scheduled_script:Count in scope assets(10e2ba6e1b0d6c106bc8dc65bd4bcb94) | table:customer_account | new GlideRecord('customer_account') | 10e2ba6e1b0d6c106bc8dc65bd4bcb94 |
| scheduled_script:Orphan ML Update Set Attachment Cleanup(1186e18f43013110e4aa4594bfb8f29a) | table:sys_attachment | new GlideRecord("sys_attachment") | 1186e18f43013110e4aa4594bfb8f29a |
| scheduled_script:Orphan ML Update Set Attachment Cleanup(1186e18f43013110e4aa4594bfb8f29a) | table:ml_update_set | new GlideRecord("ml_update_set") | 1186e18f43013110e4aa4594bfb8f29a |
| scheduled_script:Remove Agent Work Schedule end date older than a month(11d23849c3b42200467f10c422d3aea0) | table:agent_work_schedule | new GlideRecord("agent_work_schedule") | 11d23849c3b42200467f10c422d3aea0 |
| scheduled_script:Process Expense Allocation(11ed14619f312100d7f5f79ff57fcf09) | table:fm_expense_line | new GlideRecord("fm_expense_line") | 11ed14619f312100d7f5f79ff57fcf09 |
| scheduled_script:Calculate asset uptime(15a1ba431b9ba8903c0ffc4e0d4bcb3a) | table:alm_hardware | new GlideRecord("alm_hardware") | 15a1ba431b9ba8903c0ffc4e0d4bcb3a |
| scheduled_script:Calculate asset uptime(15a1ba431b9ba8903c0ffc4e0d4bcb3a) | table:cmn_location | new GlideRecord("cmn_location") | 15a1ba431b9ba8903c0ffc4e0d4bcb3a |
| scheduled_script:Calculate asset uptime(15a1ba431b9ba8903c0ffc4e0d4bcb3a) | table:cmdb_model | new GlideRecord("cmdb_model") | 15a1ba431b9ba8903c0ffc4e0d4bcb3a |
| scheduled_script:Calculate asset uptime(15a1ba431b9ba8903c0ffc4e0d4bcb3a) | table:sn_customerservice_asset_operability | new GlideRecord("sn_customerservice_asset_operability") | 15a1ba431b9ba8903c0ffc4e0d4bcb3a |
| scheduled_script:Calculate asset uptime(15a1ba431b9ba8903c0ffc4e0d4bcb3a) | table:sysauto_report | new GlideRecord('sysauto_report') | 15a1ba431b9ba8903c0ffc4e0d4bcb3a |
| scheduled_script:Calculate asset uptime(15a1ba431b9ba8903c0ffc4e0d4bcb3a) | table:sn_customerservice_case | new GlideRecord("sn_customerservice_case") | 15a1ba431b9ba8903c0ffc4e0d4bcb3a |
| scheduled_script:Calculate asset uptime(15a1ba431b9ba8903c0ffc4e0d4bcb3a) | table:sys_audit | new GlideRecord("sys_audit") | 15a1ba431b9ba8903c0ffc4e0d4bcb3a |
| scheduled_script:Calculate asset uptime(15a1ba431b9ba8903c0ffc4e0d4bcb3a) | table:wm_order | new GlideRecord("wm_order") | 15a1ba431b9ba8903c0ffc4e0d4bcb3a |
| scheduled_script:Ecc Queue Usage Analytics - Aggregate all topics from ecc_queue to ecc_queue_usage_analytics(1738989577423010b4b74b640d5a9903) | table:ecc_queue_usage_analytics | new GlideRecord('ecc_queue_usage_analytics') | 1738989577423010b4b74b640d5a9903 |
| scheduled_script:Disable Dave Walker's access(184f00711b04f0d09e12997e0d4bcb8f) | table:sys_user_grmember | new GlideRecord("sys_user_grmember") | 184f00711b04f0d09e12997e0d4bcb8f |
| scheduled_script:Enable Dave Walker's access(18da8cb51bc0f0d09e12997e0d4bcb3d) | table:sys_user_grmember | new GlideRecord("sys_user_grmember") | 18da8cb51bc0f0d09e12997e0d4bcb3d |
| scheduled_script:Inactive User Credential CleanUp(1da0ed27c32220102c5b4e483c40ddb7) | table:sys_user_public_credential | new GlideRecord('sys_user_public_credential') | 1da0ed27c32220102c5b4e483c40ddb7 |
| scheduled_script:Purge Orphaned Containerized MID Servers(1e70fdf453032010347cddeeff7b123c) | table:ecc_agent | new GlideRecord('ecc_agent') | 1e70fdf453032010347cddeeff7b123c |
| scheduled_script:Purge Orphaned Containerized MID Servers(1e70fdf453032010347cddeeff7b123c) | table:ecc_agent_issue | new GlideRecord('ecc_agent_issue') | 1e70fdf453032010347cddeeff7b123c |
| scheduled_script:Teams user auto syncing(206c86fcc32211100f24c87af040ddf1) | table:sys_cs_collab_provider_application | new GlideRecord('sys_cs_collab_provider_application') | 206c86fcc32211100f24c87af040ddf1 |
| scheduled_script:Teams user auto syncing(206c86fcc32211100f24c87af040ddf1) | table:sys_cs_collab_settings | new GlideRecord("sys_cs_collab_settings") | 206c86fcc32211100f24c87af040ddf1 |
| scheduled_script:Teams user auto syncing(206c86fcc32211100f24c87af040ddf1) | event:sidebar.teams.setup.complete | gs.eventQueue('sidebar.teams.setup.complete' | 206c86fcc32211100f24c87af040ddf1 |
| scheduled_script:Teams user auto syncing(206c86fcc32211100f24c87af040ddf1) | event:sidebar.teams.setup.failure | gs.eventQueue('sidebar.teams.setup.failure' | 206c86fcc32211100f24c87af040ddf1 |
| scheduled_script:sm dedup tracker for specific discovery sources(21754255db2cf3404cef76231f961956) | table:application_on_servers | new GlideRecord("application_on_servers") | 21754255db2cf3404cef76231f961956 |
| scheduled_script:Check Scoped App Author Config Changes(22b6bb03d700310092610eca5e610393) | event:sn_appauthor.check.config.update | gs.eventQueueScheduled("sn_appauthor.check.config.update" | 22b6bb03d700310092610eca5e610393 |
| scheduled_script:Enable search-based suggestions(25261d54ebf021100cd8d3e6475228e2) | table:sys_suggestion_reader_group | new GlideRecord('sys_suggestion_reader_group') | 25261d54ebf021100cd8d3e6475228e2 |
| scheduled_script:Populate Suggestions to avoid Cold Start - Portals(27ad23880fa933005203cbb2ff767eab) | table:sp_portal | new GlideRecord("sp_portal") | 27ad23880fa933005203cbb2ff767eab |
| scheduled_script:Populate Suggestions to avoid Cold Start - Portals(27ad23880fa933005203cbb2ff767eab) | table:m2m_sp_portal_search_source | new GlideRecord('m2m_sp_portal_search_source') | 27ad23880fa933005203cbb2ff767eab |
| scheduled_script:Populate Suggestions to avoid Cold Start - Portals(27ad23880fa933005203cbb2ff767eab) | table:sp_search_source | new GlideRecord('sp_search_source') | 27ad23880fa933005203cbb2ff767eab |
| scheduled_script:Expire Actionable Notifications(2a2b0150532310109686ddeeff7b121f) | table:sys_cs_notification | new GlideRecord("sys_cs_notification") | 2a2b0150532310109686ddeeff7b121f |
| scheduled_script:Expire Guest Session Identifier(2a647867531320103296ddeeff7b1217) | table:sys_cs_session_binding | new GlideRecord('sys_cs_session_binding') | 2a647867531320103296ddeeff7b1217 |
| scheduled_script:Expire Guest Session Identifier(2a647867531320103296ddeeff7b1217) | table:interaction | new GlideRecord('interaction') | 2a647867531320103296ddeeff7b1217 |
| scheduled_script:Expire Guest Session Identifier(2a647867531320103296ddeeff7b1217) | table:sys_cs_consumer | new GlideRecord('sys_cs_consumer') | 2a647867531320103296ddeeff7b1217 |
| scheduled_script:Enable Email Address Internationalization(31d52b94431102103ca9a661c9b8f212) | table:sys_email_account | new GlideRecordSecure("sys_email_account") | 31d52b94431102103ca9a661c9b8f212 |
| scheduled_script:Enable Email Address Internationalization(31d52b94431102103ca9a661c9b8f212) | table:sys_properties | new GlideRecord("sys_properties") | 31d52b94431102103ca9a661c9b8f212 |
| scheduled_script:Update display travel start and work end(31f46e1b48d6e110f877337ab8757e72) | table:wm_task | new GlideRecord("wm_task") | 31f46e1b48d6e110f877337ab8757e72 |
| scheduled_script:Migrate homepages(353a54c647a032107a684bdb736d437d) | table:sys_portal_page | new GlideRecord("sys_portal_page") | 353a54c647a032107a684bdb736d437d |
| scheduled_script:Migrate homepages(353a54c647a032107a684bdb736d437d) | table:sc_catalog_view_mtom | new GlideRecord("sc_catalog_view_mtom") | 353a54c647a032107a684bdb736d437d |
| scheduled_script:Migrate homepages(353a54c647a032107a684bdb736d437d) | table:pa_m2m_dashboard_tabs | new GlideRecord("pa_m2m_dashboard_tabs") | 353a54c647a032107a684bdb736d437d |
| scheduled_script:Migrate homepages(353a54c647a032107a684bdb736d437d) | table:pa_tabs | new GlideRecord("pa_tabs") | 353a54c647a032107a684bdb736d437d |
| scheduled_script:Migrate homepages(353a54c647a032107a684bdb736d437d) | table:sys_portal_page | new GlideRecord('sys_portal_page') | 353a54c647a032107a684bdb736d437d |
| scheduled_script:Migrate homepages(353a54c647a032107a684bdb736d437d) | table:sys_app_module | new GlideRecord("sys_app_module") | 353a54c647a032107a684bdb736d437d |
| scheduled_script:Migrate homepages(353a54c647a032107a684bdb736d437d) | table:sys_user | new GlideRecord("sys_user") | 353a54c647a032107a684bdb736d437d |
| scheduled_script:Migrate homepages(353a54c647a032107a684bdb736d437d) | table:sys_user_preference | new GlideRecord("sys_user_preference") | 353a54c647a032107a684bdb736d437d |
| scheduled_script:Migrate homepages(353a54c647a032107a684bdb736d437d) | table:syslog_transaction | new GlideRecord("syslog_transaction") | 353a54c647a032107a684bdb736d437d |
| scheduled_script:Migrate homepages(353a54c647a032107a684bdb736d437d) | table:sys_properties | new GlideRecord("sys_properties") | 353a54c647a032107a684bdb736d437d |
| scheduled_script:Migrate homepages(353a54c647a032107a684bdb736d437d) | table:sysauto_script | new GlideRecord("sysauto_script") | 353a54c647a032107a684bdb736d437d |
| scheduled_script:CSDM Data Sync(3903094e5362101061b7ddeeff7b12be) | table:cmdb_class_info | new GlideRecord("cmdb_class_info") | 3903094e5362101061b7ddeeff7b12be |
| scheduled_script:CSDM Data Sync(3903094e5362101061b7ddeeff7b12be) | table:cmdb_ci | new GlideRecord("cmdb_ci") | 3903094e5362101061b7ddeeff7b12be |
| scheduled_script:CSDM Data Sync(3903094e5362101061b7ddeeff7b12be) | table:cmdb_rel_ci | new GlideRecord('cmdb_rel_ci') | 3903094e5362101061b7ddeeff7b12be |
| scheduled_script:CSDM Data Sync(3903094e5362101061b7ddeeff7b12be) | table:service_offering | new GlideRecord('service_offering') | 3903094e5362101061b7ddeeff7b12be |
| scheduled_script:CSDM Data Sync(3903094e5362101061b7ddeeff7b12be) | table:svc_ci_assoc | new GlideRecord('svc_ci_assoc') | 3903094e5362101061b7ddeeff7b12be |
| scheduled_script:CSDM Data Sync(3903094e5362101061b7ddeeff7b12be) | table:cmdb_ci_query_based_service | new GlideRecord('cmdb_ci_query_based_service') | 3903094e5362101061b7ddeeff7b12be |
| scheduled_script:CSDM Data Sync(3903094e5362101061b7ddeeff7b12be) | event:csdm.tso.modified | gs.eventQueue('csdm.tso.modified' | 3903094e5362101061b7ddeeff7b12be |
| scheduled_script:Populate Helpful Count on Knowledge(3adc9b78c7f230108ad4010703c260d8) | table:sys_properties | new GlideRecord("sys_properties") | 3adc9b78c7f230108ad4010703c260d8 |
| scheduled_script:Update new requests with Freshdesk history(3d449c361b8a5010ee26dd39cd4bcb25) | table:sn_customerservice_freshdesk_journal_entries | new GlideRecord("sn_customerservice_freshdesk_journal_entries") | 3d449c361b8a5010ee26dd39cd4bcb25 |
| scheduled_script:Update new requests with Freshdesk history(3d449c361b8a5010ee26dd39cd4bcb25) | table:sc_request | new GlideRecord("sc_request") | 3d449c361b8a5010ee26dd39cd4bcb25 |
| scheduled_script:Update new requests with Freshdesk history(3d449c361b8a5010ee26dd39cd4bcb25) | table:sys_journal_field | new GlideRecord('sys_journal_field') | 3d449c361b8a5010ee26dd39cd4bcb25 |
| scheduled_script:Change project status to Retired due to inactivity(3e19f9fca3d0311011ecb18c26fcda53) | table:promin_project | new GlideRecord("promin_project") | 3e19f9fca3d0311011ecb18c26fcda53 |
| scheduled_script:Change project status to Retired due to inactivity(3e19f9fca3d0311011ecb18c26fcda53) | table:promin_ua_mining_tracker | new GlideRecord("promin_ua_mining_tracker") | 3e19f9fca3d0311011ecb18c26fcda53 |
| scheduled_script:Save and Manage CSM Trend Data(3eaa1a50dbe85050b40c355c68961969) | table:customer_account | new GlideRecord('customer_account') | 3eaa1a50dbe85050b40c355c68961969 |
| scheduled_script:Save and Manage CSM Trend Data(3eaa1a50dbe85050b40c355c68961969) | table:sn_customerservice_trend_data | new GlideRecord('sn_customerservice_trend_data') | 3eaa1a50dbe85050b40c355c68961969 |
| scheduled_script:Save and Manage CSM Trend Data(3eaa1a50dbe85050b40c355c68961969) | table:sn_customerservice_case | new GlideRecord('sn_customerservice_case') | 3eaa1a50dbe85050b40c355c68961969 |
| scheduled_script:Save and Manage CSM Trend Data(3eaa1a50dbe85050b40c355c68961969) | table:sys_audit | new GlideRecord('sys_audit') | 3eaa1a50dbe85050b40c355c68961969 |
| scheduled_script:Save and Manage CSM Trend Data(3eaa1a50dbe85050b40c355c68961969) | table:task_sla | new GlideRecord('task_sla') | 3eaa1a50dbe85050b40c355c68961969 |
| scheduled_script:Save and Manage CSM Trend Data(3eaa1a50dbe85050b40c355c68961969) | table:wm_order | new GlideRecord('wm_order') | 3eaa1a50dbe85050b40c355c68961969 |
| scheduled_script:Save and Manage CSM Trend Data(3eaa1a50dbe85050b40c355c68961969) | table:wm_task | new GlideRecord('wm_task') | 3eaa1a50dbe85050b40c355c68961969 |
| scheduled_script:Create personal stockroom for agents(3f252224b05ba510f8775f657a932b16) | table:sys_user_has_role | new GlideRecord("sys_user_has_role") | 3f252224b05ba510f8775f657a932b16 |
| scheduled_script:Create personal stockroom for agents(3f252224b05ba510f8775f657a932b16) | table:sm_config | new GlideRecord('sm_config') | 3f252224b05ba510f8775f657a932b16 |
| scheduled_script:Service Model Auto Remediation(42aaef8153133010b33bddeeff7b1225) | table:cmdb_ci_service_discovered | new GlideRecord('cmdb_ci_service_discovered') | 42aaef8153133010b33bddeeff7b1225 |
| scheduled_script:Service Model Auto Remediation(42aaef8153133010b33bddeeff7b1225) | table:svc_layer | new GlideRecord('svc_layer') | 42aaef8153133010b33bddeeff7b1225 |
| scheduled_script:Service Model Auto Remediation(42aaef8153133010b33bddeeff7b1225) | table:svc_environment | new GlideRecord('svc_environment') | 42aaef8153133010b33bddeeff7b1225 |
| scheduled_script:Service Model Auto Remediation(42aaef8153133010b33bddeeff7b1225) | table:sa_m2m_service_entry_point | new GlideRecord('sa_m2m_service_entry_point') | 42aaef8153133010b33bddeeff7b1225 |
| scheduled_script:Service Model Auto Remediation(42aaef8153133010b33bddeeff7b1225) | table:svc_model_assoc_ci | new GlideRecord('svc_model_assoc_ci') | 42aaef8153133010b33bddeeff7b1225 |
| scheduled_script:Remove old first party scoped application deletes from sys_metadata_delete table(4404c6375b43611034d351a2ea81c7a6) | table:sys_scope | GlideRecord("sys_scope") | 4404c6375b43611034d351a2ea81c7a6 |
| scheduled_script:Remove old first party scoped application deletes from sys_metadata_delete table(4404c6375b43611034d351a2ea81c7a6) | table:sys_metadata_delete | GlideRecord("sys_metadata_delete") | 4404c6375b43611034d351a2ea81c7a6 |
| scheduled_script:Create routine and regular request(44fe677b1b677c108e64eb92b24bcbe4) | table:sc_request | new GlideRecord("sc_request") | 44fe677b1b677c108e64eb92b24bcbe4 |
| scheduled_script:Create routine and regular request(44fe677b1b677c108e64eb92b24bcbe4) | table:sys_user | new GlideRecord('sys_user') | 44fe677b1b677c108e64eb92b24bcbe4 |
| scheduled_script:Discovery Credentials Affinity Cleanup(45fa94b51c92a910f877a567a129d63a) | table:dscy_credentials_affinity | new GlideRecordSecure('dscy_credentials_affinity') | 45fa94b51c92a910f877a567a129d63a |
| scheduled_script:cleanup_sys_json_chunks_missing_parent_sys_flow_report_doc(46c84b15b7031010c8c208fd7e11a9d2) | table:flow_report_chunk | new GlideRecord('flow_report_chunk') | 46c84b15b7031010c8c208fd7e11a9d2 |
| scheduled_script:cleanup_sys_json_chunks_missing_parent_sys_flow_report_doc(46c84b15b7031010c8c208fd7e11a9d2) | table:sys_json_chunk | new GlideRecord('sys_json_chunk') | 46c84b15b7031010c8c208fd7e11a9d2 |
| scheduled_script:Cleanup Attachment Scan History(4757bdf087313300a0807f9719cb0b52) | table:attachment_scan_history | new GlideRecord('attachment_scan_history') | 4757bdf087313300a0807f9719cb0b52 |
| scheduled_script:Identify a sys id(4802598e1bcf6c103c0ffc4e0d4bcb2b) | table:sys_db_object | new GlideRecord('sys_db_object') | 4802598e1bcf6c103c0ffc4e0d4bcb2b |
| scheduled_script:Populate Internet Facing attribute on Hardware(494da85d7310001061b79c0c6df6a700) | table:cmdb_ci_hardware | new GlideRecord('cmdb_ci_hardware') | 494da85d7310001061b79c0c6df6a700 |
| scheduled_script:Timeout For VA Chats Suspended on NLU Prediction(495f4ed15b22201007004d3ba881c7b0) | table:open_nlu_predict_state_tracking | new GlideRecord('open_nlu_predict_state_tracking') | 495f4ed15b22201007004d3ba881c7b0 |
| scheduled_script:Enable Stefan's access(4a1cc8f51bc0f0d09e12997e0d4bcb39) | table:sys_user_grmember | new GlideRecord("sys_user_grmember") | 4a1cc8f51bc0f0d09e12997e0d4bcb39 |
| scheduled_script:Delete Swync updates(4ab074571b43b4148e64eb92b24bcb31) | table:sys_journal_field | new GlideRecord("sys_journal_field") | 4ab074571b43b4148e64eb92b24bcb31 |
| scheduled_script:Application Service Manual Ep Cleanup(4af6a14a77b111105f2ea1b35b5a99d4) | table:cmdb_ci_endpoint_manual | new GlideRecord("cmdb_ci_endpoint_manual") | 4af6a14a77b111105f2ea1b35b5a99d4 |
| scheduled_script:Close Document Task Execution records(4b57fcebc37611108787ac8b8640dd25) | table:sn_doc_task_execution | new GlideRecord('sn_doc_task_execution') | 4b57fcebc37611108787ac8b8640dd25 |
| scheduled_script:Close Document Task Execution records(4b57fcebc37611108787ac8b8640dd25) | table:sys_flow_context | new GlideRecord('sys_flow_context') | 4b57fcebc37611108787ac8b8640dd25 |
| scheduled_script:Timeout For VA-OneExtend Interactive Chats(4b72c152eb921110c27601c7c152282b) | table:sys_cs_one_extend_invocation | new GlideRecord('sys_cs_one_extend_invocation') | 4b72c152eb921110c27601c7c152282b |
| scheduled_script:Identify duplicated TAS UIDs(4fcdfc311bf6f890afb921f0b24bcb53) | table:customer_account | new GlideRecord("customer_account") | 4fcdfc311bf6f890afb921f0b24bcb53 |
| scheduled_script:CI Rate Card Item Review(5149273cc0a80a6d3e5df70935b63d45) | table:fm_ci_rate_card | new GlideRecord("fm_ci_rate_card") | 5149273cc0a80a6d3e5df70935b63d45 |
| scheduled_script:CI Rate Card Item Review(5149273cc0a80a6d3e5df70935b63d45) | event:fm.ci_ratecard.review | gs.eventQueue("fm.ci_ratecard.review" | 5149273cc0a80a6d3e5df70935b63d45 |
| scheduled_script:Temporary Lists Auto Delete(52a28136b54d5210f877f829dcce6bbd) | table:sys_ux_my_list | new GlideRecord('sys_ux_my_list') | 52a28136b54d5210f877f829dcce6bbd |
| scheduled_script:Mark VM state as terminated(53a48dfc97987d50a24c75b71153af06) | table:cmdb_ci_vmware_instance | new GlideRecord("cmdb_ci_vmware_instance") | 53a48dfc97987d50a24c75b71153af06 |
| scheduled_script:Mark VM state as terminated(53a48dfc97987d50a24c75b71153af06) | table:sysauto_script | new GlideRecord("sysauto_script") | 53a48dfc97987d50a24c75b71153af06 |
| scheduled_script:Mark VM state as terminated(53a48dfc97987d50a24c75b71153af06) | table:cmdb_ci_vmware_instance | new GlideRecord('cmdb_ci_vmware_instance') | 53a48dfc97987d50a24c75b71153af06 |
| scheduled_script:Auto-associate Unmatched Contacts in Catch All account(543b1eec1b6cffc0ea17dd3fbd4bcbfb) | table:customer_contact | new GlideRecord('customer_contact') | 543b1eec1b6cffc0ea17dd3fbd4bcbfb |
| scheduled_script:Auto-associate Unmatched Contacts in Catch All account(543b1eec1b6cffc0ea17dd3fbd4bcbfb) | table:u_domain | new GlideRecord('u_domain') | 543b1eec1b6cffc0ea17dd3fbd4bcbfb |
| scheduled_script:Populate Meta Description on KB Articles(545c344523b30300cc4bcb0a56bf6523) | table:kb_knowledge | new GlideRecord('kb_knowledge') | 545c344523b30300cc4bcb0a56bf6523 |
| scheduled_script:cleanup_sys_json_chunks_missing_parent_sys_flow_context(59375537b7131010c8c208fd7e11a972) | table:flow_context_chunk | new GlideRecord('flow_context_chunk') | 59375537b7131010c8c208fd7e11a972 |
| scheduled_script:cleanup_sys_json_chunks_missing_parent_sys_flow_context(59375537b7131010c8c208fd7e11a972) | table:sys_json_chunk | new GlideRecord('sys_json_chunk') | 59375537b7131010c8c208fd7e11a972 |
| scheduled_script:Save and Manage Audit Trend Data(5e725f581b5d60106bc8dc65bd4bcbc6) | table:sys_user | new GlideRecord("sys_user") | 5e725f581b5d60106bc8dc65bd4bcbc6 |
| scheduled_script:Save and Manage Audit Trend Data(5e725f581b5d60106bc8dc65bd4bcbc6) | table:x_xos_snoms_audit_trend | new GlideRecord('x_xos_snoms_audit_trend') | 5e725f581b5d60106bc8dc65bd4bcbc6 |
| scheduled_script:Count in scope devices(5eb45a281b72b090afb921f0b24bcb66) | table:customer_account | new GlideRecord('customer_account') | 5eb45a281b72b090afb921f0b24bcb66 |
| scheduled_script:Proactive Event Monitoring(6044b3fb1b559490e1fb535c2e4bcb01) | table:sys_email | new GlideRecord('sys_email') | 6044b3fb1b559490e1fb535c2e4bcb01 |
| scheduled_script:Proactive Event Monitoring(6044b3fb1b559490e1fb535c2e4bcb01) | event:proactive.monitoring | gs.eventQueue('proactive.monitoring' | 6044b3fb1b559490e1fb535c2e4bcb01 |
| scheduled_script:Identify and delete locations with no related records(6504c68e1b05e8106bc8dc65bd4bcba8) | table:cmn_location | new GlideRecord("cmn_location") | 6504c68e1b05e8106bc8dc65bd4bcba8 |
| scheduled_script:Identify and delete locations with no related records(6504c68e1b05e8106bc8dc65bd4bcba8) | table:alm_asset | new GlideRecord("alm_asset") | 6504c68e1b05e8106bc8dc65bd4bcba8 |
| scheduled_script:Identify and delete locations with no related records(6504c68e1b05e8106bc8dc65bd4bcba8) | table:x_xos_snoms_deal_item | new GlideRecord("x_xos_snoms_deal_item") | 6504c68e1b05e8106bc8dc65bd4bcba8 |
| scheduled_script:Identify and delete locations with no related records(6504c68e1b05e8106bc8dc65bd4bcba8) | table:customer_contact | new GlideRecord("customer_contact") | 6504c68e1b05e8106bc8dc65bd4bcba8 |
| scheduled_script:Clear expired client push notifications(67930225a00ec210f877d14226746142) | table:sn_vsc_client_push_notifications | new GlideRecord('sn_vsc_client_push_notifications') | 67930225a00ec210f877d14226746142 |
| scheduled_script:Manage duplicated serial numbers(6b4b7284db68f4500ccf918cd396192b) | table:alm_hardware | new GlideRecord("alm_hardware") | 6b4b7284db68f4500ccf918cd396192b |
| scheduled_script:Manage duplicated serial numbers(6b4b7284db68f4500ccf918cd396192b) | table:x_xos_snoms_deal_item | new GlideRecord("x_xos_snoms_deal_item") | 6b4b7284db68f4500ccf918cd396192b |
| scheduled_script:Schedule master asset list reports(6f2ad5be1b2e50d0ee26dd39cd4bcb06) | table:customer_account | new GlideRecord('customer_account') | 6f2ad5be1b2e50d0ee26dd39cd4bcb06 |
| scheduled_script:Schedule master asset list reports(6f2ad5be1b2e50d0ee26dd39cd4bcb06) | table:sys_user | new GlideRecord('sys_user') | 6f2ad5be1b2e50d0ee26dd39cd4bcb06 |
| scheduled_script:Schedule master asset list reports(6f2ad5be1b2e50d0ee26dd39cd4bcb06) | table:sysauto_report | new GlideRecord("sysauto_report") | 6f2ad5be1b2e50d0ee26dd39cd4bcb06 |
| scheduled_script:Schedule master asset list reports(6f2ad5be1b2e50d0ee26dd39cd4bcb06) | table:sys_report | new GlideRecord("sys_report") | 6f2ad5be1b2e50d0ee26dd39cd4bcb06 |
| scheduled_script:Schedule master asset list reports(6f2ad5be1b2e50d0ee26dd39cd4bcb06) | table:sys_report | new GlideRecord('sys_report') | 6f2ad5be1b2e50d0ee26dd39cd4bcb06 |
| scheduled_script:Schedule master asset list reports(6f2ad5be1b2e50d0ee26dd39cd4bcb06) | table:sysauto_report | new GlideRecord('sysauto_report') | 6f2ad5be1b2e50d0ee26dd39cd4bcb06 |
| scheduled_script:SC - Calculate Compliance Monthly(6f3ea65153611110dd8eddeeff7b1240) | table:sysauto_pa | new GlideRecord('sysauto_pa') | 6f3ea65153611110dd8eddeeff7b1240 |
| scheduled_script:Calculate asset uptime (UHL)(6f6111381bbdf09018ba748bd34bcbfe) | table:alm_hardware | new GlideRecord("alm_hardware") | 6f6111381bbdf09018ba748bd34bcbfe |
| scheduled_script:Calculate asset uptime (UHL)(6f6111381bbdf09018ba748bd34bcbfe) | table:cmn_location | new GlideRecord("cmn_location") | 6f6111381bbdf09018ba748bd34bcbfe |
| scheduled_script:Calculate asset uptime (UHL)(6f6111381bbdf09018ba748bd34bcbfe) | table:cmdb_model | new GlideRecord("cmdb_model") | 6f6111381bbdf09018ba748bd34bcbfe |
| scheduled_script:Calculate asset uptime (UHL)(6f6111381bbdf09018ba748bd34bcbfe) | table:sn_customerservice_asset_operability | new GlideRecord("sn_customerservice_asset_operability") | 6f6111381bbdf09018ba748bd34bcbfe |
| scheduled_script:Calculate asset uptime (UHL)(6f6111381bbdf09018ba748bd34bcbfe) | table:sysauto_report | new GlideRecord('sysauto_report') | 6f6111381bbdf09018ba748bd34bcbfe |
| scheduled_script:Calculate asset uptime (UHL)(6f6111381bbdf09018ba748bd34bcbfe) | table:sn_customerservice_case | new GlideRecord("sn_customerservice_case") | 6f6111381bbdf09018ba748bd34bcbfe |
| scheduled_script:Calculate asset uptime (UHL)(6f6111381bbdf09018ba748bd34bcbfe) | table:sys_audit | new GlideRecord("sys_audit") | 6f6111381bbdf09018ba748bd34bcbfe |
| scheduled_script:Calculate asset uptime (UHL)(6f6111381bbdf09018ba748bd34bcbfe) | table:wm_order | new GlideRecord("wm_order") | 6f6111381bbdf09018ba748bd34bcbfe |
| scheduled_script:Update Deal IDs(7059098c1bbf7c108e64eb92b24bcbba) | table:alm_hardware | new GlideRecord("alm_hardware") | 7059098c1bbf7c108e64eb92b24bcbba |
| scheduled_script:Clean up events with NULL queue(70d410cbe701130022c920c343f6a9b0) | table:sysevent | new GlideRecord('sysevent') | 70d410cbe701130022c920c343f6a9b0 |
| scheduled_script:Reconcile All Record Hierarchies(73660eeeeb6112101e31e5b26b522865) | table:sys_record_hierarchy | new GlideRecord('sys_record_hierarchy') | 73660eeeeb6112101e31e5b26b522865 |
