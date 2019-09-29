import random
import string
import os
from register import registerObj
import writer

class aci_interface_policy_port_channel:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    port_channel = ''
    private_key = ''
    certificate_name = ''
    description = ''
    fast_select = ''
    graceful_convergence = ''
    load_defer = ''
    max_links = ''
    min_links = ''
    mode = ''
    output_level = ''
    port = ''
    state = ''
    suspend_individual = ''
    symmetric_hash = ''
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

