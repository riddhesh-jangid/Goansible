import random
import string
import os
from register import registerObj
import writer

class ec2_snapshot_copy:
    playbook_name = ''
    hosts=[]
    register=[]
    source_region = ''
    source_snapshot_id = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    description = ''
    ec2_url = ''
    encrypted = ''
    kms_key_id = ''
    profile = ''
    region = ''
    security_token = ''
    tags = ''
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

