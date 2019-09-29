import random
import string
import os
from register import registerObj
import writer

class gcp_redis_instance:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_kind = ''
    memory_size_gb = ''
    name = ''
    region = ''
    alternative_location_id = ''
    authorized_network = ''
    display_name = ''
    labels = ''
    location_id = ''
    project = ''
    redis_configs = ''
    redis_version = ''
    reserved_ip_range = ''
    scopes = ''
    service_account_contents = ''
    service_account_email = ''
    service_account_file = ''
    state = ''
    tier = ''
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

