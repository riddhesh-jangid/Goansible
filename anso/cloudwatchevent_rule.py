import random
import string
import os
from register import registerObj
import writer

class cloudwatchevent_rule:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    description = ''
    ec2_url = ''
    event_pattern = ''
    profile = ''
    region = ''
    role_arn = ''
    schedule_expression = ''
    security_token = ''
    state = ''
    targets = ''
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

