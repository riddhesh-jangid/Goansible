import random
import string
import os
from register import registerObj
import writer

class azure_rm_storageblob:
    playbook_name = ''
    hosts=[]
    register=[]
    container = ''
    resource_group = ''
    storage_account_name = ''
    ad_user = ''
    adfs_authority_url = ''
    api_profile = ''
    append_tags = ''
    auth_source = ''
    blob = ''
    blob_type = ''
    cache_control = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    content_disposition = ''
    content_encoding = ''
    content_language = ''
    content_md5 = ''
    content_type = ''
    dest = ''
    force = ''
    password = ''
    profile = ''
    public_access = ''
    secret = ''
    src = ''
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

