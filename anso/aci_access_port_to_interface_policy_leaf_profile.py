import random
import string
import os
from register import registerObj
import writer

class aci_access_port_to_interface_policy_leaf_profile:
    playbook_name = ''
    hosts=[]
    register=[]
    access_port_selector = ''
    from_port = ''
    host = ''
    leaf_interface_profile = ''
    leaf_port_blk = ''
    password = ''
    private_key = ''
    to_port = ''
    certificate_name = ''
    description = ''
    from_card = ''
    interface_type = ''
    leaf_port_blk_description = ''
    output_level = ''
    policy_group = ''
    port = ''
    state = ''
    timeout = ''
    to_card = ''
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

