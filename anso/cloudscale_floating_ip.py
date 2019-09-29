import random
import string
import os
from register import registerObj
import writer

class cloudscale_floating_ip:
    playbook_name = ''
    hosts=[]
    register=[]
    api_timeout = ''
    api_token = ''
    ip = ''
    ip_version = ''
    prefix_length = ''
    reverse_ptr = ''
    server = ''
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

