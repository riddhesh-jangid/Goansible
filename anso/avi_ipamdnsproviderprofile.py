import random
import string
import os
from register import registerObj
import writer

class avi_ipamdnsproviderprofile:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    type = ''
    allocate_ip_in_vrf = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    aws_profile = ''
    azure_profile = ''
    controller = ''
    custom_profile = ''
    gcp_profile = ''
    infoblox_profile = ''
    internal_profile = ''
    openstack_profile = ''
    password = ''
    proxy_configuration = ''
    state = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    url = ''
    username = ''
    uuid = ''
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

