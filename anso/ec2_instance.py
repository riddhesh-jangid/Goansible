import random
import string
import os
from register import registerObj
import writer

class ec2_instance:
    playbook_name = ''
    hosts=[]
    register=[]
    availability_zone = ''
    aws_access_key = ''
    aws_secret_key = ''
    cpu_credit_specification = ''
    cpu_options = ''
    debug_botocore_endpoint_logs = ''
    detailed_monitoring = ''
    ebs_optimized = ''
    ec2_url = ''
    filters = ''
    image = ''
    image_id = ''
    instance_ids = ''
    instance_initiated_shutdown_behavior = ''
    instance_role = ''
    instance_type = ''
    key_name = ''
    launch_template = ''
    name = ''
    network = ''
    placement_group = ''
    profile = ''
    purge_tags = ''
    region = ''
    security_group = ''
    security_groups = ''
    security_token = ''
    state = ''
    tags = ''
    tenancy = ''
    termination_protection = ''
    tower_callback = ''
    user_data = ''
    validate_certs = ''
    volumes = ''
    vpc_subnet_id = ''
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

