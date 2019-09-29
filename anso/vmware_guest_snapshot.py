import random
import string
import os
from register import registerObj
import writer

class vmware_guest_snapshot:
    playbook_name = ''
    hosts=[]
    register=[]
    datacenter = ''
    state = ''
    description = ''
    folder = ''
    hostname = ''
    memory_dump = ''
    name = ''
    name_match = ''
    new_description = ''
    new_snapshot_name = ''
    password = ''
    port = ''
    quiesce = ''
    remove_children = ''
    snapshot_name = ''
    use_instance_uuid = ''
    username = ''
    uuid = ''
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

