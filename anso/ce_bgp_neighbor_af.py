import random
import string
import os
from register import registerObj
import writer

class ce_bgp_neighbor_af:
    playbook_name = ''
    hosts=[]
    register=[]
    af_type = ''
    remote_address = ''
    vrf_name = ''
    add_path_mode = ''
    adv_add_path_num = ''
    advertise_arp = ''
    advertise_community = ''
    advertise_ext_community = ''
    advertise_irb = ''
    advertise_remote_nexthop = ''
    allow_as_loop_enable = ''
    allow_as_loop_limit = ''
    default_rt_adv_enable = ''
    default_rt_adv_policy = ''
    default_rt_match_mode = ''
    discard_ext_community = ''
    export_acl_name_or_num = ''
    export_as_path_filter = ''
    export_as_path_name_or_num = ''
    export_pref_filt_name = ''
    export_rt_policy_name = ''
    import_acl_name_or_num = ''
    import_as_path_filter = ''
    import_as_path_name_or_num = ''
    import_pref_filt_name = ''
    import_rt_policy_name = ''
    ipprefix_orf_enable = ''
    is_nonstd_ipprefix_mod = ''
    keep_all_routes = ''
    nexthop_configure = ''
    orf_mode = ''
    orftype = ''
    origin_as_valid = ''
    preferred_value = ''
    public_as_only = ''
    public_as_only_force = ''
    public_as_only_limited = ''
    public_as_only_replace = ''
    public_as_only_skip_peer_as = ''
    redirect_ip = ''
    redirect_ip_vaildation = ''
    reflect_client = ''
    route_limit = ''
    route_limit_idle_timeout = ''
    route_limit_percent = ''
    route_limit_type = ''
    rt_updt_interval = ''
    soostring = ''
    substitute_as_enable = ''
    update_pkt_standard_compatible = ''
    vpls_ad_disable = ''
    vpls_enable = ''
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

