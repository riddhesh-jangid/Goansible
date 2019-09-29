import random
import string
import os
from register import registerObj
import writer

class vsphere_guest:
    playbook_name = ''
    hosts=[]
    register=[]
    guest = ''
    password = ''
    username = ''
    vcenter_hostname = ''
    cluster = ''
    esxi = ''
    force = ''
    from_template = ''
    power_on_after_clone = ''
    resource_pool = ''
    snapshot_to_clone = ''
    state = ''
    template_src = ''
    validate_certs = ''
    vm_disk = ''
    vm_extra_config = ''
    vm_hardware = ''
    vm_hw_version = ''
    vm_nic = ''
    vmware_guest_facts = ''
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

