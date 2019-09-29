import random
import string
import os
from register import registerObj
import writer

class vmadm:
    playbook_name = ''
    hosts=[]
    register=[]
    brand = ''
    state = ''
    archive_on_delete = ''
    autoboot = ''
    boot = ''
    cpu_cap = ''
    cpu_shares = ''
    cpu_type = ''
    customer_metadata = ''
    delegate_dataset = ''
    disk_driver = ''
    disks = ''
    dns_domain = ''
    docker = ''
    filesystems = ''
    firewall_enabled = ''
    force = ''
    fs_allowed = ''
    hostname = ''
    image_uuid = ''
    indestructible_delegated = ''
    indestructible_zoneroot = ''
    internal_metadata = ''
    internal_metadata_namespace = ''
    kernel_version = ''
    limit_priv = ''
    maintain_resolvers = ''
    max_locked_memory = ''
    max_lwps = ''
    max_physical_memory = ''
    max_swap = ''
    mdata_exec_timeout = ''
    name = ''
    nic_driver = ''
    nics = ''
    nowait = ''
    qemu_extra_opts = ''
    qemu_opts = ''
    quota = ''
    ram = ''
    resolvers = ''
    routes = ''
    spice_opts = ''
    spice_password = ''
    tmpfs = ''
    uuid = ''
    vcpus = ''
    vga = ''
    virtio_txburst = ''
    virtio_txtimer = ''
    vnc_password = ''
    vnc_port = ''
    zfs_data_compression = ''
    zfs_data_recsize = ''
    zfs_filesystem_limit = ''
    zfs_io_priority = ''
    zfs_root_compression = ''
    zfs_root_recsize = ''
    zfs_snapshot_limit = ''
    zpool = ''
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

