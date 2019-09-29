import random
import string
import os
from register import registerObj
import writer

class elb_network_lb:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    state = ''
    aws_access_key = ''
    aws_secret_key = ''
    cross_zone_load_balancing = ''
    debug_botocore_endpoint_logs = ''
    deletion_protection = ''
    ec2_url = ''
    listeners = ''
    profile = ''
    purge_listeners = ''
    purge_tags = ''
    region = ''
    scheme = ''
    security_token = ''
    subnet_mappings = ''
    subnets = ''
    tags = ''
    validate_certs = ''
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

