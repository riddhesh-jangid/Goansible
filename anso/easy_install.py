import random
import string
import os
from register import registerObj
import writer

class easy_install:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    executable = ''
    state = ''
    virtualenv = ''
    virtualenv_command = ''
    virtualenv_site_packages = ''
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

