import random
import string
import os
from register import registerObj
import writer

class oneandone_public_ip:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_token = ''
    public_ip_id = ''
    api_url = ''
    datacenter = ''
    reverse_dns = ''
    state = ''
    type = ''
    wait = ''
    wait_interval = ''
    wait_timeout = ''
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

