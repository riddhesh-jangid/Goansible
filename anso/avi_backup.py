import random
import string
import os
from register import registerObj
import writer

class avi_backup:
    playbook_name = ''
    hosts=[]
    register=[]
    file_name = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    backup_config_ref = ''
    controller = ''
    local_file_url = ''
    password = ''
    remote_file_url = ''
    scheduler_ref = ''
    state = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    timestamp = ''
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

