import random
import string
import os
from register import registerObj
import writer

class aci_access_sub_port_block_to_access_port:
    playbook_name = ''
    hosts=[]
    register=[]
    access_port_selector = ''
    from_port = ''
    from_sub_port = ''
    host = ''
    leaf_interface_profile = ''
    leaf_port_blk = ''
    password = ''
    private_key = ''
    to_port = ''
    to_sub_port = ''
    certificate_name = ''
    from_card = ''
    leaf_port_blk_description = ''
    output_level = ''
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

