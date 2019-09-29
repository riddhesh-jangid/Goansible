import random
import string
import os
from register import registerObj
import writer

class ec2:
    playbook_name = ''
    hosts=[]
    register=[]
    image = ''
    instance_type = ''
    assign_public_ip = ''
    aws_access_key = ''
    aws_secret_key = ''
    count = ''
    count_tag = ''
    debug_botocore_endpoint_logs = ''
    ebs_optimized = ''
    ec2_url = ''
    exact_count = ''
    group = ''
    group_id = ''
    id = ''
    instance_ids = ''
    instance_initiated_shutdown_behavior = ''
    instance_profile_name = ''
    instance_tags = ''
    kernel = ''
    key_name = ''
    monitoring = ''
    network_interfaces = ''
    placement_group = ''
    private_ip = ''
    profile = ''
    ramdisk = ''
    region = ''
    security_token = ''
    source_dest_check = ''
    spot_launch_group = ''
    spot_price = ''
    spot_type = ''
    spot_wait_timeout = ''
    state = ''
    tenancy = ''
    termination_protection = ''
    user_data = ''
    validate_certs = ''
    volumes = ''
    vpc_subnet_id = ''
    wait = ''
    wait_timeout = ''
    zone = ''
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

