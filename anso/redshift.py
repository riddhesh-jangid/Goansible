import random
import string
import os
from register import registerObj
import writer

class redshift:
    playbook_name = ''
    hosts=[]
    register=[]
    command = ''
    identifier = ''
    allow_version_upgrade = ''
    automated_snapshot_retention_period = ''
    availability_zone = ''
    aws_access_key = ''
    aws_secret_key = ''
    cluster_parameter_group_name = ''
    cluster_security_groups = ''
    cluster_subnet_group_name = ''
    cluster_type = ''
    cluster_version = ''
    db_name = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    elastic_ip = ''
    encrypted = ''
    final_cluster_snapshot_identifier = ''
    new_cluster_identifier = ''
    node_type = ''
    number_of_nodes = ''
    password = ''
    port = ''
    preferred_maintenance_window = ''
    profile = ''
    publicly_accessible = ''
    region = ''
    security_token = ''
    skip_final_cluster_snapshot = ''
    username = ''
    validate_certs = ''
    vpc_security_group_ids = ''
    wait = ''
    wait_timeout = ''
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

