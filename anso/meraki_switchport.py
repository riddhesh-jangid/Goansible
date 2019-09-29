import random
import string
import os
from register import registerObj
import writer

class meraki_switchport:
    playbook_name = ''
    hosts=[]
    register=[]
    access_policy_number = ''
    allowed_vlans = ''
    auth_key = ''
    enabled = ''
    host = ''
    isolation_enabled = ''
    link_negotiation = ''
    name = ''
    number = ''
    org_id = ''
    org_name = ''
    output_level = ''
    poe_enabled = ''
    rstp_enabled = ''
    serial = ''
    state = ''
    stp_guard = ''
    tags = ''
    timeout = ''
    type = ''
    use_https = ''
    use_proxy = ''
    validate_certs = ''
    vlan = ''
    voice_vlan = ''
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

