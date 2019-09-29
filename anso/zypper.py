import random
import string
import os
from register import registerObj
import writer

class zypper:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    disable_gpg_check = ''
    disable_recommends = ''
    extra_args = ''
    extra_args_precommand = ''
    force = ''
    oldpackage = ''
    state = ''
    type = ''
    update_cache = ''
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

