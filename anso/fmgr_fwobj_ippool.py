import random
import string
import os
from register import registerObj
import writer

class fmgr_fwobj_ippool:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    arp_intf = ''
    arp_reply = ''
    associated_interface = ''
    block_size = ''
    comments = ''
    dynamic_mapping = ''
    dynamic_mapping_arp_intf = ''
    dynamic_mapping_arp_reply = ''
    dynamic_mapping_associated_interface = ''
    dynamic_mapping_block_size = ''
    dynamic_mapping_comments = ''
    dynamic_mapping_endip = ''
    dynamic_mapping_num_blocks_per_user = ''
    dynamic_mapping_pba_timeout = ''
    dynamic_mapping_permit_any_host = ''
    dynamic_mapping_source_endip = ''
    dynamic_mapping_source_startip = ''
    dynamic_mapping_startip = ''
    dynamic_mapping_type = ''
    endip = ''
    mode = ''
    name = ''
    num_blocks_per_user = ''
    pba_timeout = ''
    permit_any_host = ''
    source_endip = ''
    source_startip = ''
    startip = ''
    type = ''
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

