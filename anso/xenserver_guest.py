import random
import string
import os
from register import registerObj
import writer

class xenserver_guest:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    cdrom = ''
    custom_params = ''
    disks = ''
    folder = ''
    force = ''
    hardware = ''
    home_server = ''
    hostname = ''
    is_template = ''
    linked_clone = ''
    name_desc = ''
    networks = ''
    password = ''
    state = ''
    state_change_timeout = ''
    template = ''
    template_uuid = ''
    username = ''
    uuid = ''
    validate_certs = ''
    wait_for_ip_address = ''
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

