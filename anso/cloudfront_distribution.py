import random
import string
import os
from register import registerObj
import writer

class cloudfront_distribution:
    playbook_name = ''
    hosts=[]
    register=[]
    alias = ''
    aliases = ''
    aws_access_key = ''
    aws_secret_key = ''
    cache_behaviors = ''
    caller_reference = ''
    comment = ''
    custom_error_responses = ''
    debug_botocore_endpoint_logs = ''
    default_cache_behavior = ''
    default_origin_domain_name = ''
    default_origin_path = ''
    default_root_object = ''
    distribution_id = ''
    e_tag = ''
    ec2_url = ''
    enabled = ''
    http_version = ''
    ipv6_enabled = ''
    logging = ''
    origins = ''
    price_class = ''
    profile = ''
    purge_aliases = ''
    purge_cache_behaviors = ''
    purge_custom_error_responses = ''
    purge_origins = ''
    purge_tags = ''
    region = ''
    restrictions = ''
    security_token = ''
    state = ''
    tags = ''
    validate_certs = ''
    viewer_certificate = ''
    wait = ''
    wait_timeout = ''
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

