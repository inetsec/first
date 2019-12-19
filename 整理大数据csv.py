# encoding: utf-8
import sys
import time
import pandas as pd
import numpy as np
time1=time.time()
import pandas as pd
# Pandas提供了IO工具可以将大文件分块读取
# 使用不同分块大小来读取再调用 pandas.concat 连接DataFrame，chunkSize设置在1000万条左右速度优化比较明显。
# 实验结果足以说明，在非">5TB"数据的情况下，Python的表现已经能让擅长使用统计分析语言的数据分析师游刃有余。
#reader = pd.read_csv('d:/test.csv',usecols=[0,1,3,5,7],sep='|',index_col=False, iterator=True)
reader = pd.read_csv('G:/78910/pornhub.com-db/pornhub.com-db.csv',usecols=[0,1,3,5,7,8],sep='|',index_col=False, iterator=True,encoding='UTF-8')
loop = True
chunkSize =100000
chunks = []
while loop:
    try:
        chunk = reader.get_chunk(chunkSize)
        chunks.append(chunk)
    except StopIteration:
        loop = False
        print ("Iteration is stopped.")
df = pd.concat(chunks, ignore_index=True)
df['a']=df['a'].str[13:58]
df.columns=['a','b','c','d','e','f']
#print(df['d'])
df['d']=df['d'].replace(np.nan,'0')
#df=df.loc[df['d'].str.contains('Big')]
#df=df.loc[df['d'].str.contains('hd-porn|female-orgasm|celebrity|carton|webcam|threesome|squirt|pornstar|japanese|Big Ass|Big Dick|Big Tits|Bbw')]
#print(df['d'])
#print(df['b'])
df=df.loc[df['b'].str.contains('https://ci.phncdn.com/videos/')]
##df = df[(df['b'].str[29:33]).astype('int')>2018]
df['g']='iframe'
df['h']=1
df['i']=1
df.to_csv('d:/ok.csv',sep='|',index=False)
print (df)
print(df.shape[0])
time2=time.time()
print (u'总共耗时：' + str(time2 - time1) + 's')