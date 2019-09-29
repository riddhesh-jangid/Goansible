import random
import string
import os
from register import registerObj
import writer

class cloudformation_stack_set:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    accounts = ''
    administration_role_arn = ''
    aws_access_key = ''
    aws_secret_key = ''
    capabilities = ''
    debug_botocore_endpoint_logs = ''
    description = ''
    ec2_url = ''
    execution_role_name = ''
    failure_tolerance = ''
    parameters = ''
    profile = ''
    purge_stacks = ''
    region = ''
    regions = ''
    security_token = ''
    state = ''
    tags = ''
    template = ''
    template_body = ''
    template_url = ''
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

