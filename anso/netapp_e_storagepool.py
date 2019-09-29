import random
import string
import os
from register import registerObj
import writer

class netapp_e_storagepool:
    playbook_name = ''
    hosts=[]
    register=[]
    api_password = ''
    api_url = ''
    api_username = ''
    name = ''
    raid_level = ''
    state = ''
    criteria_drive_count = ''
    criteria_drive_interface_type = ''
    criteria_drive_min_size = ''
    criteria_drive_require_fde = ''
    criteria_drive_type = ''
    criteria_min_usable_capacity = ''
    criteria_size_unit = ''
    erase_secured_drives = ''
    remove_volumes = ''
    reserve_drive_count = ''
    secure_pool = ''
    ssid = ''
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

