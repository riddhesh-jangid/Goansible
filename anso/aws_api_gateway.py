import random
import string
import os
from register import registerObj
import writer

class aws_api_gateway:
    playbook_name = ''
    hosts=[]
    register=[]
    api_id = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    deploy_desc = ''
    ec2_url = ''
    profile = ''
    region = ''
    security_token = ''
    stage = ''
    state = ''
    swagger_dict = ''
    swagger_file = ''
    swagger_text = ''
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

