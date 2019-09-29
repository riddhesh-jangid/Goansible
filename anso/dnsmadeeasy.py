import random
import string
import os
from register import registerObj
import writer

class dnsmadeeasy:
    playbook_name = ''
    hosts=[]
    register=[]
    account_key = ''
    account_secret = ''
    contactList = ''
    domain = ''
    maxEmails = ''
    port = ''
    protocol = ''
    sensitivity = ''
    state = ''
    systemDescription = ''
    autoFailover = ''
    failover = ''
    httpFile = ''
    httpFqdn = ''
    httpQueryString = ''
    ip1 = ''
    ip2 = ''
    ip3 = ''
    ip4 = ''
    ip5 = ''
    monitor = ''
    record_name = ''
    record_ttl = ''
    record_type = ''
    record_value = ''
    sandbox = ''
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

