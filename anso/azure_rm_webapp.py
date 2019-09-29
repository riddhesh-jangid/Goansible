import random
import string
import os
from register import registerObj
import writer

class azure_rm_webapp:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    resource_group = ''
    ad_user = ''
    adfs_authority_url = ''
    api_profile = ''
    app_settings = ''
    app_state = ''
    append_tags = ''
    auth_source = ''
    cert_validation_mode = ''
    client_affinity_enabled = ''
    client_id = ''
    cloud_environment = ''
    container_settings = ''
    deployment_source = ''
    dns_registration = ''
    frameworks = ''
    https_only = ''
    location = ''
    password = ''
    plan = ''
    profile = ''
    purge_app_settings = ''
    scm_type = ''
    secret = ''
    skip_custom_domain_verification = ''
    startup_file = ''
    state = ''
    subscription_id = ''
    tags = ''
    tenant = ''
    ttl_in_seconds = ''
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

