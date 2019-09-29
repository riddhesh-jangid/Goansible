import random
import string
import os
from register import registerObj
import writer

class meraki_vlan:
    playbook_name = ''
    hosts=[]
    register=[]
    appliance_ip = ''
    auth_key = ''
    dns_nameservers = ''
    fixed_ip_assignments = ''
    host = ''
    name = ''
    net_id = ''
    net_name = ''
    org_id = ''
    org_name = ''
    output_level = ''
    reserved_ip_range = ''
    state = ''
    subnet = ''
    timeout = ''
    use_https = ''
    use_proxy = ''
    validate_certs = ''
    vlan_id = ''
    vpn_nat_subnet = ''
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

