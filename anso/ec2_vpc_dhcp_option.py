import random
import string
import os
from register import registerObj
import writer

class ec2_vpc_dhcp_option:
    playbook_name = ''
    hosts=[]
    register=[]
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    delete_old = ''
    dhcp_options_id = ''
    dns_servers = ''
    domain_name = ''
    ec2_url = ''
    inherit_existing = ''
    netbios_name_servers = ''
    netbios_node_type = ''
    ntp_servers = ''
    profile = ''
    region = ''
    security_token = ''
    state = ''
    tags = ''
    validate_certs = ''
    vpc_id = ''
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

