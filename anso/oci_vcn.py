import random
import string
import os
from register import registerObj
import writer

class oci_vcn:
    playbook_name = ''
    hosts=[]
    register=[]
    api_user = ''
    api_user_fingerprint = ''
    api_user_key_file = ''
    api_user_key_pass_phrase = ''
    auth_type = ''
    cidr_block = ''
    compartment_id = ''
    config_file_location = ''
    config_profile_name = ''
    defined_tags = ''
    display_name = ''
    dns_label = ''
    force_create = ''
    freeform_tags = ''
    key_by = ''
    region = ''
    state = ''
    tenancy = ''
    vcn_id = ''
    wait = ''
    wait_timeout = ''
    wait_until = ''
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

