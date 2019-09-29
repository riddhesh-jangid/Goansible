import random
import string
import os
from register import registerObj
import writer

class avi_poolgroup:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    cloud_config_cksum = ''
    cloud_ref = ''
    controller = ''
    created_by = ''
    deployment_policy_ref = ''
    description = ''
    fail_action = ''
    implicit_priority_labels = ''
    members = ''
    min_servers = ''
    password = ''
    priority_labels_ref = ''
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

