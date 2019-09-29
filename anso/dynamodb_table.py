import random
import string
import os
from register import registerObj
import writer

class dynamodb_table:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    hash_key_name = ''
    hash_key_type = ''
    indexes = ''
    profile = ''
    range_key_name = ''
    range_key_type = ''
    read_capacity = ''
    region = ''
    security_token = ''
    state = ''
    tags = ''
    validate_certs = ''
    wait_for_active_timeout = ''
    write_capacity = ''
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

