import random
import string
import os
from register import registerObj
import writer

class bundler:
    playbook_name = ''
    hosts=[]
    register=[]
    binstub_directory = ''
    chdir = ''
    clean = ''
    deployment_mode = ''
    exclude_groups = ''
    executable = ''
    extra_args = ''
    gem_path = ''
    gemfile = ''
    local = ''
    state = ''
    user_install = ''
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

