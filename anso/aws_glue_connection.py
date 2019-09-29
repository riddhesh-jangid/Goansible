import random
import string
import os
from register import registerObj
import writer

class aws_glue_connection:
    playbook_name = ''
    hosts=[]
    register=[]
    connection_properties = ''
    name = ''
    state = ''
    aws_access_key = ''
    aws_secret_key = ''
    catalog_id = ''
    connection_type = ''
    debug_botocore_endpoint_logs = ''
    description = ''
    ec2_url = ''
    match_criteria = ''
    profile = ''
    region = ''
    security_groups = ''
    security_token = ''
    subnet_id = ''
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

