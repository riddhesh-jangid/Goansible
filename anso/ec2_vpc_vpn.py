import random
import string
import os
from register import registerObj
import writer

class ec2_vpc_vpn:
    playbook_name = ''
    hosts=[]
    register=[]
    aws_access_key = ''
    aws_secret_key = ''
    connection_type = ''
    customer_gateway_id = ''
    debug_botocore_endpoint_logs = ''
    delay = ''
    ec2_url = ''
    filters = ''
    profile = ''
    purge_routes = ''
    purge_tags = ''
    region = ''
    routes = ''
    security_token = ''
    state = ''
    static_only = ''
    tags = ''
    tunnel_options = ''
    validate_certs = ''
    vpn_connection_id = ''
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

