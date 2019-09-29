import random
import string
import os
from register import registerObj
import writer

class ec2_vpc_vgw:
    playbook_name = ''
    hosts=[]
    register=[]
    asn = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    name = ''
    profile = ''
    region = ''
    security_token = ''
    state = ''
    tags = ''
    type = ''
    validate_certs = ''
    vpc_id = ''
    vpn_gateway_id = ''
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

