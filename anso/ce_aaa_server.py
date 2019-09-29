import random
import string
import os
from register import registerObj
import writer

class ce_aaa_server:
    playbook_name = ''
    hosts=[]
    register=[]
    accounting_mode = ''
    acct_scheme_name = ''
    authen_scheme_name = ''
    author_scheme_name = ''
    domain_name = ''
    first_authen_mode = ''
    first_author_mode = ''
    hwtacas_template = ''
    local_user_group = ''
    radius_server_group = ''
    state = ''
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

