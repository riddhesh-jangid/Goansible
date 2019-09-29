import random
import string
import os
from register import registerObj
import writer

class mso_schema_template_anp_epg:
    playbook_name = ''
    hosts=[]
    register=[]
    anp = ''
    host = ''
    password = ''
    schema = ''
    template = ''
    bd = ''
    display_name = ''
    epg = ''
    intersite_multicaste_source = ''
    intra_epg_isolation = ''
    output_level = ''
    port = ''
    state = ''
    subnets = ''
    timeout = ''
    use_proxy = ''
    use_ssl = ''
    useg_epg = ''
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

