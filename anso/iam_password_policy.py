import random
import string
import os
from register import registerObj
import writer

class iam_password_policy:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    allow_pw_change = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    min_pw_length = ''
    profile = ''
    pw_expire = ''
    pw_max_age = ''
    pw_reuse_prevent = ''
    region = ''
    require_lowercase = ''
    require_numbers = ''
    require_symbols = ''
    require_uppercase = ''
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

