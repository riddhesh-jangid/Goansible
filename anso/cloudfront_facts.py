import random
import string
import os
from register import registerObj
import writer

class cloudfront_facts:
    playbook_name = ''
    hosts=[]
    register=[]
    all_lists = ''
    aws_access_key = ''
    aws_secret_key = ''
    debug_botocore_endpoint_logs = ''
    distribution = ''
    distribution_config = ''
    distribution_id = ''
    domain_name_alias = ''
    ec2_url = ''
    invalidation = ''
    invalidation_id = ''
    list_distributions = ''
    list_distributions_by_web_acl_id = ''
    list_invalidations = ''
    list_origin_access_identities = ''
    list_streaming_distributions = ''
    origin_access_identity = ''
    origin_access_identity_config = ''
    origin_access_identity_id = ''
    profile = ''
    region = ''
    security_token = ''
    streaming_distribution = ''
    streaming_distribution_config = ''
    summary = ''
    validate_certs = ''
    web_acl_id = ''
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

