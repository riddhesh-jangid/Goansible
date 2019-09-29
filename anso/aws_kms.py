import random
import string
import os
from register import registerObj
import writer

class aws_kms:
    playbook_name = ''
    hosts=[]
    register=[]
    alias = ''
    aws_access_key = ''
    aws_secret_key = ''
    clean_invalid_entries = ''
    debug_botocore_endpoint_logs = ''
    description = ''
    ec2_url = ''
    enabled = ''
    grant_types = ''
    grants = ''
    key_id = ''
    mode = ''
    policy = ''
    profile = ''
    purge_grants = ''
    purge_tags = ''
    region = ''
    role_arn = ''
    role_name = ''
    security_token = ''
    state = ''
    tags = ''
    validate_certs = ''
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

