import random
import string
import os
from register import registerObj
import writer

class aci_static_binding_to_epg:
    playbook_name = ''
    hosts=[]
    register=[]
    host = ''
    password = ''
    private_key = ''
    ap = ''
    certificate_name = ''
    deploy_immediacy = ''
    description = ''
    encap_id = ''
    epg = ''
    extpaths = ''
    interface = ''
    interface_mode = ''
    interface_type = ''
    leafs = ''
    output_level = ''
    pod_id = ''
    port = ''
    primary_encap_id = ''
    state = ''
    tenant = ''
    timeout = ''
    use_proxy = ''
    use_ssl = ''
    username = ''
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

