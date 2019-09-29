import random
import string
import os
from register import registerObj
import writer

class vmware_resource_pool:
    playbook_name = ''
    hosts=[]
    register=[]
    cluster = ''
    datacenter = ''
    resource_pool = ''
    cpu_expandable_reservations = ''
    cpu_limit = ''
    cpu_reservation = ''
    cpu_shares = ''
    hostname = ''
    mem_expandable_reservations = ''
    mem_limit = ''
    mem_reservation = ''
    mem_shares = ''
    password = ''
    port = ''
    state = ''
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

