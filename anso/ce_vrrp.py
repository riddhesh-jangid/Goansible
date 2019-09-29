import random
import string
import os
from register import registerObj
import writer

class ce_vrrp:
    playbook_name = ''
    hosts=[]
    register=[]
    admin_flowdown = ''
    admin_ignore_if_down = ''
    admin_interface = ''
    admin_vrid = ''
    advertise_interval = ''
    auth_key = ''
    auth_mode = ''
    fast_resume = ''
    gratuitous_arp_interval = ''
    holding_multiplier = ''
    interface = ''
    is_plain = ''
    preempt_timer_delay = ''
    priority = ''
    recover_delay = ''
    state = ''
    version = ''
    virtual_ip = ''
    vrid = ''
    vrrp_type = ''
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

