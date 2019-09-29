import random
import string
import os
from register import registerObj
import writer

class netapp_e_snapshot_group:
    playbook_name = ''
    hosts=[]
    register=[]
    api_password = ''
    api_url = ''
    api_username = ''
    base_volume_name = ''
    name = ''
    state = ''
    storage_pool_name = ''
    delete_limit = ''
    full_policy = ''
    repo_pct = ''
    rollback_priority = ''
    validate_certs = ''
    warning_threshold = ''
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

