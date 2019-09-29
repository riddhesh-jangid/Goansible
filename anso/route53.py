import random
import string
import os
from register import registerObj
import writer

class route53:
    playbook_name = ''
    hosts=[]
    register=[]
    record = ''
    state = ''
    type = ''
    zone = ''
    alias = ''
    alias_evaluate_target_health = ''
    alias_hosted_zone_id = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    failover = ''
    health_check = ''
    hosted_zone_id = ''
    identifier = ''
    overwrite = ''
    private_zone = ''
    profile = ''
    region = ''
    retry_interval = ''
    security_token = ''
    ttl = ''
    validate_certs = ''
    value = ''
    vpc_id = ''
    wait = ''
    wait_timeout = ''
    weight = ''
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

