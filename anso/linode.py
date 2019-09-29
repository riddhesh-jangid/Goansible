import random
import string
import os
from register import registerObj
import writer

class linode:
    playbook_name = ''
    hosts=[]
    register=[]
    name = ''
    additional_disks = ''
    alert_bwin_enabled = ''
    alert_bwin_threshold = ''
    alert_bwout_enabled = ''
    alert_bwout_threshold = ''
    alert_bwquota_enabled = ''
    alert_bwquota_threshold = ''
    alert_cpu_enabled = ''
    alert_cpu_threshold = ''
    alert_diskio_enabled = ''
    alert_diskio_threshold = ''
    api_key = ''
    backupweeklyday = ''
    datacenter = ''
    displaygroup = ''
    distribution = ''
    kernel_id = ''
    linode_id = ''
    password = ''
    payment_term = ''
    plan = ''
    private_ip = ''
    ssh_pub_key = ''
    state = ''
    swap = ''
    wait = ''
    wait_timeout = ''
    watchdog = ''
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

