import random
import string
import os
from register import registerObj
import writer

class ec2_vpc_net:
    playbook_name = ''
    hosts=[]
    register=[]
    cidr_block = ''
    name = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    dhcp_opts_id = ''
    dns_hostnames = ''
    dns_support = ''
    ec2_url = ''
    multi_ok = ''
    profile = ''
    purge_cidrs = ''
    region = ''
    security_token = ''
    state = ''
    tags = ''
    tenancy = ''
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

