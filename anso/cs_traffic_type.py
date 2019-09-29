import random
import string
import os
from register import registerObj
import writer

class cs_traffic_type:
    playbook_name = ''
    hosts=[]
    register=[]
    physical_network = ''
    traffic_type = ''
    api_http_method = ''
    api_key = ''
    api_region = ''
    api_secret = ''
    api_timeout = ''
    api_url = ''
    hyperv_networklabel = ''
    isolation_method = ''
    kvm_networklabel = ''
    ovm3_networklabel = ''
    poll_async = ''
    state = ''
    vlan = ''
    vmware_networklabel = ''
    xen_networklabel = ''
    zone = ''
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

