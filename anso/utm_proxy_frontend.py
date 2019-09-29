import random
import string
import os
from register import registerObj
import writer

class utm_proxy_frontend:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    utm_host = ''
    utm_token = ''
    add_content_type_header = ''
    address = ''
    allowed_networks = ''
    certificate = ''
    comment = ''
    disable_compression = ''
    domain = ''
    exceptions = ''
    headers = ''
    htmlrewrite = ''
    htmlrewrite_cookies = ''
    implicitredirect = ''
    lbmethod = ''
    locations = ''
    port = ''
    preservehost = ''
    profile = ''
    state = ''
    status = ''
    type = ''
    utm_port = ''
    utm_protocol = ''
    validate_certs = ''
    xheaders = ''
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
