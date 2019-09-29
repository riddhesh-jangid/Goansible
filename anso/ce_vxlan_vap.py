import random
import string
import os
from register import registerObj
import writer

class ce_vxlan_vap:
    playbook_name = ''
    hosts=[]
    register=[]
    bind_vlan_id = ''
    bridge_domain_id = ''
    ce_vid = ''
    encapsulation = ''
    l2_sub_interface = ''
    pe_vid = ''
    state = ''
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

