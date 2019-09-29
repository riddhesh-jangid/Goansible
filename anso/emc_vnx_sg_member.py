import random
import string
import os
from register import registerObj
import writer

class emc_vnx_sg_member:
    playbook_name = ''
    hosts=[]
    register=[]
    lunid = ''
    name = ''
    sp_address = ''
    sp_password = ''
    sp_user = ''
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

