# ACL Matrix

## Executive Narrative
The ACL matrix captures access control depth, scripted control concentration, and operation mix across the instance.

## Security Summary
- Total ACL records: **498**
- Scripted ACL records: **48**
- ACLs with explicit roles: **0**

## ACLs by Operation
| Operation | Count |
| --- | --- |
| read | 130 |
| write | 113 |
| delete | 92 |
| create | 87 |
| 0997ab83733303005978e4b9cdf6a7b9 | 50 |
| execute | 20 |
| 54f535270a0a0b8c007c67009ab2bdc0 | 4 |
| f6861c32c0a8016400647951e901525d | 1 |
| e66cf897b7300210240b06dd1e11a9fd | 1 |

## Top Tables by ACL Volume
| Table | ACL Count |
| --- | --- |
| kb_feedback | 6 |
| kb_navons | 4 |
| kb_use | 4 |
| sla_request | 3 |
| ast_contract | 3 |
| task | 3 |
| pa_scores | 3 |
| sn_customerservice_case | 3 |
| sc_ts_query | 2 |
| sys_atf_step_performance_metrics | 2 |
| sys_atf_modified_record_m2m | 2 |
| sysevent_queue_param_definition | 2 |
| awa_service_channel | 2 |
| chat_queue_entry | 2 |
| now | 2 |
| std_change_proposal | 2 |
| sn_cmdb_ws_imp_action_card_config | 2 |
| pa_indicator_aggregate_excl | 2 |
| sys_nlu_intent | 2 |
| sn_cmdb_ws_feature_category_runtime_attribute | 2 |
| ts_c_34_8 | 2 |
| sc_request | 2 |
| sys_ui_module | 2 |
| text_search | 2 |
| sn_dependentclient_application | 2 |
| sys_cs_ca_message | 2 |
| cxs_search_result_fields | 2 |
| ts_c_3_9 | 2 |
| itom_lu_definition_usage_count | 2 |
| alm_asset | 2 |
| sn_sub_man_st_subscription_license_detail_metric | 2 |
| 2b8f18ae433431106c85385cdcb8f2b2 | 1 |
| sys_auth_mfa_context_mfa_factor_m2m | 1 |
| sys_notification_actionable_content | 1 |
| sn_bm_client_recommendation_eval | 1 |
| ecc_action | 1 |
| sc_req_item | 1 |
| sp_css_include | 1 |
| sp_row | 1 |
| sys_m2m_email_report_attachment | 1 |
| sys_pd_activity_override | 1 |
| cmdb_rel_filter | 1 |
| 578dedff53622110b87eddeeff7b1247 | 1 |
| sys_app_template_output_var | 1 |
| sp_search_facet_filter | 1 |
| agent_daily_schedule | 1 |
| cmdb_data_classification | 1 |
| sys_ws_header_map | 1 |
| cmdb_policy_type_categories | 1 |
| asmt_m2m_category_user | 1 |
| sn_apptmnt_booking_config_rule | 1 |
| sys_sg_screen_cache | 1 |
| sys_report_source | 1 |
| sys_api_response | 1 |
| sn_cmdb_ws_class_icon | 1 |
| asset_content_audit | 1 |
| sys_security_obj_oper | 1 |
| pwd_active_answer | 1 |
| sys_service_endpoint_state | 1 |
| sttrm_transition_condition | 1 |
| sn_nowassist_diagn_execution_result_message | 1 |
| cmdb_health_scorecard_service | 1 |
| sys_nowmq_subject_param | 1 |
| svc_extension_variable | 1 |
| sys_api_response_map | 1 |
| sn_ex_sp_todo_config_detail | 1 |
| ts_c_35_9 | 1 |
| oauth_entity_auth_scope_mapping | 1 |
| ts_c_6_0 | 1 |
| ts_c_6_2 | 1 |
| cert_follow_on_task | 1 |
| gcf_staging | 1 |
| sn_diagram_builder_ui_action | 1 |
| sys_db_size_stats | 1 |
| cmdb_multisource_deny_class | 1 |
| FSMManagerMapAJAX | 1 |
| par_dashboard_widget | 1 |
| sys_rest_csrf_allow_list | 1 |
| sn_aisearch_global_migration_job | 1 |
| sys_glide_object | 1 |
| sku_metadata | 1 |
| asmt_assessment_instance | 1 |
| sys_upgrade_app_version_history | 1 |
| be87b71e5b723110d9a5ce1a8581c775 | 1 |
| sys_attachment_soft_deleted | 1 |
| sn_wn_content | 1 |
| c92f61657793301039ac088b3a106154 | 1 |
| chg_overview_container | 1 |
| svc_baseline_exclusion | 1 |
| sys_gen_ai_control_setting | 1 |
| ts_c_24_2 | 1 |
| cmdb_ci_service_discovered | 1 |
| quickactions_workspace_action | 1 |
| cert_element | 1 |
| sys_sg_popup | 1 |
| awa_reject_reason | 1 |
| sys_page_theme | 1 |
| sys_gen_ai_provider_preference | 1 |
| sys_logger_configuration | 1 |
| sn_vsc_changed_hardening_settings | 1 |

