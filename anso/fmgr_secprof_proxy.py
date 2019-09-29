import random
import string
import os
from register import registerObj
import writer

class fmgr_secprof_proxy:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    header_client_ip = ''
    header_front_end_https = ''
    header_via_request = ''
    header_via_response = ''
    header_x_authenticated_groups = ''
    header_x_authenticated_user = ''
    header_x_forwarded_for = ''
    headers = ''
    headers_action = ''
    headers_content = ''
    headers_name = ''
    log_header_change = ''
    mode = ''
    name = ''
    strip_encoding = ''
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

