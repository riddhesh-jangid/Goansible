import random
import string
import os
from register import registerObj
import writer

class kubevirt_pvc:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    namespace = ''
    access_modes = ''
    annotations = ''
    api_key = ''
    ca_cert = ''
    cdi_source = ''
    client_cert = ''
    client_key = ''
    context = ''
    force = ''
    host = ''
    kubeconfig = ''
    labels = ''
    merge_type = ''
    password = ''
    resource_definition = ''
    selector = ''
    size = ''
    state = ''
    storage_class_name = ''
    username = ''
    validate_certs = ''
    volume_mode = ''
    volume_name = ''
    wait = ''
    wait_timeout = ''
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

