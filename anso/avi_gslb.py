import random
import string
import os
from register import registerObj
import writer

class avi_gslb:
    playbook_name = ''
    hosts=[]
    register=[]
    leader_cluster_uuid = ''
    name = ''
    api_context = ''
    api_version = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    clear_on_max_retries = ''
    client_ip_addr_group = ''
    controller = ''
    description = ''
    dns_configs = ''
    is_federated = ''
    maintenance_mode = ''
    password = ''
    send_interval = ''
    sites = ''
    state = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    third_party_sites = ''
    url = ''
    username = ''
    uuid = ''
    view_id = ''
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

