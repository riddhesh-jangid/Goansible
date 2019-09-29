import random
import string
import os
from register import registerObj
import writer

class gcp_compute_backend_service:
    playbook_name = ''
    hosts=[]
    register=[]
    auth_kind = ''
    health_checks = ''
    name = ''
    affinity_cookie_ttl_sec = ''
    backends = ''
    cdn_policy = ''
    connection_draining = ''
    description = ''
    enable_cdn = ''
    iap = ''
    load_balancing_scheme = ''
    port_name = ''
    project = ''
    protocol = ''
    scopes = ''
    security_policy = ''
    service_account_contents = ''
    service_account_email = ''
    service_account_file = ''
    session_affinity = ''
    state = ''
    timeout_sec = ''
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

