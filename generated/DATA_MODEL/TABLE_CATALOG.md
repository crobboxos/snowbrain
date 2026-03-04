# Data Model Catalog

## Executive Narrative
This section captures schema composition, coupling intensity, and control surface per table.

## Full Data Model Register
| Table | Label | Fields | Reference Fields | Reference Ratio | Mandatory Fields | Mandatory Ratio | Business Rules | ACLs | Risk Score |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| kb_feedback | Knowledge Feedback | 1 | 0 | 0.0% | 0 | 0.0% | 1 | 6 | 30 |
| cmdb_ci_endpoint_biztalk | BizTalk Connection Endpoint | 4 | 3 | 75.0% | 0 | 0.0% | 0 | 0 | 13 |
| task_ordering_rule | Task Ordering Rule | 6 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 11 |
| ml_capability_definition_base | Solution Definition | 0 | 0 | 0.0% | 0 | 0.0% | 2 | 0 | 10 |
| problem | Problem | 0 | 0 | 0.0% | 0 | 0.0% | 2 | 0 | 10 |
| u_fd_articles_staged | FD Articles | 10 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 10 |
| clone_data_exclude | Clone Exclude Table | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 1 | 9 |
| sys_app_template_output_var | Template Output Variable | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 1 | 9 |
| sys_user_group | Group | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 1 | 9 |
| cmdb_ci_app_server_ora_ias_m | Oracle iAS Web module | 5 | 1 | 20.0% | 0 | 0.0% | 0 | 0 | 8 |
| cmdb_ci_lb_service | Load Balancer Service | 5 | 1 | 20.0% | 0 | 0.0% | 0 | 0 | 8 |
| sn_cmdb_ws_imp_action_card_config | CMDB WS Imp Action Card Config | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 2 | 8 |
| sys_atf_modified_record_m2m | Modified Record | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 2 | 8 |
| cmdb_ci_bundled_resources | Bundled Resources | 6 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 6 |
| ecc_agent_capability_m2m | MID Server Capability | 1 | 1 | 100.0% | 1 | 100.0% | 0 | 0 | 6 |
| sys_pd_context | Playbook Executions | 1 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 6 |
| sys_variable_value | Value | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 6 |
| unassignment_rule | Un-Assignment Constraint | 6 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 6 |
| agent_schedule_task_config | Event Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| awa_work_item | Work Item | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| license_cust_table_allotment | Custom Table Allotment | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| oauth_entity_profile_scope | Oauth Entity Profile Scope | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| pa_widgets | Widgets | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| par_indicator_model | Par Indicator Model | 3 | 0 | 0.0% | 1 | 33.3% | 0 | 0 | 5 |
| release_feature | Feature | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| sn_udc_collection_item | Collection Item | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| sys_cb_node | Goal Node | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| sys_pd_process_input | Playbook Inputs | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| sys_query_rewrite | Query Rewrite | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| sys_rte_eb_upper_case_operation | Robust Transform Engine Entity Upper Case Operation | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| sys_schema_attribute_m2m | Dictionary Attribute | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| sys_scope_design_access | Design Access | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| sys_sg_properties | Mobile Properties | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| sys_update_set | Update Set | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| sys_user_preference | User Preference | 0 | 0 | 0.0% | 0 | 0.0% | 1 | 0 | 5 |
| ts_c_35_9 | Text Index for ci_diagnostic_kb | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 5 |
| alm_custom_template_task | Custom Template Task | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| cmdb_ci_endpoint_oracle_tns | Oracle App TNS Service EP | 4 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 4 |
| cmdb_ire_data_source_rule | IRE Data Source Rule | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| cmdb_metadata_containment | CMDB Metadata Containment Rules | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| cmdb_multisource_recomp_task_ci | CMDB MultiSource Recompute Task CI | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| ecc_action | Action | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| ga_guidance_input | Guidance Input | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| nlu_batch_test_set | Nlu Batch Test Set | 2 | 0 | 0.0% | 1 | 50.0% | 0 | 0 | 4 |
| oauth_jwt_claims | OAuth JWT Claim Validation | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| pa_m2m_indicator_tags | Indicator Group | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| sa_context_menu | Menu Action | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| sc_cat_item_dt_approval | Execution Plan Approval Task | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| sn_doc_task_execution | Document Task Execution | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| sn_ex_sp_st_favorite | Favorite (App Use) | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| sn_glider_ide_file_index | IDE File Index | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| sn_nowassist_diagn_package | Nowassist Diagnostic Package | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| sn_vsc_scan_comparisons | Scan Comparisons | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| sn_wn_app_config_content_m2m | App Configuration Content | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| sys_cs_collab_channel | Collaboration Chat Channel | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| sys_development_permission | Development Permission | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 4 |
| sys_generative_ai_capability_definition | Generative AI Provider Mapping | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| sys_hub_ui_element | Flow Designer UI Element | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| sys_integration_metering_resource_exclusion | Integration Metering Resource Path Exclusions | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| sys_recipient_user_mapping | Recipient User Mapping | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| ts_c_17_1 | Text Index for sys_metadata | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| ts_c_43_3 | Text Index for sc_rest_api_without_access_policy | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| ts_c_44_1 | Text Index for promin_finding_def | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| ts_configuration | Text Index Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| ua_ih_usage | IntegrationHub usage | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| user_criteria | User Criteria | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| v_st_popular_item | Popular Item | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| wm_task_scheduling_history | Work Order Task Scheduling History | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 1 | 4 |
| db_audio | Audio | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 3 |
| sys_client_interaction0004 | Client Interaction | 3 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 3 |
| sys_client_interaction0005 | Client Interaction | 3 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 3 |
| sys_search_suggestion | Search Suggestion | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 3 |
| ts_c_34_1 | Text Index for sn_apptmnt_booking_lock | 3 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 3 |
| ts_table | Text Search Table | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 3 |
| ais_ingest_datasource_stats | AI Search Indexed Source History | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 2 |
| cmdb$par1 | Cmdb$par1 | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 2 |
| sc_ic_task_defn | Task Definition | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 2 |
| sc_wizard | Catalog Wizard | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 2 |
| sn_mif_sync_data | Sync Data | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 2 |
| sys_meta_graph_edge_restriction | Edge restriction | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 2 |
| sys_scheduler_job_history_node0001 | Scheduled Job History By Node | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 2 |
| ts_c_24_4 | Text Index for csm_consumer | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 2 |
| ais_relevancy_training_staging | AI Search Relevancy Training Staging | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| ar_cert_audit_result | Archive Audit Result | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| awa_service_channel_stats | AWA Service Channel Statistics | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| cmdb_ci_schedule_policy_template | Schedule Policy Template | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| cmdb_ci_win_cluster | Windows Cluster | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| command_has_transformer | Automation Pipeline Command Transformer | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| ecc_event_handler | Event Handler | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| sc_ic_task_assign_defn | Task Assignment Definition | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| sn_async_dashboard_alert_configuration | Event Alert Configuration | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| sn_nb_action_rule_context_group | Recommendation group | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| subscription_entitlement | Subscription Entitlement | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| sys_copied_base_upgrade_log_mapping | Copied-Base Upgrade Log Mapping | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| sys_development_permission_set | Development Permission Set | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| sys_domain | Domain | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| sys_report_access_request | Report Access Request | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| sys_ux_composite_data_m2m_datasource | EVAM Datasource M2M | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| sysevent_queue_stats | Sysevent Queue Stats | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| ts_c_14_0 | Text Index for kb_social_qa_question | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| ts_c_48_7 | Text Index for sn_dt_detection_cache | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 1 |
| ais_ingest_table_stats | AI Search Indexed Table History | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ais_retention_policy | AI Search Retention Policy | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ais_rule_mirror_m2m | Mirrored Result Improvement Rule | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ais_updatable_field_event | AI Search Updatable Field Event | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| alm_transfer_order_line_subtask | Transfer Order Line Subtask | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| antivirus_activity | Antivirus Activity | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| app_cmn_sort_option_config | Sort Option Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| appsec_hardening_guide_categories | Hardening Guide Categories | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| asmt_condition | Trigger Condition | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| asmt_decision_matrix | Decision Matrix | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| automation_pipeline_filter | Filter | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| awa_eligibility_pool | Assignment Eligibility | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| awa_instance_stats | AWA Instance Statistics | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| awa_queue_stats | AWA Queue Statistics | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| catalog_channel_analytics | Catalog Channel Analytics | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cdc_queue_ih | Integration Hub Change Queue | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cdc_queue_par0007 | PAR Data Model Change Queue | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cdc_queue_uxa_user_props0003 | UXA user properties Data Model Change Queue | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| clm_terms_and_conditions | Terms and Conditions | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| clone_cleanup_script | Clone Cleanup Script | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| clone_log0001 | Clone Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| clone_log0004 | Clone Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| clone_preserved_data | Preserved Data | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_agility_process | Agility Process | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_apic_host | Apic Host | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_app_server_hp_ucmdb | HP uCMDB | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_app_server_jrun_war | Jrun WAR | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_app_server_ora_ias | Oracle iAS | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_app_simulation | Simulation | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_app_simulation_inc | Simulation Inclusion | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_generic | Generic Application | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_ibm_wmq_queue | IBM WebSphere MQ Queue | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_rabbitmq_queue | RabbitMQ Queue | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_tibco_matrix | ActiveMatrix Business Works | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_business_capability | Business Capability | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_db_mssql_server | MS SQL Server | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_docker_local_image | Docker Local Image | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_email_server_ent_vault | Enterprise Vault | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_aq_queue | AQ Queue | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_cust_gateway | Customer Gateway Endpoint | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_docbase | DocBase Connection Endpoint | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_fastsearch | Fast Search Endpoint | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_http | HTTP(S) Endpoint | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_ssis_mssql | SSIS for MSSQL Endpoint | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_vnic | VNIC Endpoint | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_ip_switch | IP Switch | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_linux_server | Linux Server | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_mainframe | IBM Mainframe | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_network_acl_rule | Network ACL Rule | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_qualifier_hidden_conn | Hidden Connection Qualifier | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_qualifier_manual_connection | Manual Connection Qualifier | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_rack | Rack | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_resource_group | Resource Group | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_san_disk | SAN Disk | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_ups_bypass | UPS Bypass | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_vcenter_host_group | VMware vCenter Host Group | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_web_application | Web Application | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_web_server | Web Server | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_data_management_task_to_document | CMDB Data Manager Task to Document | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_dynamic_ire_feature | Dynamic IRE Feature | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_fc_target | Fibre Channel Targets | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_health_result_count | CMDB Health Result Count | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_health_result_group_map | CMDB Health Result Group Mapping | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_health_scorecard_group | CMDB Group Health Scorecard | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_import_set_run | CMDB Transform History | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_kvm_device | KVM Virtual Device | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_multilevel_queue | CMDB Multilevel Queue | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_multisource_query_result | CMDB Multisource Query Results | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_multisource_query_result_ms_record | CMDB Multisource Query Result Multisource Records | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_serviceorder_product_model | Service Order Model | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_switch_port | Switch Port | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_worktask_product_model | Work Task Model | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmn_building | Building | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| content_block_programmatic | Dynamic Content | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| content_css | Style Sheet | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| content_type | Content Type | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| csdm_dashboard_action_report_result | Application Services Action Result | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| csdm_dashboard_reports_result | Application Services Dashboard Result | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| data_replication_queue0000 | Data Replication Queue | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| discovery_probes_multi_probe | MultiProbe Included Probe | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| discovery_probes_snmp_field | SNMP Field | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| discovery_status_ecc_agent_m2m | Discovery Status MID servers | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| discovery_status_hthd | Help the Help Desk Status | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| dl_definition_rel_set | Setter Field Definitions | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| dl_matcher | Data Lookup Matcher Rules | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| dynamic_scheduling_config | Dynamic Scheduling Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ecc_agent_capability_value_test | MID Server Capability Value Test | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ecc_agent_secure_access_audit_log | MID Server Secure Access Audit Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ecc_agent_sync_file | MID Server Synchronized File | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ecc_event0005 | Event | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| execution_plan_local | Task Sequencing | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| fm_log0007 | Financial Management Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| fm_rate_card | Rate Card | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| fx_configuration | FX Currency Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| fx_currency2_instance | FX Currency | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| hermes_client_metrics | Hermes Client Metrics | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| http_connection | HTTP(s) Connection | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| http_retry_conditions | Http Retry Conditions | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| iana_enterprise_numbers | IANA Enterprise Number | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| import_log0001 | Import Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| interaction_agent_status | Interaction Agent Status | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| interaction_agent_transfer | Interaction Agent Transfer | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| interaction_log | Interaction Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ip_address_list_item_m2m | List of IP addresses | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ip_exclusion | IP Exclusion | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| itam_asset_usage | Itam Asset Usage | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| jwt_verifier_map | Jwt Verifier Map | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| kb_2_sc | Related Catalog Items | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| kb_keyword | Knowledge keyword | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| label_history | Label History | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| label_table | Label Table | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| license_artifact | License Artifact | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| license_dashboard_inventory | License Dashboard Inventory | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| license_group_to_deleted_subscription | Deleted Subscription Group | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| license_kv_query | License Key Value Query | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| m2m_announcement_portal | Portal Announcements | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| m2m_app_config_theme | UX App Theme | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| m2m_approval_rule_group | Group Approver | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| m2m_bu_s_goals | M2m Business Uni Goals | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| m2m_kb_ci | Knowledge Related to Products | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| m2m_name_component | Name Component | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| map | Map | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| matching_dimension_for_assignment | Select Criterion | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| menu_section | Menu Section | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ml_advanced_solution_settings | Advanced Solution Setting | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ml_capability_definition_case_detail | Process Mining Transition Case Detail Definition | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ml_similarity_example | Similarity Example | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ml_solution_alert_stats | Ml Solution Alert Stats | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| multisso_request_parameter | Multisso Request Parameter | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| nlq_cmdb_implicit_relationship | Nlq CMDB Implicit Relationship | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| nlq_query_log0003 | NLQ Query Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| nlu_conflict_result | Nlu Conflict Result | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| oauth_oidc_external_token | OIDC External Token | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ola_monitors | OLA Monitors | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| one_api_service_plan_feature_edge | One Api Service Plan Feature Edge | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| one_api_variable_store | One Api Variable Store | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| open_nlu_driver_language | Open Nlu Driver Language | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| open_nlu_predict_log0003 | Open NLU Predict Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| open_nlu_predict_log0004 | Open NLU Predict Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| pa_m2m_widget_indicators | Breakdown Widget Indicator | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| pa_text_index_configurations | Performance Analytics Text Index Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| pa_text_indexes | Performance Analytics Text Index | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| par_component_filter | Par Component Filter | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| par_coreui_migration_bridge_sysauto | PAR Core UI Migration Scheduled Job Bridge | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| par_coreui_migration_deactivated_acl | PAR Core UI Migration Deactivated ACL | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| par_recommendation_user_action | Par Recommendation User Action | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| predictive_optimizer_log | Predictive Optimizer Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| problem_task | Problem Task | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| promin_control_flow_mapping | Control flow mapping | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| promin_log | Extract Data Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| promin_log0001 | Extract Data Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| promin_metered_usage_data | Promin Usage Data | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| promin_node | Process Node | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| proposed_change_verification_log0004 | Proposed Change Verification Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| provider_auth | Provider Auth | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| pwd_cred_store_param | Password Reset Credential Store Parameters | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sa_entry_point_ui_card | Service entry point UI card | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sa_notification0000 | Discovered Service Notification | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sc_cat_dt_app_group | Approving Groups | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sc_cat_dt_app_user | Approving Users | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sc_category_dept_no_mtom | Not Available for Departments | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sc_category_top_n | Dynamic category | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sc_item_produced_record | Item Produced Record | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sc_mobile_layout | Mobile Layout | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| scan_linter_check | Linter Check | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| scan_mute_rule_reason | Mute Reasons | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sg_studio_card_template | Mobile Studio Card Template | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sla_breakdown_by_assignment | SLA Breakdown By Assignment | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sm_config | SM Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sm_m2m_task_template_dependency | Service Order Task Template Dependency | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_actsub_activity | Activity | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_actsub_atype_attributes | Activity Type Attributes | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_admin_center_application | Application | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_bm_client_recommendation_indicator_m2m | Recommendation Indicator M2M | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_cmdb_ws_dm_certification_attribute_status | CMDB Certification Attribute Status | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_cmdb_ws_reconcile_duplicate_template_library | CMDB Workspace De-duplication template library | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_cmdb_ws_reconcile_duplicate_template_schedule | CMDB Workspace De-duplication template schedule | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_cmn_mo_map_overlay_data_item | Map Overlay Data Item | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_customercentral_card_config | Card Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_customercentral_list_config | List Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_customercentral_report_config | Report Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_customerservice_floor_data_load | Floor Data Load | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_customerservice_related_party_configuration | Related Party Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_customerservice_sales_order | Sales Order | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_dependentclient_app_plugin_map | App Dependency Client App Plugin Mapping | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_deploy_pipeline_scheduled_deployment | Scheduled Deployment | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_devstudio_navigation_module | Studio Navigation Module | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_diagram_builder_diagram_action_dependency | Diagram Action Dependency | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_diagram_builder_node_type_attribute | Node Type Attribute | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_docker_spoke_docker_webhook_answer_subflow | Docker Webhook Answer Subflow | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_ihub_data_mapping_definition | Integration Data Mapping Definition | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_instance_clone_log0001 | Clone Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_m2m_note_template_for_table | Note Template for Table | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_mif_application_trust_profile | Application Trust Profiles | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_nb_action_detail | Recommended Action Execution | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_nb_action_recommended_action | Recommendation | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_nowassist_diagn_artifact | Nowassist Diagnostic Artifact | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_nowassist_skill_config_type | Now Assist Skill Config Type | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_nowassist_skill_family | Now Assist Skill Family | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_preferred_table | Preferred Table | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_rf_recommendation_history | Recommendation History | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_sm_journal0002 | Secrets Management Journal | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_storage_tier_usage_details | Storage Tier Usage Detail | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_sub_man_st_gen_ai_metadata | Generative AI Metadata | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_uxa_channel_menu_mapping | Sn Uxa Channel Menu Mapping | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_vsc_security_check_categories | Security Check Categories | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_vsc_security_policy | Security Policy | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_vsc_security_policy_condition | Security Policy Condition | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_vsc_security_policy_notification | Security Policy Notification | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_wn_user_content_activity | User Content Activity | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| snpar_sched_export_v_scheduled_export_visualization | PAR Scheduled Visualization Export | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sp_angular_provider | Widget Angular Provider | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sp_documentation | Service Portal Documentation | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sp_instance_menu | Instance with Menu | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sp_instance_vlist | Instance of Simple List | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sp_metatag | Meta Tag | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ssa_activity_pattern | Activity Pattern | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| stage_set_table | Stage Set for Table | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| statemgmt_compat_actions | Compatible CI Actions | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| statemgmt_not_allow_actions | Not Allowed CI Actions | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| svc_extension | Deployment Extension Container | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| svc_model_obj_constraint | Service Model Constraint | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| svc_recomputation_log0001 | Service Recomputation Performance Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_activity0009 | Activity Event | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_analytics_app | User Experience Analytics App | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_analytics_channel | User Experience Analytics Channels | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_api_request_local | Local API Request | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_app_flow_template_mapping | Flow Template Mapping | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_app_scan_variable | Variable | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_app_template_output_var_instance | Template Output Variable Instance | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_app_template_spoke_configuration | Spoke Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_archive_destroy_run | Archive Destroy Run | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_archive_link_chunk | Link Archive and Destroy Chunk | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_atf_step_callable | Reusable Test Step | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_atf_test_result_step_callable | Reusable Step Result | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_attachment_doc | Attachment Document | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_authentication_factor | Authentication Factor Services | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_authenticator_certificate | Authenticator CA Certificate | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_aw_renderer | Workspace Renderer | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_broadcast_message | Broadcast Message | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_broadcast_msg_user_m2m | Broadcast Messages to Users | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_build_suggestion_log | Build Suggestion Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_cal_unit | Day of the Week | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_cb_topic_category | Topic Category | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_client_interaction | Client Interaction | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_client_interaction_details0000 | Client Interaction Details | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_cs_aia_step_log | AIA Step Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_cs_auto_resolution_simulation_run | Auto-Resolution Simulation Run | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_cs_channel_user_profile | Channel User Profile | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_cs_context_profile_group | Assistant hierarchy | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_cs_live_agent_setup | Chat Setup | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_currency_conversion_adapter_rule | Currency Adapter Rule | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_decision_question | Decision | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_delete_recovery | Delete Recovery | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_df_data_dictionary | DataFabric Data Dictionary | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_df_query_stats0003 | Data Fabric Query Stats | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_dm_table_name_rule | Table Name Configuration Rules | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_dm_table_pattern_rule | Table Pattern Configuration Rules | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_email_client_template | Email Client Template | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_email_reply_separator | Email Reply Separator | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_embed_object | Embed Object | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_execution_tracker | Execution Tracker | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_flow_cat_variable | Flow catalog variable | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_flow_data_definition | Data Definition | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_flow_email_trigger | Email Trigger | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_flow_runtime_state_chunk | Flow Runtime State Chunk | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_flow_rw_action | Flow Responder | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_gen_ai_filter_group | Generative AI Filter Group | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_generative_ai_metric | Generative AI Metric | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_generative_ai_request_validator | Generative AI Request Validator | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_generic_user_filter_criteria | Generic User Filter Criteria | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_geo_routing | Geo Routing | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_hub_action_instance_v2 | Action Instance V2 | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_hub_flow_logic_variable | Logic Variable | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_hub_flow_safe_edit | Flow Safe Edit | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_hub_flow_snapshot | Flow | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_hub_step_ext_output | Extended Step Output Variable | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_i18n_plugin_version_history | Plugin Version History | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_impex_map | Import Export Map | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_kaa_policy | Kaa Policy | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_metadata_volatility | Metadata Volatility Levels | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_mfa_factor | MFA Factor | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_mobile_devices | Mobile Devices | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_mutex_pattern | Slow Mutex | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_normalization_job | Normalization Job | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_nowmq_message_archive_test | NowMQ Test Message Archive | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_one_extend_rate_limit_count | One Extend Rate Limit Rule Count | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_package_dependency_m2m | Package dependency | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_pd_derivative | Derivative | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_pd_swim_lane | Process Definition Swim Lane | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_product_help_page | Help Page | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_properties_category_m2m | Category Property | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_query_index_hint | Index Hint Rewrite | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_query_performance_test_result | Query Performance Test Results | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_record_transformer_rule | Record Transformer Rule | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_report_value_alias | Report Value Alias | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_rollback_context | Rollback Context | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_rollback_incremental | Recorded Incremental Change | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_rte_eb_set_operation | Robust Transform Engine Entity Set Operation | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_rte_eb_to_boolean_operation | Robust Transform Engine Entity Convert to Boolean Operation | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_scheduler_job_history | Scheduled Job History | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_scheduler_job_history0003 | Scheduled Job History | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_scheduler_job_history0004 | Scheduled Job History | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_scheduler_job_history_node0006 | Scheduled Job History By Node | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_scope_master | Scope Master Definitions | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_search_genius_result_event_action | Genius Result Event Action | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_search_signal_result_event_action | Search Signal Result Event Action | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_search_source_event | Search Event per source | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_applet_launcher | Applet Launcher | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_badge_count | Badge Count | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_button_instance_carried_param_map | Function Instance carried param mapping | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_details_screen | Details screen | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_favorites_tab | Saved Tab | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_filter_condition_attribute | Filter Condition Attribute | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_global_search | Global Search Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_location_item_stream | Location item stream | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_master_item | Master Item | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_navigation | Navigation | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_parameter_screen | Parameter Screen | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_suggestion_rule | Index Suggestion Rule | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_transform_type_parameter | Transform type parameters | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_translated | Translated Name / Field | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_ui_hp_cascading_filter | Cascading Filter | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_ui_policy | UI Policy | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_uib_template_category | Builder Template Category | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_uib_toolbox_component | Builder Component | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_upgrade_history_log | Upgrade Details | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_user_grmember | Group Member | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_user_public_credential | User Public Credential | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_user_role_lic_attr | Role Subscription Attribute | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_ux_composite_data_template_predicate_bundle | EVAM View Config Bundle | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_ux_controller_preset | UX Controller Preset | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_ux_list_menu_config | UX List Menu Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_ux_screen_type | UX Screen Collection | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_ux_sitemap_definition | UX Sitemap Definition | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_ux_theme_property | UX Theme Property | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_uxa_filters | UXA Filters | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_viz_data_source_role | Visualization Data Sources Visibility | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sysauto_scan | Scheduled Scan | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sysevent_handler_node_stats | Event Handler Stats by Node | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| syslog0001 | Log Entry | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| syslog0005 | Log Entry | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| syslog_awa0000 | AWA Log | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| syslog_client_trans_det0004 | Client Transaction Detailed Log Entry | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| syslog_email0005 | Email Log Entry | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| syslog_transaction0004 | Transaction Log Entry | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| syslog_transaction_part_metrics0002 | Transaction Part Metrics | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sysrule_escalate | Service Level Agreement | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| task_service_offering | Service Offerings | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| taxonomy | Taxonomy | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_attachment | Ts Attachment | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_19_5 | Text Index for kb_knowledge | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_20_4 | Text Index for sys_user_group | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_21_4 | Text Index for core_company | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_27_0 | Text Index for sn_apptmnt_booking_service_config | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_29_5 | Text Index for unassignment_rule | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_32_0 | Text Index for user_registration_request | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_32_4 | Text Index for user_registration_request | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_34_9 | Text Index for sn_apptmnt_booking_lock | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_39_9 | Text Index for ci_diagnostic_category | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_41_0 | Text Index for sys_package | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_42_1 | Text Index for sys_app_version | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_45_8 | Text Index for promin_project | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_45_9 | Text Index for promin_project | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_48_8 | Text Index for sn_dt_detection_cache | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_48_9 | Text Index for sn_dt_detection_cache | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_49_8 | Text Index for sys_suite_config_app_version_m2m | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_4_8 | Text Index for live_message | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_5_8 | Text Index for kb_keyword | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_6_3 | Text Index for sla | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_9_4 | Text Index for sc_ic_category_request | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_9_9 | Text Index for sc_ic_category_request | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_index_group | Text Index Group | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_phrase | Ts Phrase | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_search_summary | Text Search Summaries | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_synonym_set | Synonym Set | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| u_cmdb_ci_headset | Headset | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| u_cmdb_ci_keyboard | Keyboard | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| u_domain | Customer Domain | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| u_imp_tmpl_sm_part_requirement | Imp Tmpl Sm Part Requirement | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| u_imp_tmpl_sys_ui_bookmark | Imp Tmpl Sys UI Bookmark | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| u_inbound_xsm_accounts | Inbound Xsm Accounts | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| u_rikkyo_asset_import_v2 | Rikkyo Asset Import V2 | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| u_user_clearance_list | User Clearance List | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| u_xeretec_bundle_load | Xeretec Bundle Load | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ua_prod_inst | Related production instance | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| v_db_trigger | Database Trigger | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| v_field_creator | Create Field | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| v_metadata_parent | File Parent | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| v_private_cache | Private Cache | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| v_shared_cache | Shared Cache | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| vendor_type | Vendor Type | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| wf_estimated_runtime_config | Workflow Estimated Runtime Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| wf_log0001 | Workflow Log Entry | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| wf_workflow_schedule | Workflow Schedule | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| wm_agent_schedule_attribute_plan | Resource Schedule Attribute | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| wm_work_order_task_potential_assignment_groups | Work Order Task Potential Assignment Groups | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| zing_to_ais_configuration | Zing To AI Search Configuration | 0 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_output_0401c3d21b4070103cbb8404604bcb12 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_flow_output_080283d553839110c271ddeeff7b1217 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_flow_variable_080283d553839110c271ddeeff7b1217 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_cf9b325c176ed755df095a2310594f1f |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_atf_performance_stat_transaction |  | 3 | 1 | 33.3% | 0 | 0.0% | 0 | 0 | 0 |
| sys_atf_step_performance_metrics |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ecc_queue_config |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_vcenter_folder |  | 3 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_db_mssql_int_job |  | 6 | 1 | 16.7% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_now_app |  | 6 | 1 | 16.7% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_xenapp_comp |  | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_itsm_workspace_freshdesk_history |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_service_calculated |  | 8 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_customerservice_registration |  | 8 | 2 | 25.0% | 4 | 50.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_input_f76d83e91d124110fa9b62c1c4a8a9a9 |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| cmdb_ci_printer |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_atf_agent |  | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_health_config |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_flow_input_840bf44977a33300d4bdaeca78106104 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_email_address_filt_except |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| sys_email_client_from_address |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_input_7ffcd850776730104b68b0fabe5a998a |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| var__m_sys_hub_flow_input_c6dc0c6a9b1230100290af417ef04b7d |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_846d8f1d574232b466c91e1dc56ed1e4 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| syslog_transaction0006 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_action_output_832691120f2c7300c760001ea8767e4b |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_input_08172932c35219104c13cc57bb40dd80 |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| var__m_sys_hub_flow_input_c41741ec57801110403e8f90ac94f9c6 |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| sys_rw_action |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_rw_amb_action |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_user_presence |  | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_pdf_generation_status |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_sap_bo_srv |  | 3 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_now_app_comp |  | 5 | 2 | 40.0% | 0 | 0.0% | 0 | 0 | 0 |
| dscy_router_interface |  | 6 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_ca |  | 5 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_service |  | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| pa_snapshots |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| pa_tags |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| pa_target_color_schemes |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_ui_parameter |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| v_index_creator |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_pd_snapshot |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_output_c4249b6c1b86d210f39764e5604bcb97 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_cs_message_notification |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_biztalk_orch |  | 5 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_lb_modjk |  | 5 | 1 | 20.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_iisdirectory |  | 6 | 2 | 33.3% | 0 | 0.0% | 0 | 0 | 0 |
| discovery_log |  | 2 | 1 | 50.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_pd_activity_type_prop_2f19c1c7ff2022109a9affffffffff4c |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_430c13c072108799d48a4d0306fd9f80 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_1e3c489455e2a3c3e4f0f117155e74ce |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| service_offering |  | 5 | 2 | 40.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_e9342270aad7ea0debe37b4586e7d18d |  | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_action_input_b21f0b487772330038e286a268106109 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_service_discovered |  | 2 | 0 | 0.0% | 1 | 50.0% | 0 | 0 | 0 |
| var__m_sys_hub_trigger_output_c43a1011c36813002841b63b12d3ae15 |  | 1 | 1 | 100.0% | 1 | 100.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_8b23aee49bf4f935ea8e7eae54c654a2 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_critical_update |  | 3 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_embedded_help_content |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_input_a783a016b73702106cdeef54ce11a958 |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| sys_cs_notification |  | 2 | 1 | 50.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_lvm_pool |  | 5 | 1 | 20.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_storage_node_element |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_tibco_queue |  | 5 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_output_2fa579fc5372101026b0ddeeff7b12d3 |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| var__m_sys_hub_action_input_07b905a487110300123eaf8e36cb0bab |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_4_7 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_flow_variable_b0809cc8b7a01210ccd26045de11a971 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| nlu_performance_ignored_clusters |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| nlu_conflict_definition |  | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_consumable_product_model |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| open_nlu_predict_dialog_act_feedback |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| ts_c_35_8 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_diagram_builder_configuration |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_data_source |  | 3 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_flow_input_00472786a33201106e1d0ace26fcda2b |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_nat |  | 2 | 1 | 50.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_routing_policy |  | 5 | 1 | 20.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_tibco_matrix_proc |  | 5 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_sa_dynamic_policy |  | 5 | 1 | 20.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_app_server_jb_module |  | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_output_43391dd26712101085409d6617415af2 |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| kb_navons |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_action_output_0b1c137e1b2cd810985ba64fad4bcbbc |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| u_cmdb_ci_phone_numbers |  | 4 | 1 | 25.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_action_input_8d330cfa0bff5810eb3903e193673a1c |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_navigation_section_destination_applet_launcher |  | 1 | 1 | 100.0% | 1 | 100.0% | 0 | 0 | 0 |
| sys_sg_navigation_section_m2m_destination |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_analytics_authentication |  | 2 | 0 | 0.0% | 1 | 50.0% | 0 | 0 | 0 |
| sn_nb_action_rule_context_group_strategy |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_2dd117a261c283e7ca3c3f18475e3d87 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| collaborator |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| connect_action |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_output_845af5625325301026b0ddeeff7b1252 |  | 3 | 0 | 0.0% | 1 | 33.3% | 0 | 0 | 0 |
| sm_flapper_strategy |  | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| upgrade_preview_app |  | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| upgrade_preview_schema_change |  | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_cmp_resource |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_action_output_e8e9b1baa30412106cdec213d51e612b |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| user_has_subscription |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_client_interaction0002 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_action_input_8068449c77e330104b68b0fabe5a999d |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_35ef56111b211100adca1e094f071315 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ml_solution_explainability |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_0169cbc9a05deab9210109505060336a |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_customerservice_case |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_input_b35ee7dadb4f5700dd14596e5e96191c |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| sn_apptmnt_booking_service_config |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| u_xe_customer_asset_update_ |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_action_output_73626ca0ff34121021faffffffffff9d |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_multisource_query_status |  | 6 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_cmdb_ws_integration_aggregate_data |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_m2m_model_substitute |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_ux_composite_datasource_filter |  | 1 | 1 | 100.0% | 1 | 100.0% | 0 | 0 | 0 |
| sys_ux_composite_data_template_predicate |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_ux_composite_data_template_predicaterequired_roles |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_scope_permission_set_role_assignment |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_flow_input_847740da143f5210f8779da9137d35c1 |  | 2 | 1 | 50.0% | 1 | 50.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_output_77680b896dc05210f877f9f76d0de368 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_24_1 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_b0501200de7d3b71d7af11191264799a |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_36_8 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| nlq_table_guesser_query_log0005 |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_output_c60ae43477d3330038e286a268106100 |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_input_3f6e738859482210f877a8ba01adddb6 |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_5a4d1f803669c9dd4a5f09bd1cb48fcd |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_8770333d46df328f0d9da8ae3a333245 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_action_output_b93f42810b30030085c083eb37673a63 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| u_xeretec_macd_import |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_14_1 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_flow_step_definition_input_6e61d40e73031300e6561afe2ff6a704 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| unlicensed_detail |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_flow_logic_ext_input_0c8337a51dd24110fa9b62c1c4a8a967 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_user_login_history |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_ux_lib_component |  | 2 | 1 | 50.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_output_3f76c5b0b3f0030024a3051a16a8dc41 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb |  | 2 | 2 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci |  | 3 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| knowledge_based_question_service_mapping |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| central_dispatch_config |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sc_ic_item_staging |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_37_3 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_37_1 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_script_vtable |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_flow_data_var_966e954c432121107f9fbbfd6bb8f26f |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_flow_output_d781b8b2dba0f8900ccf918cd3961936 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_instance_clone_request |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| var__m_sys_hub_flow_input_a206172a777516100239dbad6b5a99b8 |  | 1 | 1 | 100.0% | 1 | 100.0% | 0 | 0 | 0 |
| sys_hub_ui_section |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| sys_app_template |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_ssis |  | 4 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_weblogic_module |  | 5 | 3 | 60.0% | 1 | 20.0% | 0 | 0 | 0 |
| cmdb_ci_appl_sap_ascs |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_jboss |  | 5 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_hub_flow_output |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_hub_action_type_base |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_hub_category |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sn_ace_variable_28fa64f087cf0110a4a2c077f6cb0b40 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| par_export_job |  | 2 | 1 | 50.0% | 0 | 0.0% | 0 | 0 | 0 |
| syslog_transaction0007 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| u_xeretec_consumable_models |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_input_7f8ff52eff120110456d766cf43bf193 |  | 1 | 1 | 100.0% | 1 | 100.0% | 0 | 0 | 0 |
| sys_cs_control |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_action_input_15e10e5eff30311077a95dac793bf11e |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_output_3f92e5517332601026f6aa114df6a7f9 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_ga_guidance_input_bad37dc577191110e07f2a647a5a991e |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| ts_c_45_0 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sn_customerservice_u_cmdb_ci_laptop |  | 4 | 1 | 25.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_aws_account |  | 4 | 3 | 75.0% | 0 | 0.0% | 0 | 0 | 0 |
| statemgmt_ops_state_pri |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_app |  | 4 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_endpoint_xenapp |  | 5 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_32b80b9d07c75170f8e05f295c4b0e25 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_pd_activity_type_prop_293b5d5cb713001085f588e1de11a930 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_app_server_tomcat_war |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_weblogic_lb |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_wmb |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_websphere_portal |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_hp_sm_kb |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_ora_http |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| alm_transfer_order_line |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_store_app |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| wm_task_tech_preference |  | 2 | 0 | 0.0% | 1 | 50.0% | 0 | 0 | 0 |
| var__m_sn_ace_variable_76dddbc9c38501104b8e88c7c840dd9f |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_a92afd29e4d430f1f2b58b31b57b02c0 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_upgrade_history |  | 1 | 1 | 100.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_rw_action_related_table |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_ux_data_broker_rest_external |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_output_b7a478e5ffa0121021faffffffffff48 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_input_d673770153c0121074adddeeff7b1260 |  | 1 | 1 | 100.0% | 1 | 100.0% | 0 | 0 | 0 |
| var__m_sys_hub_action_output_1eb073af53d6301095f4ddeeff7b129a |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ml_agent_zero_aggregated_data |  | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| ml_language_x_prediction_result |  | 2 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_0643a9eccc0c6f5d5d2ff11bfa43c6fe |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_san_endpoint |  | 4 | 2 | 50.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_sun_dir_proxy_server |  | 4 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_output_04b79008db9b5b00dd14596e5e961974 |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| cmdb_ci_nas_file_system |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_route_table |  | 5 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_ora_report |  | 5 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_properties |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_gen_ai_metadata_document |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_lb_haproxy |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_ora_tnslsnr |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_app_server_dp_domain |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_step_ext_output_ffa9cc10772730104b68b0fabe5a997d |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| var__m_sys_hub_action_input_4cbdde101b52cc94ee26dd39cd4bcbc8 |  | 2 | 0 | 0.0% | 1 | 50.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_7854a9ea2e116fed4ccb497067da2a05 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_sys_hub_flow_input_a28fbb04c7333300fbe745ece8c26061 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_business_process |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| var__m_f6d7c2480a0a3ca60116d3ec01b40688 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_sg_font_glyph |  | 1 | 0 | 0.0% | 1 | 100.0% | 0 | 0 | 0 |
| var__m_sys_ux_lib_component_attr_26a4d05d7ce617ad4c19f3ce2bf823c1 |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_app_server_ora_ess |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_hp_index |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_vign_content_svr |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| sys_recipient_qualifier |  | 1 | 0 | 0.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_datapower_server |  | 6 | 1 | 16.7% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_snat_ip_pool |  | 5 | 1 | 20.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_appl_sendmail |  | 4 | 2 | 50.0% | 0 | 0.0% | 0 | 0 | 0 |
| cmdb_ci_peripheral |  | 4 | 1 | 25.0% | 0 | 0.0% | 0 | 0 | 0 |
