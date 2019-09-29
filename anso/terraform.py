import random
import string
import os
from register import registerObj
import writer

class terraform:
    playbook_name = ''
    hosts=[]
    register=[]
    project_path = ''
    backend_config = ''
    binary_path = ''
    force_init = ''
    lock = ''
    lock_timeout = ''
    plan_file = ''
    purge_workspace = ''
    state = ''
    state_file = ''
    targets = ''
    variables = ''
    variables_file = ''
    workspace = ''
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

