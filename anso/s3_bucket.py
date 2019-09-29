import random
import string
import os
from register import registerObj
import writer

class s3_bucket:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    aws_access_key = ''
    aws_secret_key = ''
    ceph = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    force = ''
    policy = ''
    profile = ''
    region = ''
    requester_pays = ''
    s3_url = ''
    security_token = ''
    state = ''
    tags = ''
    validate_certs = ''
    versioning = ''
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

