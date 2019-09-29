import random
import string
import os
from register import registerObj
import writer

class rax_mon_alarm:
    playbook_name = ''
    hosts=[]
    register=[]
    check_id = ''
    entity_id = ''
    label = ''
    notification_plan_id = ''
    api_key = ''
    auth_endpoint = ''
    credentials = ''
    criteria = ''
    disabled = ''
    env = ''
    identity_type = ''
    metadata = ''
    region = ''
    state = ''
    tenant_id = ''
    tenant_name = ''
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

