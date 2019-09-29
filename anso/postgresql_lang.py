import random
import string
import os
from register import registerObj
import writer

class postgresql_lang:
    playbook_name = ''
    hosts=[]
    register=[]
    lang = ''
    ca_cert = ''
    cascade = ''
    db = ''
    fail_on_drop = ''
    force_trust = ''
    login_host = ''
    login_password = ''
    login_unix_socket = ''
    login_user = ''
    port = ''
    session_role = ''
    ssl_mode = ''
    state = ''
    trust = ''
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

