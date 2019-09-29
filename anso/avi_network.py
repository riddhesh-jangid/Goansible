import random
import string
import os
from register import registerObj
import writer

class avi_network:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    cloud_ref = ''
    configured_subnets = ''
    controller = ''
    dhcp_enabled = ''
    exclude_discovered_subnets = ''
    password = ''
    state = ''
    synced_from_se = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    url = ''
    username = ''
    uuid = ''
    vcenter_dvs = ''
    vimgrnw_ref = ''
    vrf_context_ref = ''
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

