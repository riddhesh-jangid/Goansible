import random
import string
import os
from register import registerObj
import writer

class aws_direct_connect_link_aggregation_group:
    playbook_name = ''
    hosts=[]
    register=[]
    aws_access_key = ''
    aws_secret_key = ''
    bandwidth = ''
    connection_id = ''
    debug_botocore_endpoint_logs = ''
    delete_with_disassociation = ''
    ec2_url = ''
    force_delete = ''
    link_aggregation_group_id = ''
    location = ''
    min_links = ''
    name = ''
    num_connections = ''
    profile = ''
    region = ''
    security_token = ''
    state = ''
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

