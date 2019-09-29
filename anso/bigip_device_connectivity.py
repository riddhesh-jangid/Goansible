import random
import string
import os
from register import registerObj
import writer

class bigip_device_connectivity:
    playbook_name = ''
    hosts=[]
    register=[]
    password = ''
    server = ''
    user = ''
    cluster_mirroring = ''
    config_sync_ip = ''
    failover_multicast = ''
    mirror_primary_address = ''
    mirror_secondary_address = ''
    multicast_address = ''
    multicast_interface = ''
    multicast_port = ''
    provider = ''
    server_port = ''
    unicast_failover = ''
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

