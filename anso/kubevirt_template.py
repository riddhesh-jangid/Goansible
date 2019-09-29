import random
import string
import os
from register import registerObj
import writer

class kubevirt_template:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    namespace = ''
    api_key = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    context = ''
    default_disk = ''
    default_network = ''
    default_nic = ''
    default_volume = ''
    description = ''
    display_name = ''
    documentation_url = ''
    editable = ''
    force = ''
    host = ''
    icon_class = ''
    kubeconfig = ''
    long_description = ''
    merge_type = ''
    objects = ''
    parameters = ''
    password = ''
    provider_display_name = ''
    state = ''
    support_url = ''
    username = ''
    validate_certs = ''
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

