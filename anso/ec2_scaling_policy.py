import random
import string
import os
from register import registerObj
import writer

class ec2_scaling_policy:
    playbook_name = ''
    hosts=[]
    register=[]
    asg_name = ''
    name = ''
    state = ''
    adjustment_type = ''
    aws_access_key = ''
    aws_secret_key = ''
    cooldown = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    min_adjustment_step = ''
    profile = ''
    region = ''
    scaling_adjustment = ''
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

