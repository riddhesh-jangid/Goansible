import random
import string
import os
from register import registerObj
import writer

class aws_secret:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    description = ''
    ec2_url = ''
    kms_key_id = ''
    profile = ''
    recovery_window = ''
    region = ''
    rotation_interval = ''
    rotation_lambda = ''
    secret = ''
    secret_type = ''
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

