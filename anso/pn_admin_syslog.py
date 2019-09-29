import random
import string
import os
from register import registerObj
import writer

class pn_admin_syslog:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    pn_cliswitch = ''
    pn_host = ''
    pn_message_format = ''
    pn_name = ''
    pn_port = ''
    pn_scope = ''
    pn_transport = ''
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

