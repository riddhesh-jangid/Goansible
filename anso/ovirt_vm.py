import random
import string
import os
from register import registerObj
import writer

class ovirt_vm:
    playbook_name = ''
    hosts=[]
    register=[]
    auth = ''
    affinity_group_mappings = ''
    affinity_label_mappings = ''
    allow_partial_import = ''
    ballooning_enabled = ''
    boot_devices = ''
    boot_menu = ''
    cd_iso = ''
    clone = ''
    clone_permissions = ''
    cloud_init = ''
    cloud_init_nics = ''
    cloud_init_persist = ''
    cluster = ''
    cluster_mappings = ''
    comment = ''
    cpu_cores = ''
    cpu_mode = ''
    cpu_pinning = ''
    cpu_shares = ''
    cpu_sockets = ''
    cpu_threads = ''
    custom_compatibility_version = ''
    custom_properties = ''
    delete_protected = ''
    description = ''
    disk_format = ''
    disks = ''
    domain_mappings = ''
    exclusive = ''
    export_domain = ''
    export_ova = ''
    fetch_nested = ''
    force = ''
    force_migrate = ''
    graphical_console = ''
    high_availability = ''
    high_availability_priority = ''
    host = ''
    host_devices = ''
    id = ''
    initrd_path = ''
    instance_type = ''
    io_threads = ''
    kernel_params = ''
    kernel_params_persist = ''
    kernel_path = ''
    kvm = ''
    lease = ''
    lun_mappings = ''
    memory = ''
    memory_guaranteed = ''
    memory_max = ''
    migrate = ''
    name = ''
    nested_attributes = ''
    next_run = ''
    nics = ''
    numa_nodes = ''
    numa_tune_mode = ''
    operating_system = ''
    placement_policy = ''
    poll_interval = ''
    quota_id = ''
    reassign_bad_macs = ''
    rng_device = ''
    role_mappings = ''
    serial_console = ''
    serial_policy = ''
    serial_policy_value = ''
    smartcard_enabled = ''
    soundcard_enabled = ''
    sso = ''
    state = ''
    stateless = ''
    storage_domain = ''
    sysprep = ''
    template = ''
    template_version = ''
    ticket = ''
    timeout = ''
    timezone = ''
    type = ''
    usb_support = ''
    use_latest_template_version = ''
    vmware = ''
    vnic_profile_mappings = ''
    wait = ''
    watchdog = ''
    xen = ''
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

