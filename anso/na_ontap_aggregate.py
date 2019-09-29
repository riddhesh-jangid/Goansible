import random
import string
import os
from register import registerObj
import writer

class na_ontap_aggregate:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    name = ''
    password = ''
    username = ''
    disk_count = ''
    disk_size = ''
    disk_type = ''
    disks = ''
    from_name = ''
    http_port = ''
    https = ''
    is_mirrored = ''
    mirror_disks = ''
    nodes = ''
    ontapi = ''
    raid_size = ''
    raid_type = ''
    service_state = ''
    spare_pool = ''
    state = ''
    time_out = ''
    unmount_volumes = ''
    validate_certs = ''
    wait_for_online = ''
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

