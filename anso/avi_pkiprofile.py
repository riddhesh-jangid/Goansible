import random
import string
import os
from register import registerObj
import writer

class avi_pkiprofile:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    ca_certs = ''
    controller = ''
    created_by = ''
    crl_check = ''
    crls = ''
    ignore_peer_chain = ''
    is_federated = ''
    password = ''
    state = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    url = ''
    username = ''
    uuid = ''
    validate_only_leaf_crl = ''
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

