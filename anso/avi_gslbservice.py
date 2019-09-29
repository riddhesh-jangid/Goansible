import random
import string
import os
from register import registerObj
import writer

class avi_gslbservice:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    api_context = ''
    api_version = ''
    application_persistence_profile_ref = ''
    avi_api_patch_op = ''
    avi_api_update_method = ''
    avi_credentials = ''
    controller = ''
    controller_health_status_enabled = ''
    created_by = ''
    description = ''
    domain_names = ''
    down_response = ''
    enabled = ''
    groups = ''
    health_monitor_refs = ''
    health_monitor_scope = ''
    is_federated = ''
    min_members = ''
    num_dns_ip = ''
    password = ''
    pool_algorithm = ''
    site_persistence_enabled = ''
    state = ''
    tenant = ''
    tenant_ref = ''
    tenant_uuid = ''
    ttl = ''
    url = ''
    use_edns_client_subnet = ''
    username = ''
    uuid = ''
    wildcard_match = ''
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

