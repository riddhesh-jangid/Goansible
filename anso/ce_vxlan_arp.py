import random
import string
import os
from register import registerObj
import writer

class ce_vxlan_arp:
    playbook_name = ''
    hosts=[]
    register=[]
    arp_collect_host = ''
    arp_suppress = ''
    bridge_domain_id = ''
    evn_bgp = ''
    evn_peer_ip = ''
    evn_reflect_client = ''
    evn_server = ''
    evn_source_ip = ''
    host_collect_protocol = ''
    state = ''
    vbdif_name = ''
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

