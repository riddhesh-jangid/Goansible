import random
import string
import os
from register import registerObj
import writer

class efs:
    playbook_name = ''
    hosts=[]
    register=[]
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    encrypt = ''
    id = ''
    kms_key_id = ''
    name = ''
    performance_mode = ''
    profile = ''
    provisioned_throughput_in_mibps = ''
    purge_tags = ''
    region = ''
    security_token = ''
    state = ''
    tags = ''
    targets = ''
    throughput_mode = ''
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

