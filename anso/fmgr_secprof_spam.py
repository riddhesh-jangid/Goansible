import random
import string
import os
from register import registerObj
import writer

class fmgr_secprof_spam:
    playbook_name = ''
    hosts=[]
    register=[]
    adom = ''
    comment = ''
    external = ''
    flow_based = ''
    gmail = ''
    gmail_log = ''
    imap = ''
    imap_action = ''
    imap_log = ''
    imap_tag_msg = ''
    imap_tag_type = ''
    mapi = ''
    mapi_action = ''
    mapi_log = ''
    mode = ''
    msn_hotmail = ''
    msn_hotmail_log = ''
    name = ''
    options = ''
    pop3 = ''
    pop3_action = ''
    pop3_log = ''
    pop3_tag_msg = ''
    pop3_tag_type = ''
    replacemsg_group = ''
    smtp = ''
    smtp_action = ''
    smtp_hdrip = ''
    smtp_local_override = ''
    smtp_log = ''
    smtp_tag_msg = ''
    smtp_tag_type = ''
    spam_bwl_table = ''
    spam_bword_table = ''
    spam_bword_threshold = ''
    spam_filtering = ''
    spam_iptrust_table = ''
    spam_log = ''
    spam_log_fortiguard_response = ''
    spam_mheader_table = ''
    spam_rbl_table = ''
    yahoo_mail = ''
    yahoo_mail_log = ''
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

