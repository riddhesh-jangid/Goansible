import random
import string
import os
from register import registerObj
import writer

class openssl_certificate:
    playbook_name = ''
    hosts=[]
    register=[]
    path = ''
    provider = ''
    acme_accountkey_path = ''
    acme_chain = ''
    acme_challenge_path = ''
    attributes = ''
    backup = ''
    csr_path = ''
    extended_key_usage = ''
    extended_key_usage_strict = ''
    force = ''
    group = ''
    has_expired = ''
    invalid_at = ''
    issuer = ''
    issuer_strict = ''
    key_usage = ''
    key_usage_strict = ''
    mode = ''
    not_after = ''
    not_before = ''
    ownca_digest = ''
    ownca_not_after = ''
    ownca_not_before = ''
    ownca_path = ''
    ownca_privatekey_passphrase = ''
    ownca_privatekey_path = ''
    ownca_version = ''
    owner = ''
    privatekey_passphrase = ''
    privatekey_path = ''
    select_crypto_backend = ''
    selevel = ''
    selfsigned_digest = ''
    selfsigned_not_after = ''
    selfsigned_not_before = ''
    selfsigned_version = ''
    serole = ''
    setype = ''
    seuser = ''
    signature_algorithms = ''
    state = ''
    subject = ''
    subject_alt_name = ''
    subject_alt_name_strict = ''
    subject_strict = ''
    unsafe_writes = ''
    valid_at = ''
    valid_in = ''
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

