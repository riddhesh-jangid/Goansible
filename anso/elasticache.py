import random
import string
import os
from register import registerObj
import writer

class elasticache:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    state = ''
    aws_access_key = ''
    aws_secret_key = ''
    cache_engine_version = ''
    cache_parameter_group = ''
    cache_port = ''
    cache_security_groups = ''
    cache_subnet_group = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    engine = ''
    hard_modify = ''
    node_type = ''
    num_nodes = ''
    profile = ''
    region = ''
    security_group_ids = ''
    security_token = ''
    validate_certs = ''
    wait = ''
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

