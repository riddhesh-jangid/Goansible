import random
import string
import os
from register import registerObj
import writer

class kubevirt_cdi_upload:
    playbook_name = ''
    hosts=[]
    register=[]
    pvc_name = ''
    pvc_namespace = ''
    api_key = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    context = ''
    host = ''
    kubeconfig = ''
    merge_type = ''
    password = ''
    path = ''
    upload_host = ''
    upload_host_validate_certs = ''
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

