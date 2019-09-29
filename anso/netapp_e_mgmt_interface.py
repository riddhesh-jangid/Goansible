import random
import string
import os
from register import registerObj
import writer

class netapp_e_mgmt_interface:
    playbook_name = ''
    hosts=[]
    register=[]
    api_password = ''
    api_url = ''
    api_username = ''
    controller = ''
    address = ''
    channel = ''
    config_method = ''
    dns_address = ''
    dns_address_backup = ''
    dns_config_method = ''
    gateway = ''
    log_path = ''
    name = ''
    ntp_address = ''
    ntp_address_backup = ''
    ntp_config_method = ''
    ssh = ''
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

