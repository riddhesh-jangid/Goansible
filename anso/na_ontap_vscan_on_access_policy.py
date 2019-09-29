import random
import string
import os
from register import registerObj
import writer

class na_ontap_vscan_on_access_policy:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    password = ''
    policy_name = ''
    username = ''
    vserver = ''
    file_ext_to_exclude = ''
    file_ext_to_include = ''
    filters = ''
    http_port = ''
    https = ''
    is_scan_mandatory = ''
    max_file_size = ''
    ontapi = ''
    paths_to_exclude = ''
    scan_files_with_no_ext = ''
    state = ''
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

