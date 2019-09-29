import random
import string
import os
from register import registerObj
import writer

class cloudscale_server:
    playbook_name = ''
    hosts=[]
    register=[]
    anti_affinity_with = ''
    api_timeout = ''
    api_token = ''
    bulk_volume_size_gb = ''
    flavor = ''
    force = ''
    image = ''
    name = ''
    password = ''
    server_groups = ''
    ssh_keys = ''
    state = ''
    use_ipv6 = ''
    use_private_network = ''
    use_public_network = ''
    user_data = ''
    uuid = ''
    volume_size_gb = ''
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

