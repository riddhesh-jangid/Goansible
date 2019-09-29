import random
import string
import os
from register import registerObj
import writer

class win_chocolatey_source:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    admin_only = ''
    allow_self_service = ''
    bypass_proxy = ''
    certificate = ''
    certificate_password = ''
    priority = ''
    source = ''
    source_password = ''
    source_username = ''
    state = ''
    update_password = ''
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