## Full ACL Register
| Name | Operation | Type | Requires Role | Scripted | Active | Scope | Sys ID |
| --- | --- | --- | --- | --- | --- | --- | --- |
| /api/sn_wwna/wwna/ | execute | REST_Endpoint |  | false | true | 757c34719bf7f10c4a1f9fe81ba8bba3 | 038d9a8a43520210fbb28b11afb8f276 |
| 1b87ac687f9b521090975aba3c8665c1 | execute | 6d9c40e9531210101cb3ddeeff7b12f6 |  | false | true | global | 029868e87f9b521090975aba3c866504 |
| 24eecef4738a1010e37d71ef64f6a73b | execute | 6d9c40e9531210101cb3ddeeff7b12f6 |  | false | true | 7a9ab70373830010e37d71ef64f6a78b | 031b8bdc437912105652cfedefb8f2a2 |
| 2b8f18ae433431106c85385cdcb8f2b2 | execute | 6d9c40e9531210101cb3ddeeff7b12f6 |  | false | true | 5d66b0fbe770230003cd6188d2f6a976 | 000024ee433431106c85385cdcb8f240 |
| 50855f17076320105fca5d1aead30036 | execute | 6d9c40e9531210101cb3ddeeff7b12f6 |  | false | true | ead9fb5f8b27a051aa71b35163745b82 | 018cdb1b076320105fca5d1aead30035 |
| 578dedff53622110b87eddeeff7b1247 | execute | 6d9c40e9531210101cb3ddeeff7b12f6 |  | false | true | c8ab76825371201032b7ddeeff7b1280 | 0010b57753a22110b87eddeeff7b126a |
| 81c234b57fe31290076726d6ac866513 | execute | 6d9c40e9531210101cb3ddeeff7b12f6 |  | false | true | 7c395aaa53003110453cddeeff7b123c | 0353f0f57fe31290076726d6ac86658f |
| ATFTracingHelperAjax | execute | client_callable_script_include |  | false | true | global | 01c31aabff10221086faffffffffff71 |
| DocumentTaskAjax | execute | client_callable_script_include |  | true | true | 6a9ea833b763330088d9bc78ee11a88q | 00ebd5ba532600107d70ddeeff7b122a |
| FSMManagerMapAJAX | execute | client_callable_script_include |  | false | true | global | 005d1e08234523002dd6cb0a56bf65cc |
| SAMAjaxUtil | execute | client_callable_script_include |  | false | true | global | 01ca041be9900010fa9b6dba53a930b7 |
| SMServiceByTagsUtilsAjax | execute | client_callable_script_include |  | false | true | global | 00cc021ab7699110e62a8e55ce11a95a |
| a693e68353d1f110fdadddeeff7b12c7 | execute | 6d9c40e9531210101cb3ddeeff7b12f6 |  | false | true | c8ab76825371201032b7ddeeff7b1280 | 0255e20753d1f110fdadddeeff7b124e |
| account_address_relationship | create | record |  | false | true | global | 014ba7b49310d210a1b29bf56489188b |
| agent_daily_schedule | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 0017c28d9f90961091ee0fc9da0a1c42 |
| ais_connection | delete | record |  | false | true | global | 03324064c7230010d1cfd9795cc260a2 |
| alm_asset.assigned_to | read | record |  | false | true | global | 032702b7d7110200bef20ee60e6103df |
| alm_asset.stockroom | read | record |  | false | true | global | 02c1b6011b7310002502fbcd2c0713bd |
| alm_custom_template_task | read | record |  | false | true | global | 029a94d7e70033009a610558d2f6a979 |
| alm_fixed_assets | read | record |  | false | true | global | 0164db9437703000158bbfc8bcbe5d13 |
| alm_transfer_order_line.tracking_number | write | record |  | false | true | global | 027f3db1fc543300964f1e70a9c62b78 |
| amb_welcome | read | ui_page |  | false | true | global | 02a40c30eb120200e628648d9106febc |
| announcement_style | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 037cd20457a71010a9ad78e1a95529b9 |
| app_cmn_field_set_item | read | record |  | false | true | f1ad77c7671210109743b1bb27415acd | 00b07aabc72210104c1bf9f91dc260a6 |
| app_cmn_filter_config | read | record |  | false | true | f1ad77c7671210109743b1bb27415acd | 01454c93671210109743b1bb27415add |
| application_diagnostic.* | read | record |  | false | true | global | 01fb0bd51b262300985ba64fad4bcb15 |
| appsec_domain_result_set | delete | record |  | false | true | global | 03687e6b53331300a8ed21fac2dc3491 |
| asmt_assessment_instance | create | record |  | true | true | global | 0067e411df020100cd7da5f59bf26358 |
| asmt_m2m_category_user | delete | record |  | true | true | global | 001aa48187a323004caf66d107cb0bc7 |
| asmt_m2m_ycategory_matrix | read | record |  | true | true | global | 024a91b8df110100cd7da5f59bf263f8 |
| asset_content_audit | create | record |  | false | true | global | 002a8fa9b73333002c50ff98ee11a93d |
| ast_contract.* | read | record |  | true | true | global | 00739cb4df332100a9e78b6c3df263fc |
| ast_contract.starts | e66cf897b7300210240b06dd1e11a9fd | record |  | false | true | global | 03871834a141a210f877f4e599decfd9 |
| ast_contract.tax_exempt | write | record |  | false | true | global | 03480b1437a030007415bfc8bcbe5d93 |
| ast_contract_list | read | ui_page |  | false | true | global | 017d5842d7210200bef20ee60e6103f6 |
| attachment_scan_history | read | record |  | false | true | global | 01461ce7db3b030012599aefe0b8f50c |
| awa_integration_user | execute | REST_Endpoint |  | false | true | global | 026cdb0167422300a0bd35e643415a33 |
| awa_queue_metrics | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 013c92d577ef51100801255a1e5a9940 |
| awa_reject_reason | write | record |  | false | true | global | 008926639304d2104d0a423b928918f4 |
| awa_service_channel | read | record |  | false | true | global | 00498a44934452104d0a423b92891832 |
| awa_service_channel.assignment_group_field | write | record |  | false | true | global | 01942ad1732023004a905ee515f6a7b6 |
| basic_retry_conditions | read | record |  | false | true | global | 015139379fb10210204aa8530b0a1c46 |
| be87b71e5b723110d9a5ce1a8581c775 | execute | 6d9c40e9531210101cb3ddeeff7b12f6 |  | false | true | global | 006af3de5b723110d9a5ce1a8581c784 |
| business_unit | write | record |  | false | true | global | 0300820f873332008a4a578c87cb0bf2 |
| c92f61657793301039ac088b3a106154 | execute | 6d9c40e9531210101cb3ddeeff7b12f6 |  | false | true | c2a7835187123010a4a2c077f6cb0bc0 | 0070b1a57793301039ac088b3a10615f |
| catalog_category_request | delete | record |  | false | true | global | 019402e07f3452100c5dffd73c866528 |
| catalog_dl_definition | create | record |  | false | true | global | 0386920a9f1030007bb2ed93ee4bcc86 |
| central_dispatch_config.task_table | create | record |  | true | true | global | 018ea4d1d723020058c92cf65e610370 |
| cert_element | delete | record |  | false | false | global | 008022f97f301210cc4835c59c866522 |
| cert_follow_on_task.assignment_group | write | record |  | true | true | global | 004f02d2bfd10100eae043fada073946 |
| chat_queue_entry | delete | record |  | false | true | global | 02732a3c838312109d5adbe4d12bc086 |
| chat_queue_entry.state | write | record |  | false | true | global | 006a46b19f012200d5f9b3e2957fcf23 |
| chat_survey.* | create | record |  | false | true | global | 01f32047731313009ecc234ffff6a7cd |
| chg_model_condition_type | read | record |  | false | true | global | 01caec015343101034d1ddeeff7b12d1 |
| chg_overview_container | create | record |  | false | true | bccbdbb023213010785ddc1756bf6579 | 0074a4fb5310a11088d8ddeeff7b12fa |
| clm_m2m_contract_asset | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 01c3c49677df1110814d99f69c5a993e |
| clone_data_exclude.* | read | record |  | false | false | global | 01fb0bd51b262300985ba64fad4bcb27 |
| clone_instance | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 018efe3bed2a4366a88a2f74ba6f04b7 |
| cmdb_ci_service_discovered | create | record |  | false | true | global | 007bad04ff3002002e6bffffffffff24 |
| cmdb_ci_state_management_task_to_ci | delete | record |  | false | false | global | 009a89b07fc512108e66144a5b8665e8 |
| cmdb_data_classification | read | record |  | false | true | global | 00188ee2ff312110f76fc6ff9c3bf1b6 |
| cmdb_data_management_policy | write | record |  | false | false | global | 009a89b07fc512108e66144a5b8665f9 |
| cmdb_dynamic_ire_match | create | record |  | false | true | global | 037787600b73101099b8ea7885673a47 |
| cmdb_dynamic_reconciliation_definition | delete | record |  | false | true | global | 00e253f273b23010dc50c3ed8ff6a7cf |
| cmdb_facility_product_model | read | ui_page |  | false | true | global | 03594916d7310200bef20ee60e61038f |
| cmdb_group_contains_qb_query | delete | record |  | false | true | global | 029089bed7812200de92a5f75e61035f |
| cmdb_group_type | write | record |  | false | false | global | 035b89f07fc512108e66144a5b8665ba |
| cmdb_health_config | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | false | global | 02286e69930112102c4c098a54891841 |
| cmdb_health_metric_status | create | record |  | false | false | global | 03286e69930112102c4c098a54891893 |
| cmdb_health_scorecard_service | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | false | global | 0038ae69930112102c4c098a548918db |
| cmdb_ip_address_dns_name | read | record |  | false | false | global | 01f6d1d3b76022109da9ff43ae11a9b9 |
| cmdb_ip_service_ci | create | record |  | false | true | global | 00dca95a5b101210b0d51e991e81c775 |
| cmdb_ire_data_source_rule | write | record |  | false | true | global | 00e4d8930f500010c5f2fc91ff767e1e |
| cmdb_ire_partial_payloads_index | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | false | global | 013822a9930112102c4c098a548918d6 |
| cmdb_key_value | read | record |  | false | true | global | 029f34547f0000101952baf8befa9191 |
| cmdb_lb_vlan_interface | write | record |  | false | false | global | 01f6d1d3b76022109da9ff43ae11a9fc |
| cmdb_m2m_model_compatibility.model_1 | write | record |  | false | true | global | 009544b9471220009343706eecde27a5 |
| cmdb_metadata_containment | write | record |  | false | false | global | 013862a9930112102c4c098a54891838 |
| cmdb_multilevel_queue_item | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 02795a6eb7610210a616c5a8ee11a971 |
| cmdb_multisource_data | write | record |  | false | false | global | 023862a9930112102c4c098a548918bb |
| cmdb_multisource_deny_class | delete | record |  | false | true | global | 005be9cb77976110085c067f5b5a995c |
| cmdb_multisource_query | delete | record |  | false | false | global | 0338a2a9930112102c4c098a5489180d |
| cmdb_multisource_recomp_task_ci | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | false | global | 0148e2a9930112102c4c098a54891804 |
| cmdb_policy_type_categories | write | record |  | false | true | global | 001a929a53362010af64ddeeff7b12f0 |
| cmdb_reconciliation_definition_mapping | create | record |  | false | false | global | 0148e2a9930112102c4c098a54891856 |
| cmdb_rel_filter | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | false | global | 001059387fc512108e66144a5b866521 |
| cmdb_rel_group_type | create | record |  | false | false | global | 011099387fc512108e66144a5b866591 |
| cmdb_rel_team | read | record |  | false | false | global | 011099387fc512108e66144a5b8665d4 |
| cmdb_task_to_archive_chunk | read | record |  | false | false | global | 019a0db07fc512108e66144a5b866550 |
| contract_rel_user | read | record |  | false | true | global | 02ddf6bec7b1330034d1f8d07a9763f2 |
| core_company | read | record |  | false | true | global | 00df2becff3722103ad8ffffffffffeb |
| cxs_filter_mapping | read | record |  | false | true | global | 037fdaa2d7702200cc4b00285e610344 |
| cxs_search_result_fields | delete | record |  | false | true | global | 01d97d6453af130005ecddeeff7b1221 |
| cxs_search_result_fields.detail_component_name | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 02212d2653101010207bddeeff7b12b0 |
| cxs_table_fltr_condition | write | record |  | false | true | global | 0258de4ad733220034d145bcce6103e2 |
| discovery_help_link | delete | record |  | false | true | global | 0385c6d05ba50210b0d51e991e81c7ea |
| dms_classification | delete | record |  | false | true | global | 009addc0830312108daa12a7522bc03a |
| dms_document_revision | read | record |  | false | true | global | 0152e76c83c312108daa12a7522bc0ce |
| dynamic_schedule_task_filter | write | record |  | false | true | global | 01214ebbd7213200d24b00285e61031c |
| e294fd997738911023651605bc5a9937 | execute | 6d9c40e9531210101cb3ddeeff7b12f6 |  | false | true | c8ab76825371201032b7ddeeff7b1280 | 02e435d97738911023651605bc5a99d4 |
| e6f6be067778111023651605bc5a996f | execute | 6d9c40e9531210101cb3ddeeff7b12f6 |  | false | true | c8ab76825371201032b7ddeeff7b1280 | 0323c38e7778111023651605bc5a99bd |
| ecc_action | read | record |  | false | true | global | 000a6acb774012104c781b699a5a993a |
| ecc_agent_issue | write | record |  | false | true | global | 00a50f287f3322002dedbb87adfa91de |
| ecc_queue_config | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 03ab870b77c012104c781b699a5a9985 |
| ecc_queue_usage_analytics | read | record |  | false | true | global | 017371e87f045210cc0b38b8ec866502 |
| experiment.opt_out | write | record |  | false | true | global | 01eda069932312107b4e572184891829 |
| fc5be914936116104d0a423b92891849 | execute | 6d9c40e9531210101cb3ddeeff7b12f6 |  | false | true | 757c34719bf7f10c4a1f9fe81ba8bba3 | 036ced94936116104d0a423b92891864 |
| ga_guidance | read | record |  | false | true | fd76ed5a3b570010119c870044efc470 | 0391905153630010763eddeeff7b129e |
| ga_guidance_input | delete | record |  | false | true | fd76ed5a3b570010119c870044efc470 | 02b95c9553630010763eddeeff7b1288 |
| gcf_staging | delete | record |  | false | true | 49d1d428e73233005765eef6c2f6a9eb | 00521076cb133300a54f78d5634c9ccb |
| gsw_status_of_content | read | record |  | true | true | 5f4ef4ed9f401200b18a7feea57fcfbe | 01de1b599f90120066dabde8132e7089 |
| help_setup_dependency | create | record |  | false | true | global | 026d6ef10f501210e7f2da1e68767eed |
| help_user_interaction_step | read | record |  | false | true | global | 03a48737c3445210baa38ec18d40dd0a |
| interaction_queue_transfer | write | record |  | false | true | global | 02885a6437001300a213a7f07e41f196 |
| interaction_relationship_policy | create | record |  | false | true | global | 01a608446f31211026b95d3a945b36ee |
| ip_address_range | read | record |  | false | true | global | 0096a7e95b2b011048501e991e81c74f |
| ip_service_affinity | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 01d39a545be50210b0d51e991e81c7c6 |
| itom_lu_definition_usage_count | create | record |  | false | true | global | 0243c2414765c290c62e37d2846d43f9 |
| itom_lu_definition_usage_count | read | record |  | false | true | global | 02f44ac14765c290c62e37d2846d434c |
| jwt_provider.* | write | record |  | false | true | global | 01273099b7731300616ceb67ee11a900 |
| kb_feedback | delete | record |  | false | false | global | 03afba920a00070400842d23a2d6eb3f |
| kb_feedback | read | record |  | false | false | global | 03a3ae120a000704015034e42019627a |
| kb_feedback | write | record |  | false | false | global | 03a553d80a00070400119b16fc8aac59 |
| kb_feedback.* | write | record |  | false | false | global | 03a7d0ea0a00070400c9ca3377c6747a |
| kb_feedback.flagged | write | record |  | false | false | global | 03a7f69b0a000704017c506871b10178 |
| kb_feedback.work_notes | write | record |  | false | true | global | 03aa99c60a000704006e8230b942baab |
| kb_knowledge_base | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 02d46181c70010108ad4010703c260a5 |
| kb_navons | create | record |  | false | true | global | 03ac96ef0a00070401b9d1127bd48343 |
| kb_navons | delete | record |  | false | true | global | 03af71070a00070400fd3c63a548f787 |
| kb_navons | read | record |  | false | true | global | 03adb1320a000704009073fc59032685 |
| kb_navons | write | record |  | false | true | global | 03ad0cbf0a0007040145499bdfa006ad |
| kb_social_qa_view | delete | record |  | true | true | 11722b01473231007f47563dbb9a7154 | 00b2565c477002007f47563dbb9a71a2 |
| kb_use | create | record |  | false | true | global | 03ae60d40a0007040097b03343d714af |
| kb_use | delete | record |  | false | true | global | 03af25ab0a00070401e100ae0da80622 |
| kb_use | read | record |  | false | true | global | 03ae484e0a000704008052a5de12b14e |
| kb_use | write | record |  | false | true | global | 03ae7a3c0a000704009e5fed83f82d19 |
| knowledge_based_question_service_mapping | read | record |  | false | true | global | 013ae49bff7722103670ffffffffff10 |
| license_has_user_set | read | record |  | false | true | global | 00c2e8f39f3302001526317f842e7028 |
| live_mention | delete | record |  | false | true | global | 03a66a3083c312109d5adbe4d12bc05c |
| live_tag | create | record |  | false | true | global | 03076c217f1c1210461758066d8665fd |
| m2m_connected_category | read | record |  | true | true | global | 02a7261f77b01110cd1b756f1b5a99bc |
| m2m_document_user_approver | read | record |  | false | true | global | 01c59a2e838b52108daa12a7522bc0ba |
| m2m_sys_nlu_intent_entity | write | record |  | false | true | global | 0092e448ff5012106836ffffffffff6a |
| m2m_user_consent_info.* | read | record |  | false | true | global | 009afb597f310210864d8b2cac8665e7 |
| mid_k8s_deployment | delete | record |  | false | true | global | 03252da87fc05210cc0b38b8ec866594 |
| mid_k8s_deployment_hpav2_behavior_policies | write | record |  | false | true | global | 0181b9287f045210cc0b38b8ec8665fb |
| ml_autotrain_solution | create | record |  | false | true | global | 01a955ecb700001024280f98ee11a9fc |
| ml_label_user_feedback | read | record |  | false | true | 31f5f491c3a710100bf407720f40ddf4 | 034fdbba073c011028ef0a701ad3008a |
| ml_trainer_definition | create | record |  | false | true | global | 03a6c5c00b013200c7ecc71437673a5c |
| ml_word_vector_corpus | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 030e5f0653a321106e33ddeeff7b12c4 |
| multi_factor_criteria | delete | record |  | true | true | global | 0207268b73003300fdbd04fbc4f6a76e |
| nlq_synonym.table | delete | record |  | false | true | global | 01a650661b31301045d74195d34bcb28 |
| nlu_batch_test_utterance | delete | record |  | true | true | 31f5f491c3a710100bf407720f40ddf4 | 02fffcfe0773101028ef0a701ad30068 |
| nlu_performance_utterance_trace | create | record |  | false | true | 31f5f491c3a710100bf407720f40ddf4 | 02ee8d9173202010e6b632e954f6a75a |
| now.preview.form.* | read | b9eb8a1b873303002941b53046cb1234 |  | true | true | f53f19bac362fa22ca2e93692d32f18f | 0084607477a2301079ccdc3f58106158 |
| now.security-center-configuration.* | read | b9eb8a1b873303002941b53046cb1234 |  | false | true | a51d46e3f2014110366b10017c5ba675 | 01e4d34c932f0210d08813473289186e |
| oauth_credential.token | read | record |  | true | true | global | 02e25d530b20230001d36c4d37673a6c |
| oauth_entity | write | record |  | false | true | global | 0290da0693a012104de7335b448918c2 |
| oauth_entity_auth_scope_mapping | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 004a15ca7f6012107972dbd44d86658b |
| oauth_jwt_claims | write | record |  | false | true | global | 019d160693e012104de7335b4489189b |
| pa_calendars_retention | read | record |  | false | true | global | 0383bc02679e10106f023b4717415ad6 |
| pa_indicator_aggregate_excl | delete | record |  | false | true | global | 00d8281b434a1210dff8c4d05fb8f251 |
| pa_indicator_aggregate_excl | write | record |  | false | true | global | 00d8281b434a1210dff8c4d05fb8f24a |
| pa_indicator_aggregated_metrics | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 02a48e1cff0312101471fffffffffff0 |
| pa_m2m_indicator_tags | write | record |  | true | true | global | 01f7ea80bf201100b96dac808c07395a |
| pa_scores | delete | record |  | false | true | global | 03942680bf201100b96dac808c0739a9 |
| pa_scores.breakdown | 54f535270a0a0b8c007c67009ab2bdc0 | record |  | true | true | global | 03780cec9f13220090c2bb0e832e701b |
| pa_scores.indicator | 54f535270a0a0b8c007c67009ab2bdc0 | record |  | true | true | global | 012888ec9f13220090c2bb0e832e7075 |
| par_dashboard_widget | write | record |  | true | true | global | 005d606bc7610110f376a0736cc2607b |
| par_notification | delete | record |  | false | true | 9509c0e54e289e08608566160eb606cb | 03673eb86f16511089060168e25b3622 |
| pc_product_cat_item.product_id | write | record |  | false | true | global | 017e247437f03000158bbfc8bcbe5dea |
| product_instance_identifier_parameters | create | record |  | false | true | global | 02ffb74cebb1311007d5a1c6285228e5 |
| promin_breakdown_field | create | record |  | false | true | global | 03b07d0f53510010a980ddeeff7b1232 |
| promin_field_recommendation | read | record |  | false | true | global | 01b4940a77230210bf3589b28a5a9969 |
| promin_highlights_analysis_question | delete | record |  | true | true | global | 016a302b4fa12210c98b8a4a91ce0b26 |
| promin_highlights_question_metric_mapping | read | record |  | false | true | global | 033b346b4fa12210c98b8a4a91ce0bd8 |
| pwd_active_answer | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 0031ca56c72010100a9b5d83c7c260b8 |
| pwd_history | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 0186a95e73e054107d98438e7bf6a744 |
| pwd_identification_type | read | record |  | false | true | global | 01bb0cb0eb2201006a668c505206fe49 |
| pwd_question | read | record |  | false | true | global | 010cc7a8ebd0010045e1a5115206fe60 |
| pwd_user_lockout | write | record |  | false | true | global | 03b59a0deb1101006a668c505206fef0 |
| quickactions_action | read | record |  | false | true | global | 022013837f239210a3547cfb4d866576 |
| quickactions_workspace_action | delete | record |  | false | true | global | 007fe6daeb2033000c2c0c505206fe28 |
| sa_baselines | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 0335dcc977ebb910ea4d79ba2c5a99bd |
| sa_context_menu | create | record |  | false | true | global | 0169c48993011200b42e3b5b357ffb75 |
| sc_cat_item.workflow | write | record |  | true | true | global | 00cf4f4deb1211003623666cd206fed2 |
| sc_cat_item_catalog | create | record |  | false | true | global | 02843332c320110067ec37659bba8ff2 |
| sc_cat_item_company_mtom | delete | record |  | true | true | global | 00bdcea2eb9230003623666cd206fe2b |
| sc_cat_item_dt_approval | delete | record |  | false | true | global | 02adcaa2eb9230003623666cd206fed4 |
| sc_cat_item_dt_ext_mtom | delete | record |  | false | true | global | 01bd02e2eb9230003623666cd206fee5 |
| sc_cat_item_guide_items | read | record |  | true | true | global | 00b9d5b49312120042cf530b547ffbbe |
| sc_cat_item_subscribe_no_mtom | read | record |  | false | true | global | 03a89fac73c033004030e67bcaf6a7e7 |
| sc_homepage_renderer | create | record |  | false | true | global | 01324be2eb9230003623666cd206fec5 |
| sc_ic_question_choice | read | record |  | true | true | global | 02c9a48d470311002ee987e8dee490d3 |
| sc_item_variable_assignment | create | record |  | true | true | global | 02d7cda793a3020042cf530b547ffb3f |
| sc_req_item.* | write | record |  | false | true | global | 000c0fd51b262300985ba64fad4bcb35 |
| sc_request.comments | read | record |  | false | true | global | 010822261b8c35d0a4a92029274bcb0c |
| sc_request.comments | write | record |  | true | true | global | 03400ec11bc49c10985ba64fad4bcb64 |
| sc_service_fulfillment_step | write | record |  | false | true | global | 0363ab31c7a12010ca6da1e603c26019 |
| sc_template_detail | read | record |  | false | true | global | 01b80f92c7121010159ca1e603c2600e |
| sc_ts_query.* | read | record |  | false | true | global | 000c0fd51b262300985ba64fad4bcb3b |
| sc_ts_query.* | write | record |  | false | true | global | 000c0fd51b262300985ba64fad4bcb3c |
| scan_check_suite | read | record |  | false | true | global | 0136874b43701210bc26a9bb1cb8f2bc |
| service_availability | read | record |  | false | true | global | 02ac47ae43209a10b98152304bb8f2b2 |
| sku_metadata | write | record |  | false | true | bcadabf277f311109c62f5f3cb5a992a | 0061e2bd43e61210e777c91766b8f26d |
| sla_request | delete | record |  | false | true | global | 000c0fd51b262300985ba64fad4bcb48 |
| sla_request.* | read | record |  | false | true | global | 000c0fd51b262300985ba64fad4bcb46 |
| sla_request.* | write | record |  | false | true | global | 000c0fd51b262300985ba64fad4bcb47 |
| sla_timer_config | delete | record |  | false | true | 76d8e8b253320010a393ddeeff7b127b | 0226956753220010a393ddeeff7b12e9 |
| sm_flapper_strategy_data.* | create | record |  | false | true | global | 00e6ec409f8533000f51b7bda42e7079 |
| sm_order | write | record |  | false | false | global | 01970b21df203100dca6a5f59bf26363 |
| sn_ace_content_block_context | create | record |  | false | true | 5df6db91ebe4011090fa99602a52289e | 015eed74eb2f0110da1861c59c5228aa |
| sn_ace_page | write | record |  | false | true | 5df6db91ebe4011090fa99602a52289e | 023375b8eb2f0110da1861c59c5228b4 |
| sn_actsub_activity_type.target_field | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 01e8bf65648d5050f8772a8167d4cb95 |
| sn_actsub_activitytype_template | create | record |  | false | true | global | 0216928773870010e37d71ef64f6a7ae |
| sn_actsub_m2m_context_subobject | write | record |  | true | true | global | 01539027c743001093814865cb976396 |
| sn_actsub_source_context_mapping | read | record |  | false | true | global | 011d991aff786210d696ffffffffff51 |
| sn_aisearch_global_job_log | create | record |  | false | true | 3c467b5f0bf130109e0fa4e6e9c4c946 | 022da4dfb78d01107f033307fe11a9d9 |
| sn_aisearch_global_job_staging.state | write | record |  | false | true | 3c467b5f0bf130109e0fa4e6e9c4c946 | 03a53167b71101107f033307fe11a910 |
| sn_aisearch_global_migration_job | delete | record |  | false | true | 3c467b5f0bf130109e0fa4e6e9c4c946 | 005fd32eeb9891100cd8d3e647522803 |
| sn_apptmnt_booking_config_rule | create | record |  | false | true | d0f0c1303ba23200ce8a4d72f3efc4ac | 001ab95b7c430110fa9bc95958e5fd2e |
| sn_bm_client_recommendation_eval | f6861c32c0a8016400647951e901525d | record |  | false | false | 3ad18693db92220004997878f0b8f516 | 00071400775010100f7a72f9691061a2 |
| sn_bm_client_region | write | record |  | false | true | 3ad18693db92220004997878f0b8f516 | 01d79003431721107f9fbbfd6bb8f2dd |
| sn_cmdb_ws_base_aggregate_data | delete | record |  | false | true | c8ab76825371201032b7ddeeff7b1280 | 035cf47bb7012110b87e80408e11a955 |
| sn_cmdb_ws_class_icon | create | record |  | false | true | c8ab76825371201032b7ddeeff7b1280 | 0022b9bb37d72110f563825174924b9f |
| sn_cmdb_ws_feature_category_runtime_attribute | delete | record |  | false | true | c8ab76825371201032b7ddeeff7b1280 | 00f433cc77432110ee0d0cc2fa5a9909 |
| sn_cmdb_ws_feature_category_runtime_attribute | read | record |  | false | false | c8ab76825371201032b7ddeeff7b1280 | 01b9ff8f7fa41210cc4835c59c8665b2 |
| sn_cmdb_ws_imp_action_card_config | create | record |  | false | false | c8ab76825371201032b7ddeeff7b1280 | 00b93b8f7fa41210cc4835c59c8665ba |
| sn_cmdb_ws_imp_action_card_config.filter_conditions | write | record |  | false | true | c8ab76825371201032b7ddeeff7b1280 | 00cfc8e953632110b87eddeeff7b1255 |
| sn_cmdb_ws_nlq_excluded_table | create | record |  | false | false | c8ab76825371201032b7ddeeff7b1280 | 00b946737f241210640c144a5b8665db |
| sn_cmdb_ws_partial_payload_item | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | false | c8ab76825371201032b7ddeeff7b1280 | 01b9ff8f7fa41210cc4835c59c8665d3 |
| sn_cmdb_ws_quick_links | write | record |  | false | false | c8ab76825371201032b7ddeeff7b1280 | 01b9ff8f7fa41210cc4835c59c8665f4 |
| sn_cmdb_ws_reconcile_duplicate_template_suggested_task | write | record |  | false | true | c8ab76825371201032b7ddeeff7b1280 | 02e46adc779179103bce067f5b5a9910 |
| sn_cmdb_ws_service_graph_connector | create | record |  | false | false | c8ab76825371201032b7ddeeff7b1280 | 01b933cf7fa41210cc4835c59c866515 |
| sn_customercentral_cust_info_config | read | record |  | false | true | 7a9ab70373830010e37d71ef64f6a78b | 01b483a0732300109234c346c4f6a711 |
| sn_customerservice_appointment | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | 51d811fad7223100b7490ee60e61034f | 00eaa024530aa210f27eddeeff7b12a6 |
| sn_customerservice_case.resolved_by | write | record |  | false | true | 51d811fad7223100b7490ee60e61034f | 0208c97a1bef2780985ba64fad4bcb11 |
| sn_customerservice_case.short_description | read | record |  | false | true | 51d811fad7223100b7490ee60e61034f | 03547be7732023004a905ee515f6a762 |
| sn_customerservice_case.state | write | record |  | false | true | 51d811fad7223100b7490ee60e61034f | 020752b10f5a10105bc5e7b1d4767ee3 |
| sn_customerservice_responsibility_access_config.applies_to_relationship | 54f535270a0a0b8c007c67009ab2bdc0 | record |  | false | true | 51d811fad7223100b7490ee60e61034f | 0140660743152110911baf56aab8f2d8 |
| sn_dependentclient_application | delete | record |  | false | true | f1d83d71c700030089413952f0976370 | 01c06deac7a0030089413952f09763aa |
| sn_dependentclient_application.* | write | record |  | false | true | f1d83d71c700030089413952f0976370 | 0220e5eac7a0030089413952f09763b9 |
| sn_devstudio_user_preferences | create | record |  | true | true | 5d9789f3eb51310007e48c1cf106fe9e | 029e88d437002200612747efbe41f11e |
| sn_diagram_builder_spot | read | record |  | false | true | 1cf7ad026abf3abab12e761ddaa6e9df | 022491fea3c212105d51b85de31e61a2 |
| sn_diagram_builder_ui_action | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | 1cf7ad026abf3abab12e761ddaa6e9df | 005419fea3c212105d51b85de31e615b |
| sn_doc_pdf_template_mapping | create | record |  | false | true | 6a9ea833b763330088d9bc78ee11a88q | 02c9230fb73100101cadbc78ee11a944 |
| sn_doc_task_execution | read | record |  | true | true | 6a9ea833b763330088d9bc78ee11a88q | 02a27ca7c37611108787ac8b8640dd29 |
| sn_dt_translation_cache | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | 7d7635917313230052317a5454f6a76b | 0126962b7ff3121015b317b81d8665b3 |
| sn_employee_overview_section_field | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | 1e95bac2738f001001b566b90ff6a7cd | 00c55b3fe969a550f8772e47a4f52c64 |
| sn_employee_tab | delete | record |  | true | true | 1e95bac2738f001001b566b90ff6a7cd | 01700bd577e21110fedf8bb7cb5a9908 |
| sn_ex_sp_favorite_content_config | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | 4249e63a28d54d61bb6fbf61fd86cccb | 01e6ee309c802110f877e26fc0971081 |
| sn_ex_sp_footer | read | record |  | false | true | 4249e63a28d54d61bb6fbf61fd86cccb | 02cff21d73413010c94f54eb7df6a7b7 |
| sn_ex_sp_send_self_configuration | create | record |  | false | true | 4249e63a28d54d61bb6fbf61fd86cccb | 03051ef3079102104c73f5100ad30032 |
| sn_ex_sp_st_favorite | read | record |  | true | true | 4249e63a28d54d61bb6fbf61fd86cccb | 02ed0f12073101108d6d78e99cd3005e |
| sn_ex_sp_static_content_user_criteria_no_mtom | delete | record |  | false | true | 4249e63a28d54d61bb6fbf61fd86cccb | 0254e0e643ff2110816452cba5b8f21b |
| sn_ex_sp_todo_config_detail | write | record |  | false | true | 4249e63a28d54d61bb6fbf61fd86cccb | 00415c3fc341b0105a09f0ad9840ddad |
| sn_glider_ide_file_index.* | write | record |  | false | true | fd254d9443a161100967247e6bb8f200 | 02ec36c5fb302210f9d0f3acaeefdcc5 |
| sn_instance_clone_request | create | record |  | false | true | 31774a2953839110a6f8ddeeff7b12cb | 0146145c07122110fda37a76fed300fc |
| sn_km_mr_st_kb_knowledge | read | record |  | false | true | b3a70c8a530323004c36ddeeff7b124c | 039baaa987521010420e5cdac5cb0b62 |
| sn_nowassist_diagn_execution_result_message | create | record |  | false | true | 7b67ecf7437042105947644c7ab8f21b | 00373c77433002105947644c7ab8f204 |
| sn_nowassist_diagn_package | delete | record |  | false | true | 7b67ecf7437042105947644c7ab8f21b | 0308c0f67f110210ae3e0ee66d86656b |
| sn_ns_skill_config_ui | delete | record |  | false | true | 7c395aaa53003110453cddeeff7b123c | 016cb6b153b175104410ddeeff7b1253 |
| sn_pipeline_request_authorization_key | delete | record |  | false | true | e78853e9c3222010b83971e54440dd26 | 035f8f64c77a3010408bc8d6f2c260cd |
| sn_rf_record_display_configuration | read | record |  | false | true | 30a32ce6c7313010dd7ab6c427c2600e | 023d433e53b330107234ddeeff7b1216 |
| sn_rtbi_report_template.name | write | record |  | false | true | global | 01d322b39f7442104ec676308a0a1ca8 |
| sn_storage_cloud_consumption | create | record |  | false | true | 9641d1d043110210243f9cd82ab8f2ab | 029ae2e943150210243f9cd82ab8f2b8 |
| sn_sub_man_gen_ai_usage_details_aggregate | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | 86d7bb63ff021110468365d7d3b8fe41 | 029ceea19f1c121067b009923b0a1c2a |
| sn_sub_man_st_subscription_license_detail_metric | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | 86d7bb63ff021110468365d7d3b8fe41 | 038c6ef9432a1210e777c91766b8f2f1 |
| sn_sub_man_st_subscription_license_detail_metric | read | record |  | false | true | 86d7bb63ff021110468365d7d3b8fe41 | 038c6ef9432a1210e777c91766b8f2e4 |
| sn_templated_snip_note_template | write | record |  | true | true | 2d3597c80b67320036e62c7885673a43 | 01c796430b63320036e62c7885673ac4 |
| sn_vsc_best_practice_configurations | create | record |  | false | true | a51d46e3f2014110366b10017c5ba675 | 02e42211772631101b803a91fa5a992b |
| sn_vsc_changed_hardening_settings | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | a51d46e3f2014110366b10017c5ba675 | 009111565311211053a6ddeeff7b12d6 |
| sn_vsc_export_setting | delete | record |  | false | true | a51d46e3f2014110366b10017c5ba675 | 01c1761187721110adf7083f37cb0b23 |
| sn_vsc_mi_user_metrics | create | record |  | false | true | a51d46e3f2014110366b10017c5ba675 | 00aae87193af0210b633a3cd91891810 |
| sn_vsc_scan_comparisons | read | record |  | false | true | a51d46e3f2014110366b10017c5ba675 | 0197aaaa53011110dd8eddeeff7b12fa |
| sn_wn_app_config_content_m2m | read | record |  | false | true | cb08e377eb9071106fb3951ff15228b8 | 0196b6bf9fc49e1003ea0a7e7a0a1c59 |
| sn_wn_content | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | cb08e377eb9071106fb3951ff15228b8 | 006f923b373d3110878cafdd84924b33 |
| sn_wn_content_media_m2m | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | cb08e377eb9071106fb3951ff15228b8 | 026fd23b373d3110878cafdd84924b6d |
| sp_css_include.* | write | record |  | false | true | global | 000c0fd51b262300985ba64fad4bcb55 |
| sp_js_include | read | record |  | false | true | global | 033709e0d7101200a9addd173e24d47b |
| sp_page_title_variable | create | record |  | false | true | global | 0198390867d4030023c82e08f585ef1c |
| sp_portal.search_results_configuration | 54f535270a0a0b8c007c67009ab2bdc0 | record |  | false | true | global | 02d58a0cc7231010393d265c95c260c4 |
| sp_row.* | write | record |  | false | true | global | 000c0fd51b262300985ba64fad4bcb6d |
| sp_search_facet_filter | delete | record |  | false | true | global | 00174d91b34203007a6de81816a8dce5 |
| sp_ui_formatter | read | record |  | false | true | global | 032ea2ff3c711210f8770959e7b8d798 |
| statemgmt_not_allow_ops | write | record |  | false | false | global | 0348e6a9930112102c4c098a5489187e |
| statemgmt_register_users | delete | record |  | false | false | global | 0348e6a9930112102c4c098a548918bf |
| std_change_proposal | delete | record |  | true | true | global | 0361d4c6ff300200b18affffffffffab |
| std_change_proposal | read | record |  | false | true | global | 008a4bedff700200b18affffffffffa6 |
| std_ticket_action_input | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | c9f1df5787f50010e0ef0cf888cb0b2c | 0099d669d48ea210f87704adede80e67 |
| sttrm_transition_condition | create | record |  | true | true | global | 003653274305021071353d1e2ab8f2c0 |
| subscription_detail | write | record |  | false | true | bcadabf277f311109c62f5f3cb5a992a | 00b8d82c770221107d731dd91e5a9999 |
| subscription_entitlement_audit_log | write | record |  | false | true | bcadabf277f311109c62f5f3cb5a992a | 0209eb4f777121107d731dd91e5a999f |
| svc_baseline_exclusion | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 0075f3a4ff702210f8d3ffffffffff42 |
| svc_extension_variable | create | record |  | false | true | global | 003f7960773c5210087379ba2c5a9939 |
| svc_recomputation_log | read | record |  | false | true | global | 03b17359536313003e38ddeeff7b12ea |
| sys_administrative_script_transaction | delete | record |  | true | true | global | 02fbab270fe30010a4dff00c97767e39 |
| sys_analytics_batch_state.* | read | record |  | false | true | global | 0298b7d57f310210864d8b2cac8665bb |
| sys_analytics_data_points_error.* | read | record |  | false | true | global | 034474ac7f8192103ff504866d86652d |
| sys_analytics_trigger_definition | write | record |  | true | true | global | 01ffb48f4321311010515042e9b8f299 |
| sys_api_access_scope | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 018bc805935012104de7335b4489180c |
| sys_api_collection | write | record |  | false | true | global | 02df2cf673133300fdfc066a4cf6a737 |
| sys_api_response | delete | record |  | false | true | global | 0020703a73133300fdfc066a4cf6a75e |
| sys_api_response_map | read | record |  | false | true | global | 0040343a73133300fdfc066a4cf6a7a6 |
| sys_api_stats_script | write | record |  | false | true | global | 033899d343341210a371a0246bb8f2b8 |
| sys_api_stats_whitelist | create | record |  | false | true | global | 0267fd429f002200ef4afa7dc67fcf3f |
| sys_app_scan_variable_type | delete | record |  | false | true | global | 02e0d2147ffc12100c5dffd73c8665ab |
| sys_app_template | write | record |  | false | true | global | 02e0d2147ffc12100c5dffd73c8665cc |
| sys_app_template_dependency_definition | read | record |  | false | true | global | 02e016147ffc12100c5dffd73c86650a |
| sys_app_template_output_var.type | write | record |  | false | true | global | 0016f6a40f1020108c9c5019c4767ea7 |
| sys_atf_modified_record_m2m | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 0046d9f543301210bc26a9bb1cb8f259 |
| sys_atf_modified_record_m2m | create | record |  | false | true | global | 02cca73753122300c792ddeeff7b1296 |
| sys_atf_step_performance_metrics | create | record |  | false | true | global | 0021e07fa3b17110571967d1361e6129 |
| sys_atf_step_performance_metrics | create | record |  | false | true | global | 01dd974a43301210bc26a9bb1cb8f2a7 |
| sys_atf_whitelist | write | record |  | false | true | global | 0201478543301210bc26a9bb1cb8f23d |
| sys_attachment_attribute | create | record |  | true | true | global | 00ef919da3531210984b9caef31e61ff |
| sys_attachment_soft_deleted | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 006d9e84a330121045bd9caef31e6150 |
| sys_audit_retention | write | record |  | false | true | global | 020c983a7f12121048dd0840ac8665b9 |
| sys_auth_mfa_context_mfa_factor_m2m | read | record |  | false | true | global | 00032e987721111029fc1646ba5a992d |
| sys_auth_profile_mapping | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 035bd6ad935012104de7335b44891884 |
| sys_aw_form_default_section | delete | record |  | false | true | global | 016a956d49945210f877085c5dc69d76 |
| sys_aw_master_config | create | record |  | false | true | global | 01cf36cb87c0130084aca571d5cb0b6a |
| sys_blocked_email_address | create | record |  | false | true | global | 01699cdcc33031105e1a6333d840dd07 |
| sys_call_chain | read | record |  | false | true | global | 00fcc54c534f0010b471ddeeff7b127b |
| sys_cb_topic | read | record |  | false | true | global | 03a9d93bb3333200f7d1a13816a8dc65 |
| sys_cs_ca_message | create | record |  | false | true | global | 01cd83cbeb361110da1861c59c5228d6 |
| sys_cs_ca_message | delete | record |  | false | true | global | 029e470feb361110da1861c59c52285f |
| sys_cs_collab_channel | read | record |  | false | true | 53b1b0e79761011018b2fa98c253afcc | 03450417379a92106cdecc4883924bb9 |
| sys_cs_collab_chat_webhook_registry | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | 53b1b0e79761011018b2fa98c253afcc | 029fefc8c3a121100f24c87af040ddf9 |
| sys_cs_collab_message_reaction | delete | record |  | true | true | 53b1b0e79761011018b2fa98c253afcc | 011bb53ec3713010fe394f877840ddae |
| sys_cs_dynamic_translation_virtual_agent.* | read | record |  | false | true | 7c395aaa53003110453cddeeff7b123c | 023b600bff231210f86dffffffffffb5 |
| sys_cs_message_tab_detail.last_read_message_id | write | record |  | false | true | global | 0194f9639f43121057bda426da0a1c1f |
| sys_cs_notification_delivery_channel | delete | record |  | false | true | global | 01609d34ffd13010635f056d793bf11e |
| sys_cs_vendor_client_adapter_configuration | create | record |  | false | true | global | 00a55f5b0b1013000e83c71437673a52 |
| sys_db_cache | delete | record |  | false | true | global | 031906814374121062e9927e8bb8f228 |
| sys_db_size_stats | delete | record |  | false | true | global | 005b516feb041210a8c99147c15228dd |
| sys_decision.* | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 022dd18c53920210dcd9ddeeff7b129e |
| sys_decision_multi_result | read | record |  | true | true | global | 02f66afd5393301097a3ddeeff7b1236 |
| sys_declarative_action_model_field | read | record |  | false | true | global | 00bd0d29c7411010bfbaf89f51c2601e |
| sys_declarative_action_payload_definition | write | record |  | false | true | global | 00c52b2243611110bbc664746ab8f27a |
| sys_destination_preference | delete | record |  | false | true | global | 018fa6825b1210103a9b51d11581c7fb |
| sys_dm_job | write | record |  | false | true | global | 0269f57aeb401210a8c99147c152283d |
| sys_export_set | write | record |  | false | true | global | 01c3e0037f42310036bfdd620efa915d |
| sys_flow_context | read | record |  | true | true | global | 00a26b38cbb23200a30bb895634c9c47 |
| sys_frequency | create | record |  | false | true | global | 0232cbe2eb9230003623666cd206fe99 |
| sys_gen_ai_control_setting.* | write | record |  | false | true | global | 0076dd487f220210ee61def20d866522 |
| sys_gen_ai_detector_few_shot_pattern | read | record |  | false | true | global | 025c152953322210221a644b21f7b455 |
| sys_gen_ai_feature_mapping | create | record |  | false | true | global | 00bc8f84c7453110967a34c91dc26011 |
| sys_gen_ai_provider_preference | write | record |  | false | true | global | 008d582dff383210a3aeffffffffff00 |
| sys_gen_ai_text_cache | write | record |  | false | true | global | 0118378eff403210dda4ffffffffffb9 |
| sys_generative_ai_capability_definition | read | record |  | false | true | global | 0214bc07537121106b38ddeeff7b1262 |
| sys_glide_object | read | record |  | false | true | global | 00615b51c7511010bfbaf89f51c26057 |
| sys_global_file_hash | write | record |  | false | true | global | 02f013007fb012106b6f23a37d866594 |
| sys_guided_tour_analytics | create | record |  | false | true | global | 020925ca0b751300eed8635663673aaa |
| sys_guided_tour_analytics_event | delete | record |  | false | true | global | 01aea14a0b311300eed8635663673acc |
| sys_homepage_destination_rule.name | write | record |  | false | true | global | 01e059ca073201105fca5d1aead30007 |
| sys_hub_flow_designer_co_template | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 00c119f9432fc2107aec2cc4bab8f2f1 |
| sys_hub_ui_element | write | record |  | false | true | global | 034f61fd0f851010f4166fe7c4767e93 |
| sys_ih_external_webhook | read | record |  | true | true | global | 03a44f5077e02110b15a31cd6b5a99ef |
| sys_import_set | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 01a130000fe110108d2e0e52ff767eaf |
| sys_integration_metering_resource_exclusion | delete | record |  | false | true | global | 028759e01b1232104a226283b24bcbe4 |
| sys_ire_partial_payload_pattern | delete | record |  | false | true | global | 0325b200ff0522109da9ffffffffffbf |
| sys_logger_configuration | create | record |  | false | true | global | 009034c67fac5610f38254350d8665af |
| sys_m2m_email_report_attachment | delete | record |  | true | true | global | 000e6770ff602210a684ffffffffff57 |
| sys_nlu_intent | read | record |  | false | true | global | 00f4240cff5012106836ffffffffff2e |
| sys_nlu_intent.name | write | record |  | false | true | global | 018e090beb0220105de665fcc85228e2 |
| sys_nlu_model.display_name | write | record |  | false | true | global | 032cc1c7eb0220105de665fcc852284f |
| sys_notification_actionable_content | delete | record |  | false | true | global | 00062626c322201032dd09c77d40dde9 |
| sys_notification_next_experience_content.use_action | read | record |  | false | true | global | 00f9a8f753661110486fddeeff7b1222 |
| sys_nowmq_subject_param | create | record |  | false | true | global | 003c052cc3673010eeef3928bb40dd49 |
| sys_object_source | create | record |  | false | true | global | 0365e947ef70300098d5925495c0fb93 |
| sys_openapi_parameter_map | create | record |  | false | true | global | 020591f3875033001afc0a1d36cb0b35 |
| sys_openapi_request | delete | record |  | false | true | global | 01b9327c0fd03300c79ef140ff767eea |
| sys_page_theme.* | write | record |  | false | true | global | 008bb5dfff333010b0fde1602946bd82 |
| sys_pd_activity_override | create | record |  | false | true | global | 000f512ea3e01210b5911aaaf31e61ba |
| sys_pd_activity_type | delete | record |  | false | true | global | 019214d6a3281210b5911aaaf31e61d0 |
| sys_pdf_generation_status.context | create | record |  | false | true | global | 0116ae034350121037ca0c173bb8f240 |
| sys_pg_table_stats_config | delete | record |  | false | true | global | 01955406472032107a684bdb736d43a2 |
| sys_playbook_activity_renderer | write | record |  | false | true | global | 02fcc21dc7310010bfbaf89f51c260e6 |
| sys_playbook_experience_status_to_state | read | record |  | false | true | global | 02b73b57ff721010667053ea793bf131 |
| sys_progress_worker | read | record |  | false | true | global | 03941a19a31231108d80ad2f241e6161 |
| sys_recipient_user_mapping | delete | record |  | false | true | global | 01fa0fab7721111007737e567a5a9973 |
| sys_rel_source | write | record |  | false | false | global | 0248a6a9930112102c4c098a54891806 |
| sys_remote_scoped_plugin | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | 781f36a96fef21005be8883e6b3ee43d | 01926ee4a3713110db40cf40141e61a4 |
| sys_report_color | delete | record |  | false | true | global | 0203d6a4d7612100b96d45a3ce610331 |
| sys_report_map_condition | write | record |  | false | true | global | 01de8d41d7101200bd4a4ebfae6103af |
| sys_report_source | read | record |  | true | true | global | 001f5245c331210038bf506adfba8ff0 |
| sys_rest_csrf_allow_list | read | record |  | false | true | global | 005f08beff331210f8aaffffffffff1b |
| sys_run_level | read | record |  | false | true | global | 00ce4d2eb70320104c75ccf78e11a921 |
| sys_scheduler_job_history_node | write | record |  | false | true | global | 015c490b431b52102677642b75b8f21e |
| sys_scoped_admin_acl_inheritance | write | record |  | true | true | global | 02bf914d93932200c9a7db47c47ffbc1 |
| sys_search_filter | create | record |  | false | true | global | 00a98c265b031010e91728582d81c705 |
| sys_search_suggestion_blacklist | create | record |  | false | true | global | 02d4e02a0f3323003d0e4062ff767e3b |
| sys_security_obj_oper | delete | record |  | false | true | global | 002b29a59f6412108647e8c40b0a1c1b |
| sys_security_table_level_audit | delete | record |  | false | true | global | 029d42f5935012100a004c52848918be |
| sys_sensitive_data_handling_regex | read | record |  | false | true | 91c0c191531b3010b6e8ddeeff7b127b | 02610c60eb153110101c378ab55228a3 |
| sys_service_endpoint_state | create | record |  | false | true | global | 0033723777221010bf05d4082b1061c7 |
| sys_sg_alp_quick_action_map | read | record |  | false | true | global | 03841beaff6b121065e6ffffffffffeb |
| sys_sg_calendar_screen | write | record |  | false | true | global | 00b4132eff6b121065e6ffffffffffd5 |
| sys_sg_custom_map_config | write | record |  | false | true | global | 02a49feaff6b121065e6ffffffffffb5 |
| sys_sg_function | write | record |  | false | true | global | 00a41feaff6b121065e6fffffffffffc |
| sys_sg_offline_result_m2m_mobile_responder | write | record |  | false | true | global | 02a49feaff6b121065e6ffffffffffd7 |
| sys_sg_popup | read | record |  | false | true | global | 0084d7eaff6b121065e6ffffffffff18 |
| sys_sg_screen_cache | create | record |  | false | true | global | 001bdc73531220106c1dddeeff7b1206 |
| sys_sg_time_span_item_stream | write | record |  | false | true | global | 01a45feaff6b121065e6ffffffffffe9 |
| sys_sg_ui_style | read | record |  | false | true | global | 03841beaff6b121065e6ffffffffffc9 |
| sys_token_auth_parameter | read | record |  | false | true | global | 0140c075934012104de7335b44891817 |
| sys_trend | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 024c551043531110563cd5bbdab8f23a |
| sys_ui_annotation | read | record |  | true | true | global | 012942110f130000b12e6903cfe0125b |
| sys_ui_element | create | record |  | false | true | global | 02d3e314531313008cd9ddeeff7b124c |
| sys_ui_hp_publisher | write | record |  | false | true | global | 01914903870331004ebe19fa84e3ec53 |
| sys_ui_macro.* | write | record |  | false | true | global | 03235d368763021019b2ed3e0ebb35d7 |
| sys_ui_module.* | read | record |  | false | true | global | 010c8fd51b262300985ba64fad4bcb51 |
| sys_ui_module.* | write | record |  | false | true | global | 010c8fd51b262300985ba64fad4bcb52 |
| sys_update_set_log | write | record |  | false | true | global | 029bf6087f3012106b6f23a37d86657e |
| sys_upgrade_app_version_history | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 006a6a8c7752211041758f368c5a99a7 |
| sys_user_group.* | read | record |  | false | true | global | 015885be1bef2780985ba64fad4bcbd3 |
| sys_ux_client_script_include | read | record |  | false | true | global | 0128ec63eb2301103c43d6e8b5522814 |
| sys_ux_data_broker_scriptlet | create | record |  | true | true | global | 03070cac934631103fce469f748918b3 |
| sys_ux_data_broker_transform | delete | record |  | false | true | global | 0326fb18930631103fce469f74891861 |
| sys_ux_m2m_workspace_header_ux_header_config | create | record |  | false | true | global | 033d59ed49945210f877085c5dc69db9 |
| sys_ux_ribbon_config | create | record |  | false | true | global | 021a0f3953dc1610c685ddeeff7b1236 |
| sys_ux_route_permission | delete | record |  | false | true | global | 01c5ccff77003010dd0359033f5a995e |
| sys_uxa_stats | create | record |  | false | true | global | 0136649c378e1210d1224ef1a4924bc0 |
| sys_variable_value | delete | record |  | false | true | global | 03a3e67253322200184e289e16dc34d8 |
| sys_web_service_input | write | record |  | false | true | global | 013bb80577330210497192f08e5a998b |
| sys_ws_header_map | read | record |  | false | true | global | 001a6ff267111200c4098c7942415a45 |
| sysauto_ms_report_builder | read | record |  | false | false | global | 024866a9930112102c4c098a548918b4 |
| sysevent_event_queue_map | read | record |  | false | true | global | 00ecb6b143901210249aa574a9b8f2b5 |
| sysevent_queue_param_definition | read | record |  | false | true | global | 0048bfcd43121210c4635de1e9b8f2c9 |
| sysevent_queue_param_definition | write | record |  | false | true | global | 01777f8d43121210c4635de1e9b8f21c |
| task.approval_set | read | record |  | false | true | global | 010c8fd51b262300985ba64fad4bcbbe |
| task.approval_set | write | record |  | false | true | global | 010c8fd51b262300985ba64fad4bcbbf |
| task.description | write | record |  | false | true | global | 010c8fd51b262300985ba64fad4bcbc0 |
| task_cmdb_ci_business_app | delete | record |  | false | true | global | 02a1b54e233210101488dc1756bf6516 |
| temp_cmdb_ci_disk | read | record |  | false | true | global | 031e69da5b101210b0d51e991e81c778 |
| temp_flow_debugger_script | delete | record |  | false | true | global | 02f408e3ff0122107d70ffffffffffae |
| text_search.* | read | record |  | false | true | global | 010c8fd51b262300985ba64fad4bcbd7 |
| text_search.* | write | record |  | false | true | global | 010c8fd51b262300985ba64fad4bcbd8 |
| transaction_call_chain | delete | record |  | false | true | global | 01dd13757f131010d185f3c26f2a0ca0 |
| trend_recommendation | write | record |  | true | true | da8f2ef273232300e64cc1f52ff6a78f | 038a665b73332300e64cc1f52ff6a7e1 |
| ts_c_10_0.* | write | record |  | false | true | global | 016cc7111b662300985ba64fad4bcb63 |
| ts_c_10_2.* | write | record |  | false | true | global | 016cc7111b662300985ba64fad4bcba3 |
| ts_c_13_1 | delete | record |  | false | true | global | 02719b951b262300985ba64fad4bcbba |
| ts_c_13_2 | delete | record |  | false | true | global | 0271db951b262300985ba64fad4bcb00 |
| ts_c_13_6.* | read | record |  | false | true | global | 0271db951b262300985ba64fad4bcbc9 |
| ts_c_17_0.* | write | record |  | false | true | global | 021d8b111b222300985ba64fad4bcbce |
| ts_c_17_1.* | write | record |  | false | true | global | 021d8b111b222300985ba64fad4bcbef |
| ts_c_18_9 | delete | record |  | false | true | global | 03915b591b262300985ba64fad4bcb25 |
| ts_c_19_7 | delete | record |  | false | true | global | 01a193991b262300985ba64fad4bcb04 |
| ts_c_20_0.* | write | record |  | false | true | global | 03a113d91b262300985ba64fad4bcb49 |
| ts_c_20_3 | create | record |  | false | true | global | 03a113d91b262300985ba64fad4bcbfa |
| ts_c_21_2 | create | record |  | false | true | global | 01b15bd91b262300985ba64fad4bcb58 |
| ts_c_21_3 | create | record |  | false | true | global | 01b15bd91b262300985ba64fad4bcb9e |
| ts_c_23_8 | delete | record |  | false | true | global | 02c1135d1b262300985ba64fad4bcb0c |
| ts_c_24_2.* | read | record |  | false | true | global | 00784d321baba380ea17dd3fbd4bcbed |
| ts_c_34_8 | create | record |  | false | true | global | 01060af91bef64104cd3a798bd4bcb08 |
| ts_c_34_8.* | write | record |  | false | true | global | 0106c6f91bef64104cd3a798bd4bcbff |
| ts_c_35_9 | delete | record |  | false | true | global | 00443c2e1b03011018ba748bd34bcb4a |
| ts_c_38_4 | create | record |  | false | true | global | 038b4a1f1b162110c979ecade54bcbe8 |
| ts_c_3_9 | delete | record |  | false | true | global | 022c0bd91b262300985ba64fad4bcbd3 |
| ts_c_3_9.* | read | record |  | false | true | global | 022c0bd91b262300985ba64fad4bcb84 |
| ts_c_42_6.* | read | record |  | false | true | global | 00f338e01b710210a4a92029274bcbf5 |
| ts_c_43_3 | create | record |  | false | true | global | 0124b4a41b710210a4a92029274bcb8b |
| ts_c_43_9.* | read | record |  | false | true | global | 022478a41b710210a4a92029274bcba8 |
| ts_c_44_1.* | read | record |  | false | true | global | 02958fc9fb742210f9d0f3acaeefdca5 |
| ts_c_45_0.* | read | record |  | false | true | global | 00a5434dfb742210f9d0f3acaeefdc0a |
| ts_c_46_2.* | read | record |  | false | true | global | 02a5038dfb742210f9d0f3acaeefdca9 |
| ts_c_47_6.* | read | record |  | false | true | global | 0267f39afb3222102ba6fc32beefdc82 |
| ts_c_49_0 | delete | record |  | false | true | global | 02c8dd201b5232104a226283b24bcb0b |
| ts_c_5_5 | delete | record |  | false | true | global | 023ccb9d1b262300985ba64fad4bcb14 |
| ts_c_5_7 | delete | record |  | false | true | global | 023c0f9d1b262300985ba64fad4bcb27 |
| ts_c_6_0.* | read | record |  | false | true | global | 004c47dd1b262300985ba64fad4bcbd2 |
| ts_c_6_2 | create | record |  | false | true | global | 004c87dd1b262300985ba64fad4bcb3e |
| ts_configuration | delete | record |  | false | true | global | 01b85aa153403300d0baddeeff7b1222 |
| ts_index_synonym_dictionary | delete | record |  | false | true | global | 034231e05301220025472c39e3dc34c8 |
| ts_query_kb.* | write | record |  | false | true | global | 010c8fd51b262300985ba64fad4bcbe6 |
| u_suppliers | create | record |  | false | true | global | 0253218c1b4d8410985ba64fad4bcb74 |
| ua_audit_stats | delete | record |  | false | true | global | 02e840540b00001024f8ae9b37673a94 |
| ua_entitlement | delete | record |  | false | true | global | 037745c353032200ef65cbaac2dc3460 |
| ua_ih_usage | delete | record |  | false | true | global | 00de7d94736b230075b6e6e24ff6a7c6 |
| ua_scripted_defn | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 038654b27f40221024de08776d86652f |
| ua_shared_service | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 014158fa7f00221024de08776d86658d |
| ua_sp_logouts | create | record |  | false | true | global | 0272117253012200376acbaac2dc3468 |
| usageanalytics_count | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 00b7b542eb13111090ec54c3b15228dd |
| user_criteria | read | record |  | false | true | 6a9ea833b763330088d9bc78ee11a88q | 022b3ebec75200107da20b3703c26019 |
| ux_framework_builder_api_experiences | execute | REST_Endpoint |  | false | true | global | 018ee562ff331010bb24108e793bf10d |
| v_pd_lane_condition_to_run | create | record |  | false | true | global | 02317df4c71301106fb2a0e55cc260e0 |
| v_st_popular_item.* | write | record |  | false | true | 2263a68187032300e0ef0cf888cb0b3f | 0336a8a61b03011045d74195d34bcbf5 |
| var_dictionary.* | read | record |  | false | true | global | 0094a7263b021000dada82c09ccf3d38 |
| wm_map_filters_config | create | record |  | true | true | global | 00a070207f202200068712f44efa912a |
| wm_order.u_wo_claim_status | write | record |  | false | true | global | 02b4e39b1b6af5105eeb7ea5464bcbb6 |
| wm_questionnaire.* | delete | record |  | false | true | global | 00f12e057f203200c57212f44efa914b |
| wm_task.location | write | record |  | true | true | global | 026bda371b23200050fdfbcd2c071301 |
| wm_task_scheduling_history | create | record |  | false | true | global | 01713abc77623010715517e91e5a996a |
| wm_task_tech_preference | 0997ab83733303005978e4b9cdf6a7b9 | record |  | false | true | global | 0253781e43bf31103ee6dddfcbb8f20b |
| ws_security_profiles_outbound | read | record |  | false | true | global | 00b6f1ca43b01210d3e933674bb8f267 |
| x_hpmms_hpdaas_apm_case_state_mappings | read | record |  | false | true | 1281fe89db169f00c3d6f9361d961925 | 0150d3991b097340985ba64fad4bcb05 |
