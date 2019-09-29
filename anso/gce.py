import random
import string
import os
from register import registerObj
import writer

class gce:
    playbook_name = ''
    hosts=[]
    register=[]
    zone = ''
    credentials_file = ''
    disk_auto_delete = ''
    disk_size = ''
    disks = ''
    external_ip = ''
    external_projects = ''
    image = ''
    image_family = ''
    instance_names = ''
    ip_forward = ''
    machine_type = ''
    metadata = ''
    name = ''
    network = ''
    num_instances = ''
    pem_file = ''
    persistent_boot_disk = ''
    preemptible = ''
    project_id = ''
    service_account_email = ''
    service_account_permissions = ''
    state = ''
    subnetwork = ''
    tags = ''
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

