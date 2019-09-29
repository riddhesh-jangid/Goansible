import random
import string
import os
from register import registerObj
import writer

class route53_facts:
    playbook_name = ''
    hosts=[]
    register=[]
    query = ''
    aws_access_key = ''
    aws_secret_key = ''
    change_id = ''
    debug_botocore_endpoint_logs = ''
    delegation_set_id = ''
    dns_name = ''
    ec2_url = ''
    health_check_id = ''
    health_check_method = ''
    hosted_zone_id = ''
    hosted_zone_method = ''
    max_items = ''
    next_marker = ''
    profile = ''
    region = ''
    resource_id = ''
    security_token = ''
    start_record_name = ''
    type = ''
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

