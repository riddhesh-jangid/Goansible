import random
import string
import os
from register import registerObj
import writer

class elb_application_lb:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    access_logs_enabled = ''
    access_logs_s3_bucket = ''
    access_logs_s3_prefix = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    deletion_protection = ''
    ec2_url = ''
    http2 = ''
    idle_timeout = ''
    listeners = ''
    profile = ''
    purge_listeners = ''
    purge_rules = ''
    purge_tags = ''
    region = ''
    scheme = ''
    security_groups = ''
    security_token = ''
    state = ''
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

