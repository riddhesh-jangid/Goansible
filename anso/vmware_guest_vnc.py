import random
import string
import os
from register import registerObj
import writer

class vmware_guest_vnc:
    playbook_name = ''
    hosts=[]
    register=[]
    datacenter = ''
    folder = ''
    hostname = ''
    name = ''
    name_match = ''
    password = ''
    port = ''
    state = ''
    username = ''
    uuid = ''
    validate_certs = ''
    vnc_ip = ''
    vnc_password = ''
    vnc_port = ''
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

