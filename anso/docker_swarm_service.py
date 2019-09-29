import random
import string
import os
from register import registerObj
import writer

class docker_swarm_service:
    playbook_name = ''
    hosts=[]
    register=[]
    image = ''
    name = ''
    state = ''
    api_version = ''
    args = ''
    ca_cert = ''
    client_cert = ''
    client_key = ''
    command = ''
    configs = ''
    constraints = ''
    container_labels = ''
    debug = ''
    dns = ''
    dns_options = ''
    dns_search = ''
    docker_host = ''
    endpoint_mode = ''
    env = ''
    env_files = ''
    force_update = ''
    groups = ''
    healthcheck = ''
    hostname = ''
    hosts = ''
    labels = ''
    limit_cpu = ''
    limit_memory = ''
    limits = ''
    log_driver = ''
    log_driver_options = ''
    logging = ''
    mode = ''
    mounts = ''
    networks = ''
    placement = ''
    publish = ''
    read_only = ''
    replicas = ''
    reservations = ''
    reserve_cpu = ''
    reserve_memory = ''
    resolve_image = ''
    restart_config = ''
    restart_policy = ''
    restart_policy_attempts = ''
    restart_policy_delay = ''
    restart_policy_window = ''
    rollback_config = ''
    secrets = ''
    ssl_version = ''
    stop_grace_period = ''
    stop_signal = ''
    timeout = ''
    tls = ''
    tls_hostname = ''
    tty = ''
    update_config = ''
    update_delay = ''
    update_failure_action = ''
    update_max_failure_ratio = ''
    update_monitor = ''
    update_order = ''
    update_parallelism = ''
    user = ''
    validate_certs = ''
    working_dir = ''
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

