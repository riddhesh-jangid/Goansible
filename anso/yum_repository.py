import random
import string
import os
from register import registerObj
import writer

class yum_repository:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    async = ''
    attributes = ''
    bandwidth = ''
    baseurl = ''
    cost = ''
    deltarpm_metadata_percentage = ''
    deltarpm_percentage = ''
    description = ''
    enabled = ''
    enablegroups = ''
    exclude = ''
    failovermethod = ''
    file = ''
    gpgcakey = ''
    gpgcheck = ''
    gpgkey = ''
    group = ''
    http_caching = ''
    include = ''
    includepkgs = ''
    ip_resolve = ''
    keepalive = ''
    keepcache = ''
    metadata_expire = ''
    metadata_expire_filter = ''
    metalink = ''
    mirrorlist = ''
    mirrorlist_expire = ''
    mode = ''
    owner = ''
    password = ''
    priority = ''
    protect = ''
    proxy = ''
    proxy_password = ''
    proxy_username = ''
    repo_gpgcheck = ''
    reposdir = ''
    retries = ''
    s3_enabled = ''
    selevel = ''
    serole = ''
    setype = ''
    seuser = ''
    skip_if_unavailable = ''
    ssl_check_cert_permissions = ''
    sslcacert = ''
    sslclientcert = ''
    sslclientkey = ''
    sslverify = ''
    state = ''
    throttle = ''
    timeout = ''
    ui_repoid_vars = ''
    unsafe_writes = ''
    username = ''
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

