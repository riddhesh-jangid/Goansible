import random
import string
import os
from register import registerObj
import writer

class gce_lb:
    playbook_name = ''
    hosts=[]
    register=[]
    credentials_file = ''
    external_ip = ''
    httphealthcheck_healthy_count = ''
    httphealthcheck_host = ''
    httphealthcheck_interval = ''
    httphealthcheck_name = ''
    httphealthcheck_path = ''
    httphealthcheck_port = ''
    httphealthcheck_timeout = ''
    httphealthcheck_unhealthy_count = ''
    members = ''
    name = ''
    pem_file = ''
    port_range = ''
    project_id = ''
    protocol = ''
    region = ''
    service_account_email = ''
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

