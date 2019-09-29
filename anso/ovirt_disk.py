import random
import string
import os
from register import registerObj
import writer

class ovirt_disk:
    playbook_name = ''
    hosts=[]
    register=[]
    auth = ''
    activate = ''
    bootable = ''
    content_type = ''
    description = ''
    download_image_path = ''
    fetch_nested = ''
    force = ''
    format = ''
    host = ''
    id = ''
    image_provider = ''
    interface = ''
    logical_unit = ''
    name = ''
    nested_attributes = ''
    openstack_volume_type = ''
    poll_interval = ''
    profile = ''
    quota_id = ''
    shareable = ''
    size = ''
    sparse = ''
    sparsify = ''
    state = ''
    storage_domain = ''
    storage_domains = ''
    timeout = ''
    upload_image_path = ''
    vm_id = ''
    vm_name = ''
    wait = ''
    wipe_after_delete = ''
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

