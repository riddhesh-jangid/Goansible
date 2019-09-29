import random
import string
import os
from register import registerObj
import writer

class svr4pkg:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    state = ''
    category = ''
    proxy = ''
    response_file = ''
    src = ''
    zone = ''
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

