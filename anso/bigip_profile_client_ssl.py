import random
import string
import os
from register import registerObj
import writer

class bigip_profile_client_ssl:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    password = ''
    server = ''
    user = ''
    advertised_cert_authority = ''
    allow_expired_crl = ''
    allow_non_ssl = ''
    cert_auth_depth = ''
    cert_key_chain = ''
    ciphers = ''
    client_auth_crl = ''
    client_auth_frequency = ''
    client_certificate = ''
    options = ''
    parent = ''
    partition = ''
    provider = ''
    renegotiation = ''
    retain_certificate = ''
    secure_renegotiation = ''
    server_name = ''
    server_port = ''
    sni_default = ''
    sni_require = ''
    state = ''
    strict_resume = ''
    trusted_cert_authority = ''
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

