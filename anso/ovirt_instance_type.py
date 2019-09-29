import random
import string
import os
from register import registerObj
import writer

class ovirt_instance_type:
    playbook_name = ''
    hosts=[]
    register=[]
    auth = ''
    ballooning_enabled = ''
    boot_devices = ''
    cpu_cores = ''
    cpu_mode = ''
    cpu_pinning = ''
    cpu_sockets = ''
    cpu_threads = ''
    description = ''
    fetch_nested = ''
    graphical_console = ''
    high_availability = ''
    high_availability_priority = ''
    host = ''
    id = ''
    io_threads = ''
    memory = ''
    memory_guaranteed = ''
    memory_max = ''
    name = ''
    nested_attributes = ''
    nics = ''
    operating_system = ''
    placement_policy = ''
    poll_interval = ''
    rng_bytes = ''
    rng_device = ''
    rng_period = ''
    serial_console = ''
    smartcard_enabled = ''
    soundcard_enabled = ''
    state = ''
    timeout = ''
    usb_support = ''
    virtio_scsi = ''
    wait = ''
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

