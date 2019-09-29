import random
import string
import os
from register import registerObj
import writer

class na_elementsw_cluster:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    management_virtual_ip = ''
    nodes = ''
    password = ''
    storage_virtual_ip = ''
    username = ''
    accept_eula = ''
    attributes = ''
    cluster_admin_password = ''
    cluster_admin_username = ''
    replica_count = ''
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

