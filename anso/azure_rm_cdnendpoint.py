import random
import string
import os
from register import registerObj
import writer

class azure_rm_cdnendpoint:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    origins = ''
    profile_name = ''
    resource_group = ''
    ad_user = ''
    adfs_authority_url = ''
    api_profile = ''
    append_tags = ''
    auth_source = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    content_types_to_compress = ''
    is_compression_enabled = ''
    is_http_allowed = ''
    is_https_allowed = ''
    location = ''
    origin_host_header = ''
    origin_path = ''
    password = ''
    profile = ''
    purge = ''
    purge_content_paths = ''
    query_string_caching_behavior = ''
    secret = ''
    started = ''
    state = ''
    subscription_id = ''
    tags = ''
    tenant = ''
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

