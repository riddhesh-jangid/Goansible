import random
import string
import os
from register import registerObj
import writer

class aci_bd_subnet:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    private_key = ''
    bd = ''
    certificate_name = ''
    description = ''
    enable_vip = ''
    gateway = ''
    mask = ''
    nd_prefix_policy = ''
    output_level = ''
    port = ''
    preferred = ''
    route_profile = ''
    route_profile_l3_out = ''
    scope = ''
    state = ''
    subnet_control = ''
    subnet_name = ''
    tenant = ''
    timeout = ''
    use_proxy = ''
    use_ssl = ''
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

