import random
import string
import os
from register import registerObj
import writer

class ec2_vpc_nat_gateway:
    playbook_name = ''
    hosts=[]
    register=[]
    allocation_id = ''
    aws_access_key = ''
    aws_secret_key = ''
    client_token = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    eip_address = ''
    if_exist_do_not_create = ''
    nat_gateway_id = ''
    profile = ''
    region = ''
    release_eip = ''
    security_token = ''
    state = ''
    subnet_id = ''
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

