import random
import string
import os
from register import registerObj
import writer

class aws_batch_job_definition:
    playbook_name = ''
    hosts=[]
    register=[]
    job_definition_name = ''
    state = ''
    type = ''
    attempts = ''
    aws_access_key = ''
    aws_secret_key = ''
    command = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    environment = ''
    image = ''
    job_definition_arn = ''
    job_role_arn = ''
    memory = ''
    mount_points = ''
    parameters = ''
    privileged = ''
    profile = ''
    readonly_root_filesystem = ''
    region = ''
    security_token = ''
    ulimits = ''
    user = ''
    validate_certs = ''
    vcpus = ''
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

