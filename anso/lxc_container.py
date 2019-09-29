import random
import string
import os
from register import registerObj
import writer

class lxc_container:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    archive = ''
    archive_compression = ''
    archive_path = ''
    backing_store = ''
    clone_name = ''
    clone_snapshot = ''
    config = ''
    container_command = ''
    container_config = ''
    container_log = ''
    container_log_level = ''
    directory = ''
    fs_size = ''
    fs_type = ''
    lv_name = ''
    lxc_path = ''
    state = ''
    template = ''
    template_options = ''
    thinpool = ''
    vg_name = ''
    zfs_root = ''
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

