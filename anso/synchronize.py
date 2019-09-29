import random
import string
import os
from register import registerObj
import writer

class synchronize:
    playbook_name = ''
    hosts=[]
    register=[]
    dest = ''
    src = ''
    archive = ''
    checksum = ''
    compress = ''
    copy_links = ''
    delete = ''
    dest_port = ''
    dirs = ''
    existing_only = ''
    group = ''
    link_dest = ''
    links = ''
    mode = ''
    owner = ''
    partial = ''
    perms = ''
    private_key = ''
    recursive = ''
    rsync_opts = ''
    rsync_path = ''
    rsync_timeout = ''
    set_remote_user = ''
    times = ''
    use_ssh_args = ''
    verify_host = ''
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

