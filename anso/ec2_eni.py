import random
import string
import os
from register import registerObj
import writer

class ec2_eni:
    playbook_name = ''
    hosts=[]
    register=[]
    allow_reassignment = ''
    attached = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    delete_on_termination = ''
    description = ''
    device_index = ''
    ec2_url = ''
    eni_id = ''
    force_detach = ''
    instance_id = ''
    private_ip_address = ''
    profile = ''
    purge_secondary_private_ip_addresses = ''
    region = ''
    secondary_private_ip_address_count = ''
    secondary_private_ip_addresses = ''
    security_groups = ''
    security_token = ''
    source_dest_check = ''
    state = ''
    subnet_id = ''
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

