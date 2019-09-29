import random
import string
import os
from register import registerObj
import writer

class rds:
    playbook_name = ''
    hosts=[]
    register=[]
    command = ''
    region = ''
    apply_immediately = ''
    aws_access_key = ''
    aws_secret_key = ''
    backup_retention = ''
    backup_window = ''
    character_set_name = ''
    db_engine = ''
    db_name = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    engine_version = ''
    force_failover = ''
    instance_name = ''
    instance_type = ''
    iops = ''
    license_model = ''
    maint_window = ''
    multi_zone = ''
    new_instance_name = ''
    option_group = ''
    parameter_group = ''
    password = ''
    port = ''
    profile = ''
    publicly_accessible = ''
    security_groups = ''
    security_token = ''
    size = ''
    snapshot = ''
    source_instance = ''
    subnet = ''
    tags = ''
    upgrade = ''
    username = ''
    validate_certs = ''
    vpc_security_groups = ''
    wait = ''
    wait_timeout = ''
    zone = ''
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

