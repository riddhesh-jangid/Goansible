import random
import string
import os
from register import registerObj
import writer

class ec2_ami_find:
    playbook_name = ''
    hosts=[]
    register=[]
    region = ''
    ami_id = ''
    ami_tags = ''
    architecture = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    hypervisor = ''
    is_public = ''
    name = ''
    no_result_action = ''
    owner = ''
    platform = ''
    product_code = ''
    profile = ''
    root_device_type = ''
    security_token = ''
    sort = ''
    sort_end = ''
    sort_order = ''
    sort_start = ''
    sort_tag = ''
    state = ''
    validate_certs = ''
    virtualization_type = ''
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

