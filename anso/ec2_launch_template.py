import random
import string
import os
from register import registerObj
import writer

class ec2_launch_template:
    playbook_name = ''
    hosts=[]
    register=[]
    aws_access_key = ''
    aws_secret_key = ''
    block_device_mappings = ''
    cpu_options = ''
    credit_specification = ''
    debug_botocore_endpoint_logs = ''
    default_version = ''
    disable_api_termination = ''
    ebs_optimized = ''
    ec2_url = ''
    elastic_gpu_specifications = ''
    iam_instance_profile = ''
    image_id = ''
    instance_initiated_shutdown_behavior = ''
    instance_market_options = ''
    instance_type = ''
    kernel_id = ''
    key_name = ''
    monitoring = ''
    network_interfaces = ''
    placement = ''
    profile = ''
    ram_disk_id = ''
    region = ''
    security_group_ids = ''
    security_groups = ''
    security_token = ''
    state = ''
    tags = ''
    template_id = ''
    template_name = ''
    user_data = ''
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

