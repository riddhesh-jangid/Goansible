import random
import string
import os
from register import registerObj
import writer

class win_domain_controller:
    playbook_name = ''
    hosts=[]
    register=[]
    domain_admin_password = ''
    domain_admin_user = ''
    database_path = ''
    dns_domain_name = ''
    local_admin_password = ''
    read_only = ''
    safe_mode_password = ''
    site_name = ''
    state = ''
    sysvol_path = ''
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

