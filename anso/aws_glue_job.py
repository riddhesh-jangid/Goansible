import random
import string
import os
from register import registerObj
import writer

class aws_glue_job:
    playbook_name = ''
    hosts=[]
    register=[]
    command_script_location = ''
    name = ''
    role = ''
    state = ''
    allocated_capacity = ''
    aws_access_key = ''
    aws_secret_key = ''
    command_name = ''
    connections = ''
    debug_botocore_endpoint_logs = ''
    default_arguments = ''
    description = ''
    ec2_url = ''
    max_concurrent_runs = ''
    max_retries = ''
    profile = ''
    region = ''
    security_token = ''
    timeout = ''
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

