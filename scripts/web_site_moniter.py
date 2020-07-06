#!/usr/bin/env python
# coding:utf-8


import os, sys, json
reload(sys)
sys.setdefaultencoding('utf-8')

# 将要监控的web站点url添加到urllist列表
# urllist = ["http://baidu.com",
#            "http://www.qq.com",
#            "http://www.sina.com.cn/"]
files = '/data/zabbix/scripts/web_url.txt'

fd = open(files, 'r')
urllist = []
for i in fd.readlines():
    if i[0] != '#':
        urllist.append(i.strip('\n'))
fd.close()


# 这个函数主要是构造出一个特定格式的字典，用于zabbix
def web_site_discovery():
    web_list = []
    web_dict = {"data": None}

    for url in urllist:
        url_dict = {"{#SITENAME}": url.split('|')[0], "{#URL}": url.split('|')[1]}
        web_list.append(url_dict)
        # yield {
        #     "{#SITENAME}": url.split('|')[0],
        #     "{#URL}"]: url.split('|')[1]
        # }

    # print json.dumps(web_list, ensure_ascii=False, encoding='UTF-8')

    web_dict["data"] = web_list
    jsonStr = json.dumps(web_dict, sort_keys=True, indent=4, ensure_ascii=False, encoding='UTF-8',separators=(',', ': ')).replace('[', '{').replace(']', '}')   # 解决汉字乱码
    # print jsonStr
    return jsonStr
# web_site_discovery()

# 这个函数用于测试站点返回的状态码，注意在cmd命令中如果有%{}这种字符要使用占位符代替，否则会报错
def web_site_code():
    cmd = 'curl --connect-timeout 10 -m 20 -o /dev/null -s -w %s %s' % ("%{http_code}", sys.argv[2])
    reply_code = os.popen(cmd).readlines()[0]
    return reply_code


if __name__ == "__main__":
    try:
        if sys.argv[1] == "web_site_discovery":
            print web_site_discovery()
        elif sys.argv[1] == "web_site_code":
            print web_site_code()
        else:
            print "Pls sys.argv[0] web_site_discovery | web_site_code[URL]"
    except Exception as msg:
        print msg
