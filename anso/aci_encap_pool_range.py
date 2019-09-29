import random
import string
import os
from register import registerObj
import writer

class aci_encap_pool_range:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    pool_type = ''
    private_key = ''
    allocation_mode = ''
    certificate_name = ''
    description = ''
    output_level = ''
    pool = ''
    pool_allocation_mode = ''
    port = ''
    range_end = ''
    range_name = ''
    range_start = ''
    state = ''
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

