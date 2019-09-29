import random
import string
import os
from register import registerObj
import writer

class ldap_passwd:
    playbook_name = ''
    hosts=[]
    register=[]
    dn = ''
    passwd = ''
    bind_dn = ''
    bind_pw = ''
    server_uri = ''
    start_tls = ''
    validate_certs = ''
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

