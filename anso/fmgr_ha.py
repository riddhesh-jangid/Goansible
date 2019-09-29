import random
import string
import os
from register import registerObj
import writer

class fmgr_ha:
    playbook_name = ''
    hosts=[]
    register=[]
    fmgr_ha_cluster_id = ''
    fmgr_ha_cluster_pw = ''
    fmgr_ha_file_quota = ''
    fmgr_ha_hb_interval = ''
    fmgr_ha_hb_threshold = ''
    fmgr_ha_mode = ''
    fmgr_ha_peer_ipv4 = ''
    fmgr_ha_peer_ipv6 = ''
    fmgr_ha_peer_sn = ''
    fmgr_ha_peer_status = ''
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

