import random
import string
import os
from register import registerObj
import writer

class na_ontap_svm:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    name = ''
    password = ''
    username = ''
    aggr_list = ''
    allowed_protocols = ''
    comment = ''
    from_name = ''
    http_port = ''
    https = ''
    ipspace = ''
    language = ''
    ontapi = ''
    root_volume = ''
    root_volume_aggregate = ''
    root_volume_security_style = ''
    snapshot_policy = ''
    state = ''
    subtype = ''
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

