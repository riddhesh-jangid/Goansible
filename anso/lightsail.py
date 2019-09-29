import random
import string
import os
from register import registerObj
import writer

class lightsail:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    aws_access_key = ''
    aws_secret_key = ''
    blueprint_id = ''
    bundle_id = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    key_pair_name = ''
    profile = ''
    region = ''
    security_token = ''
    state = ''
    user_data = ''
    validate_certs = ''
    wait = ''
    wait_timeout = ''
    zone = ''
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

