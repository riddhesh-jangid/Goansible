import random
import string
import os
from register import registerObj
import writer

class pamd:
    playbook_name = ''
    hosts=[]
    register=[]
    control = ''
    module_path = ''
    name = ''
    type = ''
    backup = ''
    module_arguments = ''
    new_control = ''
    new_module_path = ''
    new_type = ''
    path = ''
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

