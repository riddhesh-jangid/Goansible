import random
import string
import os
from register import registerObj
import writer

class ce_stp:
    playbook_name = ''
    hosts=[]
    register=[]
    bpdu_filter = ''
    bpdu_protection = ''
    cost = ''
    edged_port = ''
    interface = ''
    loop_protection = ''
    root_protection = ''
    state = ''
    stp_converge = ''
    stp_enable = ''
    stp_mode = ''
    tc_protection = ''
    tc_protection_interval = ''
    tc_protection_threshold = ''
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

