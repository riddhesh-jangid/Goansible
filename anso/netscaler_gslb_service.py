import random
import string
import os
from register import registerObj
import writer

class netscaler_gslb_service:
    playbook_name = ''
    hosts=[]
    register=[]
    nitro_pass = ''
    nitro_user = ''
    nsip = ''
    appflowlog = ''
    cip = ''
    cipheader = ''
    clttimeout = ''
    cnameentry = ''
    comment = ''
    downstateflush = ''
    hashid = ''
    healthmonitor = ''
    ipaddress = ''
    maxaaausers = ''
    maxbandwidth = ''
    maxclient = ''
    monitor_bindings = ''
    monthreshold = ''
    nitro_protocol = ''
    nitro_timeout = ''
    port = ''
    publicip = ''
    publicport = ''
    save_config = ''
    servername = ''
    servicename = ''
    servicetype = ''
    sitename = ''
    sitepersistence = ''
    siteprefix = ''
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

