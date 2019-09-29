import random
import string
import os
from register import registerObj
import writer

class nxos_bgp:
    playbook_name = ''
    hosts=[]
    register=[]
    asn = ''
    bestpath_always_compare_med = ''
    bestpath_aspath_multipath_relax = ''
    bestpath_compare_neighborid = ''
    bestpath_compare_routerid = ''
    bestpath_cost_community_ignore = ''
    bestpath_med_confed = ''
    bestpath_med_missing_as_worst = ''
    bestpath_med_non_deterministic = ''
    cluster_id = ''
    confederation_id = ''
    confederation_peers = ''
    disable_policy_batching = ''
    disable_policy_batching_ipv4_prefix_list = ''
    disable_policy_batching_ipv6_prefix_list = ''
    enforce_first_as = ''
    event_history_cli = ''
    event_history_detail = ''
    event_history_events = ''
    event_history_periodic = ''
    fast_external_fallover = ''
    flush_routes = ''
    graceful_restart = ''
    graceful_restart_helper = ''
    graceful_restart_timers_restart = ''
    graceful_restart_timers_stalepath_time = ''
    isolate = ''
    local_as = ''
    log_neighbor_changes = ''
    maxas_limit = ''
    neighbor_down_fib_accelerate = ''
    provider = ''
    reconnect_interval = ''
    router_id = ''
    shutdown = ''
    state = ''
    suppress_fib_pending = ''
    timer_bestpath_limit = ''
    timer_bgp_hold = ''
    timer_bgp_keepalive = ''
    vrf = ''
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

