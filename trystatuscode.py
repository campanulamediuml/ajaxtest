#coding=utf-8
import urllib2
import user_agents
import random
debug = 1
def get_pagehtml(url):
    randomarry = random.choice(user_agents.user_agent_list)
    headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language':'zh-CN,zh;q=0.8,zh-TW;q=0.6',
    'X-Requested-With':'XMLHttpRequest',
    'User-Agent':randomarry
    }
    data = None
    requests = urllib2.Request(url,data,headers)
    try:
        response = urllib2.urlopen(requests,timeout=30)
        result = 200
    except urllib2.HTTPError,e:
        if e.code == 404:
            result = e.code        
    if debug:
        print result
    return result

fh = open('status_code.txt','w')
fh.write(str(get_pagehtml('https://www.amazon.com/dp/'+raw_input('输入asin:'))))
fh.close()