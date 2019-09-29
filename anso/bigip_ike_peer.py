import random
import string
import os
from register import registerObj
import writer

class bigip_ike_peer:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    description = ''
    partition = ''
    phase1_auth_method = ''
    phase1_cert = ''
    phase1_encryption_algorithm = ''
    phase1_hash_algorithm = ''
    phase1_key = ''
    phase1_perfect_forward_secrecy = ''
    phase1_verify_peer_cert = ''
    presented_id_type = ''
    presented_id_value = ''
    preshared_key = ''
    provider = ''
    remote_address = ''
    server_port = ''
    state = ''
    update_password = ''
    validate_certs = ''
    verified_id_type = ''
    verified_id_value = ''
    version = ''
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

