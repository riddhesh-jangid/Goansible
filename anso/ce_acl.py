import random
import string
import os
from register import registerObj
import writer

class ce_acl:
    playbook_name = ''
    hosts=[]
    register=[]
    acl_name = ''
    acl_description = ''
    acl_num = ''
    acl_step = ''
    frag_type = ''
    log_flag = ''
    rule_action = ''
    rule_description = ''
    rule_id = ''
    rule_name = ''
    source_ip = ''
    src_mask = ''
    state = ''
    time_range = ''
    vrf_name = ''
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

