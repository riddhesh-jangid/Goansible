import random
import string
import os
from register import registerObj
import writer

class avi_backupconfiguration:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    backup_file_prefix = ''
    backup_passphrase = ''
    controller = ''
    maximum_backups_stored = ''
    password = ''
    remote_directory = ''
    remote_hostname = ''
    save_local = ''
    ssh_user_ref = ''
    state = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    upload_to_remote_host = ''
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

