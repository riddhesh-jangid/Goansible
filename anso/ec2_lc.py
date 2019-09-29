import random
import string
import os
from register import registerObj
import writer

class ec2_lc:
    playbook_name = ''
    hosts=[]
    register=[]
    instance_type = ''
    name = ''
    assign_public_ip = ''
    aws_access_key = ''
    aws_secret_key = ''
    classic_link_vpc_id = ''
    classic_link_vpc_security_groups = ''
    debug_botocore_endpoint_logs = ''
    ebs_optimized = ''
    ec2_url = ''
    image_id = ''
    instance_id = ''
    instance_monitoring = ''
    instance_profile_name = ''
    kernel_id = ''
    key_name = ''
    placement_tenancy = ''
    profile = ''
    ramdisk_id = ''
    region = ''
    security_groups = ''
    security_token = ''
    spot_price = ''
    state = ''
    user_data = ''
    user_data_path = ''
    validate_certs = ''
    volumes = ''
    vpc_id = ''
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

