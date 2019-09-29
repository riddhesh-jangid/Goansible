import random
import string
import os
from register import registerObj
import writer

class bigip_vcmp_guest:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    allowed_slots = ''
    cores_per_slot = ''
    delete_virtual_disk = ''
    initial_image = ''
    mgmt_address = ''
    mgmt_network = ''
    mgmt_route = ''
    min_number_of_slots = ''
    number_of_slots = ''
    partition = ''
    provider = ''
    server_port = ''
    state = ''
    validate_certs = ''
    vlans = ''
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

