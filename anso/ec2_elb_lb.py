import random
import string
import os
from register import registerObj
import writer

class ec2_elb_lb:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    state = ''
    access_logs = ''
    aws_access_key = ''
    aws_secret_key = ''
    connection_draining_timeout = ''
    cross_az_load_balancing = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    health_check = ''
    idle_timeout = ''
    instance_ids = ''
    listeners = ''
    profile = ''
    purge_instance_ids = ''
    purge_listeners = ''
    purge_subnets = ''
    purge_zones = ''
    region = ''
    scheme = ''
    security_group_ids = ''
    security_group_names = ''
    security_token = ''
    stickiness = ''
    subnets = ''
    tags = ''
    validate_certs = ''
    wait = ''
    wait_timeout = ''
    zones = ''
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

