#! /usr/bin/env python2
#coding=utf-8
import sys
import urllib
import urllib.request
import requests
import re,queue,threading

dummy_event = threading.Event()
dummy_event.wait(timeout=3)
list_url=queue.Queue()  #queue容器
requests.adapters.DEFAULT_RETRIES = 5 # 增加重连次数
s = requests.session()
s.keep_alive = False # 关闭多余连接
#s.proxies = {"https": "47.100.104.247:8080", "http": "36.248.10.47:8080", }
#s.headers = header
#r = s.get(url)
#print r.status_code  # 如果代理可用则正常访问，不可用报以上错误


with open('picc_14.txt','r') as f:
    for i in f.readlines():
        i = i.strip('\n')  # 去除\n
        #i = re.split(' ', i)   空格分割成列表
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
                request = requests.get(urls)
                httpStatusCode = request.status_code
               # print(list_url.queue)
                if httpStatusCode == 200:
                    with open('200.txt','a') as f:
                        f.write(urls + '\n')                        
                else:
                    with open('404.txt','a') as f:
                        f.write(urls + '\n')
            except Exception as e:
                print (e)
        print("退出线程：" + str(self.num))
thread = []
for i in range(15):  #启动多线程 识别状态码是否200
    t=open_url(i)
    thread.append(t)
    t.start()
for i in thread:    #结束多线程
    i.join()


print ("\n程序运行完毕！\n")