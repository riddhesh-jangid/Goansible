import random
import string
import os
from register import registerObj
import writer

class postgresql_privs:
    playbook_name = ''
    hosts=[]
    register=[]
    database = ''
    roles = ''
    ca_cert = ''
    fail_on_role = ''
    grant_option = ''
    host = ''
    login = ''
    login_host = ''
    login_password = ''
    login_unix_socket = ''
    login_user = ''
    objs = ''
    password = ''
    port = ''
    privs = ''
    schema = ''
    session_role = ''
    ssl_mode = ''
    state = ''
    target_roles = ''
    type = ''
    unix_socket = ''
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

