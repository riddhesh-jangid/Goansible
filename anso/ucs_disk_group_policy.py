import random
import string
import os
from register import registerObj
import writer

class ucs_disk_group_policy:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    name = ''
    password = ''
    configuration_mode = ''
    description = ''
    drive_type = ''
    manual_disks = ''
    min_drive_size = ''
    num_ded_hot_spares = ''
    num_drives = ''
    num_glob_hot_spares = ''
    org_dn = ''
    port = ''
    proxy = ''
    raid_level = ''
    state = ''
    use_proxy = ''
    use_remaining_disks = ''
    use_ssl = ''
    username = ''
    virtual_drive = ''
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

