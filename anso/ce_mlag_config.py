import random
import string
import os
from register import registerObj
import writer

class ce_mlag_config:
    playbook_name = ''
    hosts=[]
    register=[]
    dfs_group_id = ''
    eth_trunk_id = ''
    ip_address = ''
    nickname = ''
    peer_link_id = ''
    priority_id = ''
    pseudo_nickname = ''
    pseudo_priority = ''
    state = ''
    vpn_instance_name = ''
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

