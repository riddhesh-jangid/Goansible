import random
import string
import os
from register import registerObj
import writer

class avi_ipaddrgroup:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    addrs = ''
    api_context = ''
    api_version = ''
    apic_epg_name = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    controller = ''
    country_codes = ''
    description = ''
    ip_ports = ''
    marathon_app_name = ''
    marathon_service_port = ''
    password = ''
    prefixes = ''
    ranges = ''
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

