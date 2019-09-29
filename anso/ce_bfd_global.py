import random
import string
import os
from register import registerObj
import writer

class ce_bfd_global:
    playbook_name = ''
    hosts=[]
    register=[]
    bfd_enable = ''
    damp_init_wait_time = ''
    damp_max_wait_time = ''
    damp_second_wait_time = ''
    default_ip = ''
    delay_up_time = ''
    state = ''
    tos_exp_dynamic = ''
    tos_exp_static = ''
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

