import random
import string
import os
from register import registerObj
import writer

class vmware_guest_boot_manager:
    playbook_name = ''
    hosts=[]
    register=[]
    boot_delay = ''
    boot_firmware = ''
    boot_order = ''
    boot_retry_delay = ''
    boot_retry_enabled = ''
    enter_bios_setup = ''
    hostname = ''
    name = ''
    name_match = ''
    password = ''
    port = ''
    secure_boot_enabled = ''
    use_instance_uuid = ''
    username = ''
    uuid = ''
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

