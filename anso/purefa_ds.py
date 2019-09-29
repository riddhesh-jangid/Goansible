import random
import string
import os
from register import registerObj
import writer

class purefa_ds:
    playbook_name = ''
    hosts=[]
    register=[]
    api_token = ''
    base_dn = ''
    fa_url = ''
    aa_group = ''
    bind_password = ''
    bind_user = ''
    enable = ''
    group_base = ''
    ro_group = ''
    sa_group = ''
    state = ''
    uri = ''
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

