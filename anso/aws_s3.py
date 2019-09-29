import random
import string
import os
from register import registerObj
import writer

class aws_s3:
    playbook_name = ''
    hosts=[]
    register=[]
    bucket = ''
    mode = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    dest = ''
    dualstack = ''
    ec2_url = ''
    encrypt = ''
    encryption_kms_key_id = ''
    encryption_mode = ''
    expiration = ''
    headers = ''
    ignore_nonexistent_bucket = ''
    marker = ''
    max_keys = ''
    metadata = ''
    object = ''
    overwrite = ''
    permission = ''
    prefix = ''
    profile = ''
    region = ''
    retries = ''
    rgw = ''
    s3_url = ''
    security_token = ''
    src = ''
    validate_certs = ''
    version = ''
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

