import random
import string
import os
from register import registerObj
import writer

class ecs_service:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    state = ''
    aws_access_key = ''
    aws_secret_key = ''
    client_token = ''
    cluster = ''
    debug_botocore_endpoint_logs = ''
    delay = ''
    deployment_configuration = ''
    desired_count = ''
    ec2_url = ''
    force_new_deployment = ''
    health_check_grace_period_seconds = ''
    launch_type = ''
    load_balancers = ''
    network_configuration = ''
    placement_constraints = ''
    placement_strategy = ''
    profile = ''
    region = ''
    repeat = ''
    role = ''
    scheduling_strategy = ''
    security_token = ''
    service_registries = ''
    task_definition = ''
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

