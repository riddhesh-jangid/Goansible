import random
import string
import os
from register import registerObj
import writer

class ovirt_snapshot:
    playbook_name = ''
    hosts=[]
    register=[]
    auth = ''
    vm_name = ''
    description = ''
    disk_id = ''
    disk_name = ''
    download_image_path = ''
    fetch_nested = ''
    keep_days_old = ''
    nested_attributes = ''
    poll_interval = ''
    snapshot_id = ''
    state = ''
    timeout = ''
    upload_image_path = ''
    use_memory = ''
    wait = ''
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

