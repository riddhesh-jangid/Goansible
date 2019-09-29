import random
import string
import os
from register import registerObj
import writer

class na_elementsw_cluster_config:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    password = ''
    username = ''
    enable_virtual_volumes = ''
    encryption_at_rest = ''
    modify_cluster_full_threshold = ''
    set_ntp_info = ''
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

