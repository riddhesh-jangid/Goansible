import random
import string
import os
from register import registerObj
import writer

class s3_sync:
    playbook_name = ''
    hosts=[]
    register=[]
    bucket = ''
    file_root = ''
    mode = ''
    aws_access_key = ''
    aws_secret_key = ''
    cache_control = ''
    debug_botocore_endpoint_logs = ''
    delete = ''
    ec2_url = ''
    exclude = ''
    file_change_strategy = ''
    include = ''
    key_prefix = ''
    mime_map = ''
    permission = ''
    profile = ''
    region = ''
    security_token = ''
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

