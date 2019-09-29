import random
import string
import os
from register import registerObj
import writer

class avi_vrfcontext:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    bgp_profile = ''
    cloud_ref = ''
    controller = ''
    debugvrfcontext = ''
    description = ''
    gateway_mon = ''
    internal_gateway_monitor = ''
    password = ''
    state = ''
    static_routes = ''
    system_default = ''
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

