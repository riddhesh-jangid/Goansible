import random
import string
import os
from register import registerObj
import writer

class ec2_metric_alarm:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    state = ''
    alarm_actions = ''
    aws_access_key = ''
    aws_secret_key = ''
    comparison = ''
    debug_botocore_endpoint_logs = ''
    description = ''
    dimensions = ''
    ec2_url = ''
    evaluation_periods = ''
    insufficient_data_actions = ''
    metric = ''
    namespace = ''
    ok_actions = ''
    period = ''
    profile = ''
    region = ''
    security_token = ''
    statistic = ''
    threshold = ''
    unit = ''
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

