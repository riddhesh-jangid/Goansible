import random
import string
import os
from register import registerObj
import writer

class rax_mon_check:
    playbook_name = ''
    hosts=[]
    register=[]
    check_type = ''
    entity_id = ''
    label = ''
    api_key = ''
    auth_endpoint = ''
    credentials = ''
    details = ''
    disabled = ''
    env = ''
    identity_type = ''
    metadata = ''
    monitoring_zones_poll = ''
    period = ''
    region = ''
    state = ''
    target_alias = ''
    target_hostname = ''
    tenant_id = ''
    tenant_name = ''
    timeout = ''
    username = ''
    validate_certs = ''
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

