import random
import string
import os
from register import registerObj
import writer

class pn_vrouterif:
    playbook_name = ''
    hosts=[]
    register=[]
    pn_vrouter_name = ''
    state = ''
    pn_alias = ''
    pn_assignment = ''
    pn_clipassword = ''
    pn_cliswitch = ''
    pn_cliusername = ''
    pn_exclusive = ''
    pn_interface = ''
    pn_interface_ip = ''
    pn_l3port = ''
    pn_nic_enable = ''
    pn_nic_str = ''
    pn_secondary_macs = ''
    pn_vlan = ''
    pn_vrrp_adv_int = ''
    pn_vrrp_id = ''
    pn_vrrp_priority = ''
    pn_vxlan = ''
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

