import random
import string
import os
from register import registerObj
import writer

class azure_rm_devtestlabartifactsource:
    playbook_name = ''
    hosts=[]
    register=[]
    lab_name = ''
    name = ''
    resource_group = ''
    ad_user = ''
    adfs_authority_url = ''
    api_profile = ''
    append_tags = ''
    arm_template_folder_path = ''
    auth_source = ''
    branch_ref = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    display_name = ''
    folder_path = ''
    is_enabled = ''
    password = ''
    profile = ''
    secret = ''
    security_token = ''
    source_type = ''
    state = ''
    subscription_id = ''
    tags = ''
    tenant = ''
    uri = ''
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

