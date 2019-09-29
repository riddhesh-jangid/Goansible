import random
import string
import os
from register import registerObj
import writer

class proxmox_kvm:
    playbook_name = ''
    hosts=[]
    register=[]
    api_host = ''
    api_user = ''
    acpi = ''
    agent = ''
    api_password = ''
    args = ''
    autostart = ''
    balloon = ''
    bios = ''
    boot = ''
    bootdisk = ''
    clone = ''
    cores = ''
    cpu = ''
    cpulimit = ''
    cpuunits = ''
    delete = ''
    description = ''
    digest = ''
    force = ''
    format = ''
    freeze = ''
    full = ''
    hostpci = ''
    hotplug = ''
    hugepages = ''
    ide = ''
    keyboard = ''
    kvm = ''
    localtime = ''
    lock = ''
    machine = ''
    memory = ''
    migrate_downtime = ''
    migrate_speed = ''
    name = ''
    net = ''
    newid = ''
    node = ''
    numa = ''
    onboot = ''
    ostype = ''
    parallel = ''
    pool = ''
    protection = ''
    reboot = ''
    revert = ''
    sata = ''
    scsi = ''
    scsihw = ''
    serial = ''
    shares = ''
    skiplock = ''
    smbios = ''
    snapname = ''
    sockets = ''
    startdate = ''
    startup = ''
    state = ''
    storage = ''
    tablet = ''
    target = ''
    tdf = ''
    template = ''
    timeout = ''
    update = ''
    validate_certs = ''
    vcpus = ''
    vga = ''
    virtio = ''
    vmid = ''
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

