import random
import string
import os
from register import registerObj
import writer

class sts_assume_role:
    playbook_name = ''
    hosts=[]
    register=[]
    role_arn = ''
    role_session_name = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    duration_seconds = ''
    ec2_url = ''
    external_id = ''
    mfa_serial_number = ''
    mfa_token = ''
    policy = ''
    profile = ''
    region = ''
    security_token = ''
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

