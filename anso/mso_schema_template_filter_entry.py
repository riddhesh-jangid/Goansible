import random
import string
import os
from register import registerObj
import writer

class mso_schema_template_filter_entry:
    playbook_name = ''
    hosts=[]
    register=[]
    filter = ''
    host = ''
    password = ''
    schema = ''
    template = ''
    arp_flag = ''
    description = ''
    destination_from = ''
    destination_to = ''
    display_name = ''
    entry = ''
    ethertype = ''
    filter_display_name = ''
    fragments_only = ''
    ip_protocol = ''
    output_level = ''
    port = ''
    source_from = ''
    source_to = ''
    state = ''
    stateful = ''
    tcp_session_rules = ''
    timeout = ''
    use_proxy = ''
    use_ssl = ''
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

