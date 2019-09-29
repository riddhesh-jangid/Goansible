import random
import string
import os
from register import registerObj
import writer

class avi_applicationpersistenceprofile:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    persistence_type = ''
    api_context = ''
    api_version = ''
    app_cookie_persistence_profile = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    controller = ''
    description = ''
    hdr_persistence_profile = ''
    http_cookie_persistence_profile = ''
    ip_persistence_profile = ''
    is_federated = ''
    password = ''
    server_hm_down_recovery = ''
    state = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
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

