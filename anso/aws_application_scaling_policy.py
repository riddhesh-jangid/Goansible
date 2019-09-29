import random
import string
import os
from register import registerObj
import writer

class aws_application_scaling_policy:
    playbook_name = ''
    hosts=[]
    register=[]
    policy_name = ''
    policy_type = ''
    resource_id = ''
    scalable_dimension = ''
    service_namespace = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    maximum_tasks = ''
    minimum_tasks = ''
    override_task_capacity = ''
    profile = ''
    region = ''
    security_token = ''
    step_scaling_policy_configuration = ''
    target_tracking_scaling_policy_configuration = ''
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

