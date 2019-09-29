import random
import string
import os
from register import registerObj
import writer

class meraki_snmp:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_key = ''
    host = ''
    org_id = ''
    org_name = ''
    output_level = ''
    peer_ips = ''
    state = ''
    timeout = ''
    use_https = ''
    use_proxy = ''
    v2c_enabled = ''
    v3_auth_mode = ''
    v3_auth_pass = ''
    v3_enabled = ''
    v3_priv_mode = ''
    v3_priv_pass = ''
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

