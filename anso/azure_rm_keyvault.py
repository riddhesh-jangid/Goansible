import random
import string
import os
from register import registerObj
import writer

class azure_rm_keyvault:
    playbook_name = ''
    hosts=[]
    register=[]
    resource_group = ''
    vault_name = ''
    access_policies = ''
    ad_user = ''
    adfs_authority_url = ''
    api_profile = ''
    append_tags = ''
    auth_source = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    enable_soft_delete = ''
    enabled_for_deployment = ''
    enabled_for_disk_encryption = ''
    enabled_for_template_deployment = ''
    location = ''
    password = ''
    profile = ''
    recover_mode = ''
    secret = ''
    sku = ''
    state = ''
    subscription_id = ''
    tags = ''
    tenant = ''
    vault_tenant = ''
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

