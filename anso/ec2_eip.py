import random
import string
import os
from register import registerObj
import writer

class ec2_eip:
    playbook_name = ''
    hosts=[]
    register=[]
    allow_reassociation = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    device_id = ''
    ec2_url = ''
    in_vpc = ''
    private_ip_address = ''
    profile = ''
    public_ip = ''
    region = ''
    release_on_disassociation = ''
    reuse_existing_ip_allowed = ''
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

