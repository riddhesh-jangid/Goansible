import random
import string
import os
from register import registerObj
import writer

class ecs_taskdefinition:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    arn = ''
    aws_access_key = ''
    aws_secret_key = ''
    containers = ''
    cpu = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    execution_role_arn = ''
    family = ''
    force_create = ''
    launch_type = ''
    memory = ''
    network_mode = ''
    profile = ''
    region = ''
    revision = ''
    security_token = ''
    task_role_arn = ''
    validate_certs = ''
    volumes = ''
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

