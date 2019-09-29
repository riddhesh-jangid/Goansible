import random
import string
import os
from register import registerObj
import writer

class aws_batch_compute_environment:
    playbook_name = ''
    hosts=[]
    register=[]
    compute_environment_name = ''
    compute_resource_type = ''
    instance_role = ''
    instance_types = ''
    maxv_cpus = ''
    minv_cpus = ''
    security_group_ids = ''
    service_role = ''
    state = ''
    subnets = ''
    type = ''
    aws_access_key = ''
    aws_secret_key = ''
    bid_percentage = ''
    compute_environment_state = ''
    debug_botocore_endpoint_logs = ''
    desiredv_cpus = ''
    ec2_key_pair = ''
    ec2_url = ''
    image_id = ''
    profile = ''
    region = ''
    security_token = ''
    spot_iam_fleet_role = ''
    tags = ''
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

