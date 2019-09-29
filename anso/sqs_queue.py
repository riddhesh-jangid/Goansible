import random
import string
import os
from register import registerObj
import writer

class sqs_queue:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    default_visibility_timeout = ''
    delivery_delay = ''
    ec2_url = ''
    maximum_message_size = ''
    message_retention_period = ''
    policy = ''
    profile = ''
    receive_message_wait_time = ''
    redrive_policy = ''
    region = ''
    security_token = ''
    state = ''
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

