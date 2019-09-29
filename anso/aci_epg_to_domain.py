import random
import string
import os
from register import registerObj
import writer

class aci_epg_to_domain:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    private_key = ''
    allow_useg = ''
    ap = ''
    certificate_name = ''
    deploy_immediacy = ''
    domain = ''
    domain_type = ''
    encap = ''
    encap_mode = ''
    epg = ''
    netflow = ''
    output_level = ''
    port = ''
    primary_encap = ''
    resolution_immediacy = ''
    state = ''
    tenant = ''
    timeout = ''
    use_proxy = ''
    use_ssl = ''
    username = ''
    validate_certs = ''
    vm_provider = ''
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

