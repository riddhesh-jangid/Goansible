import random
import string
import os
from register import registerObj
import writer

class voss_config:
    playbook_name = ''
    hosts=[]
    register=[]
    after = ''
    backup = ''
    backup_options = ''
    before = ''
    defaults = ''
    diff_against = ''
    diff_ignore_lines = ''
    intended_config = ''
    lines = ''
    match = ''
    parents = ''
    replace = ''
    running_config = ''
    save_when = ''
    src = ''
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

