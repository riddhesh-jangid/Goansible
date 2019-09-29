import random
import string
import os
from register import registerObj
import writer

class netscaler_cs_vserver:
    playbook_name = ''
    hosts=[]
    register=[]
    nitro_pass = ''
    nitro_user = ''
    nsip = ''
    appflowlog = ''
    authentication = ''
    authenticationhost = ''
    authn401 = ''
    authnprofile = ''
    authnvsname = ''
    backupip = ''
    backupvserver = ''
    cacheable = ''
    casesensitive = ''
    clttimeout = ''
    comment = ''
    cookiedomain = ''
    cookietimeout = ''
    dbprofilename = ''
    disabled = ''
    disableprimaryondown = ''
    dnsprofilename = ''
    domainname = ''
    downstateflush = ''
    httpprofilename = ''
    icmpvsrresponse = ''
    insertvserveripport = ''
    ipmask = ''
    ippattern = ''
    ipv46 = ''
    l2conn = ''
    lbvserver = ''
    listenpolicy = ''
    mssqlserverversion = ''
    mysqlcharacterset = ''
    mysqlprotocolversion = ''
    mysqlservercapabilities = ''
    mysqlserverversion = ''
    name = ''
    netprofile = ''
    nitro_protocol = ''
    nitro_timeout = ''
    oracleserverversion = ''
    port = ''
    precedence = ''
    push = ''
    pushlabel = ''
    pushmulticlients = ''
    pushvserver = ''
    range = ''
    redirectportrewrite = ''
    redirecturl = ''
    rhistate = ''
    rtspnat = ''
    save_config = ''
    servicetype = ''
    sitedomainttl = ''
    sobackupaction = ''
    somethod = ''
    sopersistence = ''
    sopersistencetimeout = ''
    sothreshold = ''
    ssl_certkey = ''
    state = ''
    stateupdate = ''
    targettype = ''
    tcpprofilename = ''
    td = ''
    ttl = ''
    validate_certs = ''
    vipheader = ''
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

