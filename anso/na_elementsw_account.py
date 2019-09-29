import random
import string
import os
from register import registerObj
import writer

class na_elementsw_account:
    playbook_name = ''
    hosts=[]
    register=[]
    element_username = ''
    hostname = ''
    password = ''
    state = ''
    username = ''
    attributes = ''
    from_name = ''
    initiator_secret = ''
    status = ''
    target_secret = ''
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

