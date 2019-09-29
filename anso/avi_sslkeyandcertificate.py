import random
import string
import os
from register import registerObj
import writer

class avi_sslkeyandcertificate:
    playbook_name = ''
    hosts=[]
    register=[]
    certificate = ''
    name = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    ca_certs = ''
    certificate_management_profile_ref = ''
    controller = ''
    created_by = ''
    dynamic_params = ''
    enckey_base64 = ''
    enckey_name = ''
    hardwaresecuritymodulegroup_ref = ''
    key = ''
    key_params = ''
    password = ''
    state = ''
    status = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    type = ''
    url = ''
    username = ''
    uuid = ''
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

