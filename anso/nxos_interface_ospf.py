import random
import string
import os
from register import registerObj
import writer

class nxos_interface_ospf:
    playbook_name = ''
    hosts=[]
    register=[]
    area = ''
    interface = ''
    ospf = ''
    cost = ''
    dead_interval = ''
    hello_interval = ''
    message_digest = ''
    message_digest_algorithm_type = ''
    message_digest_encryption_type = ''
    message_digest_key_id = ''
    message_digest_password = ''
    network = ''
    passive_interface = ''
    provider = ''
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

