import random
import string
import os
from register import registerObj
import writer

class cloudtrail:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    state = ''
    aws_access_key = ''
    aws_secret_key = ''
    cloudwatch_logs_log_group_arn = ''
    cloudwatch_logs_role_arn = ''
    debug_botocore_endpoint_logs = ''
    ec2_url = ''
    enable_log_file_validation = ''
    enable_logging = ''
    include_global_events = ''
    is_multi_region_trail = ''
    kms_key_id = ''
    profile = ''
    region = ''
    s3_bucket_name = ''
    s3_key_prefix = ''
    security_token = ''
    sns_topic_name = ''
    tags = ''
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

