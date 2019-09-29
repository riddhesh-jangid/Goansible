from googlesearch import search
import re
def search_module(query):
    query = query+" in ansible"
    Lsuggest=[]
    for j in search(query, tld="co.in", num=10, stop=10, pause=2):
        if j[:24]=='https://docs.ansible.com':
            j = re.split('/',j)[-1]
            j = re.split('_module',j)[0]
            if j in Lsuggest:
                pass
            else:
                Lsuggest.append(j)
    return Lsuggest            
