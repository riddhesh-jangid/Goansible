import random
import string
import os
from register import registerObj
import writer

class bigip_virtual_server:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    address_translation = ''
    clone_pools = ''
    default_persistence_profile = ''
    description = ''
    destination = ''
    disabled_vlans = ''
    enabled_vlans = ''
    fallback_persistence_profile = ''
    firewall_enforced_policy = ''
    firewall_staged_policy = ''
    insert_metadata = ''
    ip_intelligence_policy = ''
    ip_protocol = ''
    irules = ''
    mask = ''
    metadata = ''
    mirror = ''
    partition = ''
    policies = ''
    pool = ''
    port = ''
    port_translation = ''
    profiles = ''
    provider = ''
    rate_limit = ''
    rate_limit_dst_mask = ''
    rate_limit_mode = ''
    rate_limit_src_mask = ''
    security_log_profiles = ''
    security_nat_policy = ''
    server_port = ''
    snat = ''
    source = ''
    source_port = ''
    state = ''
    type = ''
    validate_certs = ''
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

