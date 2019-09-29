import random
import string
import os
from register import registerObj
import writer

class ec2_ami_facts:
    playbook_name = ''
    hosts=[]
    register=[]
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    describe_image_attributes = ''
    ec2_url = ''
    executable_users = ''
    filters = ''
    image_ids = ''
    owners = ''
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

