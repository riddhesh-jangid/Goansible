import random
import string
import os
from register import registerObj
import writer

class netscaler_service:
    playbook_name = ''
    hosts=[]
    register=[]
    nitro_pass = ''
    nitro_user = ''
    nsip = ''
    accessdown = ''
    appflowlog = ''
    cacheable = ''
    cachetype = ''
    cip = ''
    cipheader = ''
    cka = ''
    cleartextport = ''
    clttimeout = ''
    cmp = ''
    comment = ''
    customserverid = ''
    disabled = ''
    dnsprofilename = ''
    downstateflush = ''
    graceful = ''
    hashid = ''
    healthmonitor = ''
    httpprofilename = ''
    ip = ''
    ipaddress = ''
    maxbandwidth = ''
    maxclient = ''
    maxreq = ''
    monitor_bindings = ''
    monthreshold = ''
    name = ''
    netprofile = ''
    nitro_protocol = ''
    nitro_timeout = ''
    pathmonitor = ''
    pathmonitorindv = ''
    port = ''
    processlocal = ''
    rtspsessionidremap = ''
    save_config = ''
    serverid = ''
    servername = ''
    servicetype = ''
    sp = ''
    state = ''
    svrtimeout = ''
    tcpb = ''
    tcpprofilename = ''
    td = ''
    useproxyport = ''
    usip = ''
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

