import random
import string
import os
from register import registerObj
import writer

class apache2_mod_proxy:
    playbook_name = ''
    hosts=[]
    register=[]
    balancer_vhost = ''
    balancer_url_suffix = ''
    member_host = ''
    state = ''
    tls = ''
    validate_certs = ''
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

