import random
import string
import os
from register import registerObj
import writer

class lxd_container:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    architecture = ''
    client_cert = ''
    client_key = ''
    config = ''
    devices = ''
    ephemeral = ''
    force_stop = ''
    snap_url = ''
    source = ''
    state = ''
    timeout = ''
    trust_password = ''
    url = ''
    wait_for_ipv4_addresses = ''
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

