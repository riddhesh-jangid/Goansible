import random
import string
import os
from register import registerObj
import writer

class aci_domain_to_encap_pool:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    pool_type = ''
    private_key = ''
    certificate_name = ''
    domain = ''
    domain_type = ''
    output_level = ''
    pool = ''
    pool_allocation_mode = ''
    port = ''
    state = ''
    timeout = ''
    use_proxy = ''
    use_ssl = ''
    username = ''
    validate_certs = ''
    vm_provider = ''
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

