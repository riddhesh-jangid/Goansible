import random
import string
import os
from register import registerObj
import writer

class avi_useraccountprofile:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    account_lock_timeout = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    controller = ''
    credentials_timeout_threshold = ''
    max_concurrent_sessions = ''
    max_login_failure_count = ''
    max_password_history_count = ''
    password = ''
    state = ''
    tenant = ''
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

