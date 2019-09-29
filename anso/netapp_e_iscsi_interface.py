import random
import string
import os
from register import registerObj
import writer

class netapp_e_iscsi_interface:
    playbook_name = ''
    hosts=[]
    register=[]
    api_password = ''
    api_url = ''
    api_username = ''
    controller = ''
    name = ''
    address = ''
    config_method = ''
    gateway = ''
    log_path = ''
    mtu = ''
    ssid = ''
    state = ''
    subnet_mask = ''
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

