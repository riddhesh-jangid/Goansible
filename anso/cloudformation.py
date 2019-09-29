import random
import string
import os
from register import registerObj
import writer

class cloudformation:
    playbook_name = ''
    hosts=[]
    register=[]
    stack_name = ''
    aws_access_key = ''
    aws_secret_key = ''
    backoff_delay = ''
    backoff_max_delay = ''
    backoff_retries = ''
    capabilities = ''
    changeset_name = ''
    create_changeset = ''
    create_timeout = ''
    debug_botocore_endpoint_logs = ''
    disable_rollback = ''
    ec2_url = ''
    events_limit = ''
    notification_arns = ''
    profile = ''
    region = ''
    role_arn = ''
    security_token = ''
    stack_policy = ''
    state = ''
    tags = ''
    template = ''
    template_body = ''
    template_format = ''
    template_parameters = ''
    template_url = ''
    termination_protection = ''
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

