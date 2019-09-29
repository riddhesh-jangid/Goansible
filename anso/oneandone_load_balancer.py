import random
import string
import os
from register import registerObj
import writer

class oneandone_load_balancer:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_token = ''
    health_check_interval = ''
    health_check_test = ''
    load_balancer = ''
    method = ''
    name = ''
    persistence = ''
    persistence_time = ''
    rules = ''
    add_rules = ''
    add_server_ips = ''
    api_url = ''
    datacenter = ''
    description = ''
    health_check_parse = ''
    health_check_path = ''
    remove_rules = ''
    remove_server_ips = ''
    state = ''
    wait = ''
    wait_interval = ''
    wait_timeout = ''
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

