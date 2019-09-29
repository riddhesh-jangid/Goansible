import random
import string
import os
from register import registerObj
import writer

class win_wait_for_process:
    playbook_name = ''
    hosts=[]
    register=[]
    owner = ''
    pid = ''
    post_wait_delay = ''
    pre_wait_delay = ''
    process_min_count = ''
    process_name_exact = ''
    process_name_pattern = ''
    sleep = ''
    state = ''
    timeout = ''
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

