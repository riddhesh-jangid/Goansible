import random
import string
import os
from register import registerObj
import writer

class ovirt_template:
    playbook_name = ''
    hosts=[]
    register=[]
    auth = ''
    allow_partial_import = ''
    clone_name = ''
    clone_permissions = ''
    cluster = ''
    cluster_mappings = ''
    cpu_profile = ''
    description = ''
    domain_mappings = ''
    exclusive = ''
    export_domain = ''
    fetch_nested = ''
    id = ''
    image_disk = ''
    image_provider = ''
    io_threads = ''
    memory = ''
    memory_guaranteed = ''
    memory_max = ''
    name = ''
    nested_attributes = ''
    operating_system = ''
    poll_interval = ''
    role_mappings = ''
    seal = ''
    state = ''
    storage_domain = ''
    template_image_disk_name = ''
    timeout = ''
    version = ''
    vm = ''
    vnic_profile_mappings = ''
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

