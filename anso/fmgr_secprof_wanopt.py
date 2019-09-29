import random
import string
import os
from register import registerObj
import writer

class fmgr_secprof_wanopt:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    auth_group = ''
    cifs = ''
    cifs_byte_caching = ''
    cifs_log_traffic = ''
    cifs_port = ''
    cifs_prefer_chunking = ''
    cifs_secure_tunnel = ''
    cifs_status = ''
    cifs_tunnel_sharing = ''
    comments = ''
    ftp = ''
    ftp_byte_caching = ''
    ftp_log_traffic = ''
    ftp_port = ''
    ftp_prefer_chunking = ''
    ftp_secure_tunnel = ''
    ftp_status = ''
    ftp_tunnel_sharing = ''
    http = ''
    http_byte_caching = ''
    http_log_traffic = ''
    http_port = ''
    http_prefer_chunking = ''
    http_secure_tunnel = ''
    http_ssl = ''
    http_ssl_port = ''
    http_status = ''
    http_tunnel_non_http = ''
    http_tunnel_sharing = ''
    http_unknown_http_version = ''
    mapi = ''
    mapi_byte_caching = ''
    mapi_log_traffic = ''
    mapi_port = ''
    mapi_secure_tunnel = ''
    mapi_status = ''
    mapi_tunnel_sharing = ''
    mode = ''
    name = ''
    tcp = ''
    tcp_byte_caching = ''
    tcp_byte_caching_opt = ''
    tcp_log_traffic = ''
    tcp_port = ''
    tcp_secure_tunnel = ''
    tcp_ssl = ''
    tcp_ssl_port = ''
    tcp_status = ''
    tcp_tunnel_sharing = ''
    transparent = ''
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

