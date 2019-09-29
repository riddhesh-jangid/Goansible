import random
import string
import os
from register import registerObj
import writer

class junos_l3_interface:
    playbook_name = ''
    hosts=[]
    register=[]
    active = ''
    aggregate = ''
    filter6_input = ''
    filter6_output = ''
    filter_input = ''
    filter_output = ''
    ipv4 = ''
    ipv6 = ''
    name = ''
    provider = ''
    state = ''
    unit = ''
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

