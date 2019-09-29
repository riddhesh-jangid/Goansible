import random
import string
import os
from register import registerObj
import writer

class rds_instance:
    playbook_name = ''
    hosts=[]
    register=[]
    db_instance_identifier = ''
    allocated_storage = ''
    allow_major_version_upgrade = ''
    apply_immediately = ''
    auto_minor_version_upgrade = ''
    availability_zone = ''
    aws_access_key = ''
    aws_secret_key = ''
    backup_retention_period = ''
    ca_certificate_identifier = ''
    character_set_name = ''
    copy_tags_to_snapshot = ''
    creation_source = ''
    db_cluster_identifier = ''
    db_instance_class = ''
    db_name = ''
    db_parameter_group_name = ''
    db_security_groups = ''
    db_snapshot_identifier = ''
    db_subnet_group_name = ''
    debug_botocore_endpoint_logs = ''
    domain = ''
    domain_iam_role_name = ''
    ec2_url = ''
    enable_cloudwatch_logs_exports = ''
    enable_iam_database_authentication = ''
    enable_performance_insights = ''
    engine = ''
    engine_version = ''
    final_db_snapshot_identifier = ''
    force_failover = ''
    force_update_password = ''
    iops = ''
    kms_key_id = ''
    license_model = ''
    master_user_password = ''
    master_username = ''
    monitoring_interval = ''
    monitoring_role_arn = ''
    multi_az = ''
    new_db_instance_identifier = ''
    option_group_name = ''
    performance_insights_kms_key_id = ''
    performance_insights_retention_period = ''
    port = ''
    preferred_backup_window = ''
    preferred_maintenance_window = ''
    processor_features = ''
    profile = ''
    promotion_tier = ''
    publicly_accessible = ''
    purge_cloudwatch_logs_exports = ''
    purge_tags = ''
    read_replica = ''
    region = ''
    restore_time = ''
    s3_bucket_name = ''
    s3_ingestion_role_arn = ''
    s3_prefix = ''
    security_token = ''
    skip_final_snapshot = ''
    snapshot_identifier = ''
    source_db_instance_identifier = ''
    source_engine = ''
    source_engine_version = ''
    source_region = ''
    state = ''
    storage_encrypted = ''
    storage_type = ''
    tags = ''
    tde_credential_arn = ''
    tde_credential_password = ''
    timezone = ''
    use_latest_restorable_time = ''
    validate_certs = ''
    vpc_security_group_ids = ''
    wait = ''
    def compile(self):
       self.playbook_name=writer.writer(self,self.playbook_name)

    def run(self):
       dump_name=''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
       os.system('{} | tee {}'.format(self.playbook_name,dump_name))
       self.register = registerObj(dump_name)
       os.remove(dump_name)

    def go(self):
       self.compile()
       self.run()
