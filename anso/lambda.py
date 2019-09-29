import random
import string
import os
from register import registerObj
import writer

class lambda:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    aws_access_key = ''
    aws_secret_key = ''
    dead_letter_arn = ''
    debug_botocore_endpoint_logs = ''
    description = ''
    ec2_url = ''
    environment_variables = ''
    handler = ''
    memory_size = ''
    profile = ''
    region = ''
    role = ''
    runtime = ''
    s3_bucket = ''
    s3_key = ''
    s3_object_version = ''
    security_token = ''
    state = ''
    tags = ''
    timeout = ''
    validate_certs = ''
    vpc_security_group_ids = ''
    vpc_subnet_ids = ''
    zip_file = ''
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

