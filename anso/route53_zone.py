import random
import string
import os
from register import registerObj
import writer

class route53_zone:
    playbook_name = ''
    hosts=[]
    register=[]
    zone = ''
    aws_access_key = ''
    aws_secret_key = ''
    comment = ''
    debug_botocore_endpoint_logs = ''
    delegation_set_id = ''
    ec2_url = ''
    hosted_zone_id = ''
    profile = ''
    region = ''
    security_token = ''
    state = ''
    validate_certs = ''
    vpc_id = ''
    vpc_region = ''
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

