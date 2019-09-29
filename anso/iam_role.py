import random
import string
import os
from register import registerObj
import writer

class iam_role:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    assume_role_policy_document = ''
    aws_access_key = ''
    aws_secret_key = ''
    boundary = ''
    create_instance_profile = ''
    debug_botocore_endpoint_logs = ''
    description = ''
    ec2_url = ''
    managed_policy = ''
    path = ''
    profile = ''
    purge_policies = ''
    region = ''
    security_token = ''
    state = ''
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

