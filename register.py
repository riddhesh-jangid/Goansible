#!/usr/bin/python

import re
def registerObj(play_path):
    display=0
    dict_str="{'msg':{'info':'This Register have all info of task'}}"
    dict_obj = eval(dict_str)
    Lregister=[]
    Lregister.append(dict_obj)
    dict_str=""
    with open(play_path) as pointer:
        for line in pointer:
            get_newnode = re.findall('.*=> {',line)
            get_endnode = re.findall('^}$',line)
            if len(get_newnode)>0:
                display=1
                dict_str="{"
                continue
            if len(get_endnode)>0:
                display=0
                dict_str=dict_str+"}"
                dict_obj=eval(dict_str)
                Lregister.append(dict_obj)
            if display==1:
                    line = line.replace('false',"False")
                    line = line.replace('true',"True")
                    dict_str = dict_str+line
    return Lregister        

