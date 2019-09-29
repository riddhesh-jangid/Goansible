import random
import string
import os
from register import registerObj
import writer

class pn_port_cos_rate_setting:
    playbook_name = ''
    hosts=[]
    register=[]
    state = ''
    pn_cliswitch = ''
    pn_cos0_rate = ''
    pn_cos1_rate = ''
    pn_cos2_rate = ''
    pn_cos3_rate = ''
    pn_cos4_rate = ''
    pn_cos5_rate = ''
    pn_cos6_rate = ''
    pn_cos7_rate = ''
    pn_port = ''
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

