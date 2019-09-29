import random
import string
import os
from register import registerObj
import writer

class azure_rm_virtualnetworkpeering:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    resource_group = ''
    virtual_network = ''
    ad_user = ''
    adfs_authority_url = ''
    allow_forwarded_traffic = ''
    allow_gateway_transit = ''
    allow_virtual_network_access = ''
    api_profile = ''
    auth_source = ''
    cert_validation_mode = ''
    client_id = ''
    cloud_environment = ''
    password = ''
    profile = ''
    remote_virtual_network = ''
    secret = ''
    state = ''
    subscription_id = ''
    tenant = ''
    use_remote_gateways = ''
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

