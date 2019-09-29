import random
import string
import os
from register import registerObj
import writer

class vmware_host:
    playbook_name = ''
    hosts=[]
    register=[]
    datacenter_name = ''
    esxi_hostname = ''
    add_connected = ''
    cluster_name = ''
    esxi_password = ''
    esxi_ssl_thumbprint = ''
    esxi_username = ''
    fetch_ssl_thumbprint = ''
    folder = ''
    force_connection = ''
    hostname = ''
    password = ''
    port = ''
    reconnect_disconnected = ''
    state = ''
    username = ''
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

