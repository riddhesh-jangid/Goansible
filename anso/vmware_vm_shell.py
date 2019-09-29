import random
import string
import os
from register import registerObj
import writer

class vmware_vm_shell:
    playbook_name = ''
    hosts=[]
    register=[]
    vm_id = ''
    vm_password = ''
    vm_shell = ''
    vm_username = ''
    cluster = ''
    datacenter = ''
    folder = ''
    hostname = ''
    password = ''
    port = ''
    timeout = ''
    username = ''
    validate_certs = ''
    vm_id_type = ''
    vm_shell_args = ''
    vm_shell_cwd = ''
    vm_shell_env = ''
    wait_for_process = ''
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

