import random
import string
import os
from register import registerObj
import writer

class na_ontap_nfs:
    playbook_name = ''
    hosts=[]
    register=[]
    hostname = ''
    password = ''
    username = ''
    vserver = ''
    http_port = ''
    https = ''
    nfsv3 = ''
    nfsv3_fsid_change = ''
    nfsv4 = ''
    nfsv40_acl = ''
    nfsv40_read_delegation = ''
    nfsv40_write_delegation = ''
    nfsv41 = ''
    nfsv41_acl = ''
    nfsv41_read_delegation = ''
    nfsv41_write_delegation = ''
    nfsv4_id_domain = ''
    ontapi = ''
    service_state = ''
    showmount = ''
    state = ''
    tcp = ''
    tcp_max_xfer_size = ''
    udp = ''
    validate_certs = ''
    vstorage_state = ''
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

