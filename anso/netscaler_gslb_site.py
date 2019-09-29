import random
import string
import os
from register import registerObj
import writer

class netscaler_gslb_site:
    playbook_name = ''
    hosts=[]
    register=[]
    nitro_pass = ''
    nitro_user = ''
    nsip = ''
    clip = ''
    metricexchange = ''
    naptrreplacementsuffix = ''
    nitro_protocol = ''
    nitro_timeout = ''
    nwmetricexchange = ''
    parentsite = ''
    publicclip = ''
    publicip = ''
    save_config = ''
    sessionexchange = ''
    siteipaddress = ''
    sitename = ''
    sitetype = ''
    state = ''
    triggermonitor = ''
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

