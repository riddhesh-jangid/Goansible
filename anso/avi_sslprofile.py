import random
import string
import os
from register import registerObj
import writer

class avi_sslprofile:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    accepted_ciphers = ''
    accepted_versions = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    cipher_enums = ''
    controller = ''
    description = ''
    dhparam = ''
    enable_ssl_session_reuse = ''
    password = ''
    prefer_client_cipher_ordering = ''
    send_close_notify = ''
    ssl_rating = ''
    ssl_session_timeout = ''
    state = ''
    tags = ''
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

