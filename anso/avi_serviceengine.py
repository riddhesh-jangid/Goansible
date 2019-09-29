import random
import string
import os
from register import registerObj
import writer

class avi_serviceengine:
    playbook_name = ''
    hosts=[]
    register=[]
    api_context = ''
    api_version = ''
    availability_zone = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    cloud_ref = ''
    container_mode = ''
    container_type = ''
    controller = ''
    controller_created = ''
    controller_ip = ''
    data_vnics = ''
    enable_state = ''
    flavor = ''
    host_ref = ''
    hypervisor = ''
    mgmt_vnic = ''
    name = ''
    password = ''
    resources = ''
    se_group_ref = ''
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

