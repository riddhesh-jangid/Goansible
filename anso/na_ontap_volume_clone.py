import random
import string
import os
from register import registerObj
import writer

class na_ontap_volume_clone:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    parent_volume = ''
    password = ''
    username = ''
    volume = ''
    vserver = ''
    http_port = ''
    https = ''
    junction_path = ''
    ontapi = ''
    parent_snapshot = ''
    parent_vserver = ''
    qos_policy_group_name = ''
    space_reserve = ''
    state = ''
    validate_certs = ''
    volume_type = ''
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

