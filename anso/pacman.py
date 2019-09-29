import random
import string
import os
from register import registerObj
import writer

class pacman:
    playbook_name = ''
    hosts=[]
    register=[]
    extra_args = ''
    force = ''
    name = ''
    recurse = ''
    state = ''
    update_cache = ''
    update_cache_extra_args = ''
    upgrade = ''
    upgrade_extra_args = ''
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

