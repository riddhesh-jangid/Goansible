import random
import string
import os
from register import registerObj
import writer

class cs_instance:
    playbook_name = ''
    hosts=[]
    register=[]
    account = ''
    affinity_groups = ''
    allow_root_disk_shrink = ''
    api_http_method = ''
    api_key = ''
    api_region = ''
    api_secret = ''
    api_timeout = ''
    api_url = ''
    cpu = ''
    cpu_speed = ''
    details = ''
    disk_offering = ''
    disk_size = ''
    display_name = ''
    domain = ''
    force = ''
    group = ''
    host = ''
    hypervisor = ''
    ip6_address = ''
    ip_address = ''
    ip_to_networks = ''
    iso = ''
    keyboard = ''
    memory = ''
    name = ''
    networks = ''
    poll_async = ''
    project = ''
    root_disk_size = ''
    security_groups = ''
    service_offering = ''
    ssh_key = ''
    state = ''
    tags = ''
    template = ''
    template_filter = ''
    user_data = ''
    zone = ''
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

