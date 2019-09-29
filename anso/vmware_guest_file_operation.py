import random
import string
import os
from register import registerObj
import writer

class vmware_guest_file_operation:
    playbook_name = ''
    hosts=[]
    register=[]
    vm_id = ''
    vm_password = ''
    vm_username = ''
    cluster = ''
    copy = ''
    datacenter = ''
    directory = ''
    fetch = ''
    folder = ''
    hostname = ''
    password = ''
    port = ''
    username = ''
    validate_certs = ''
    vm_id_type = ''
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

