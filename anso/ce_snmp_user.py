import random
import string
import os
from register import registerObj
import writer

class ce_snmp_user:
    playbook_name = ''
    hosts=[]
    register=[]
    aaa_local_user = ''
    acl_number = ''
    auth_key = ''
    auth_protocol = ''
    priv_key = ''
    priv_protocol = ''
    remote_engine_id = ''
    user_group = ''
    usm_user_name = ''
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

