import random
import string
import os
from register import registerObj
import writer

class openssl_csr:
    playbook_name = ''
    hosts=[]
    register=[]
    path = ''
    privatekey_path = ''
    attributes = ''
    backup = ''
    basic_constraints = ''
    basic_constraints_critical = ''
    common_name = ''
    country_name = ''
    digest = ''
    email_address = ''
    extended_key_usage = ''
    extended_key_usage_critical = ''
    force = ''
    group = ''
    key_usage = ''
    key_usage_critical = ''
    locality_name = ''
    mode = ''
    ocsp_must_staple = ''
    ocsp_must_staple_critical = ''
    organization_name = ''
    organizational_unit_name = ''
    owner = ''
    privatekey_passphrase = ''
    select_crypto_backend = ''
    selevel = ''
    serole = ''
    setype = ''
    seuser = ''
    state = ''
    state_or_province_name = ''
    subject = ''
    subject_alt_name = ''
    subject_alt_name_critical = ''
    unsafe_writes = ''
    use_common_name_for_san = ''
    version = ''
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

