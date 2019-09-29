import random
import string
import os
from register import registerObj
import writer

class gcp_compute_image:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_kind = ''
    name = ''
    description = ''
    disk_size_gb = ''
    family = ''
    guest_os_features = ''
    image_encryption_key = ''
    labels = ''
    licenses = ''
    project = ''
    raw_disk = ''
    scopes = ''
    service_account_contents = ''
    service_account_email = ''
    service_account_file = ''
    source_disk = ''
    source_disk_encryption_key = ''
    source_disk_id = ''
    source_type = ''
    state = ''
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

