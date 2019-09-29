import random
import string
import os
from register import registerObj
import writer

class aws_direct_connect_virtual_interface:
    playbook_name = ''
    hosts=[]
    register=[]
    address_type = ''
    amazon_address = ''
    authentication_key = ''
    aws_access_key = ''
    aws_secret_key = ''
    bgp_asn = ''
    cidr = ''
    customer_address = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    id_to_associate = ''
    name = ''
    profile = ''
    public = ''
    region = ''
    security_token = ''
    state = ''
    validate_certs = ''
    virtual_gateway_id = ''
    virtual_interface_id = ''
    vlan = ''
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

