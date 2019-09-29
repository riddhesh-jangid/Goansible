import random
import string
import os
from register import registerObj
import writer

class ftd_install:
    playbook_name = ''
    hosts=[]
    register=[]
    console_ip = ''
    console_password = ''
    console_port = ''
    console_username = ''
    device_hostname = ''
    device_password = ''
    image_file_location = ''
    image_version = ''
    rommon_file_location = ''
    device_gateway = ''
    device_ip = ''
    device_model = ''
    device_netmask = ''
    device_new_password = ''
    device_sudo_password = ''
    device_username = ''
    dns_server = ''
    force_install = ''
    search_domains = ''
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

