import random
import string
import os
from register import registerObj
import writer

class ce_bfd_session:
    playbook_name = ''
    hosts=[]
    register=[]
    session_name = ''
    addr_type = ''
    create_type = ''
    dest_addr = ''
    out_if_name = ''
    src_addr = ''
    state = ''
    use_default_ip = ''
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

