#!/usr/bin/env python
# -*- conding:utf-8 -*- 
import sys
import time
import pandas as pd
import numpy as np
time1=time.time()
import pandas as pd

reader = pd.read_csv('d:/ok.csv',sep='|',index_col=False, iterator=True,encoding='UTF-8')

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
#df=df.loc[df['d'].str.contains('HD Porn|Female Orgasm|Celebrity|Carton|Webcam|Threesome|Squirt|Pornstar|Japanese|Big Ass|Big Dick|Big Tits|BBW')]
#df.loc[df['d'].str.contains('Carton') is not np,'h'] = '4'
df['c']=df['c'].replace(np.nan,'0')
df['d']=df['d'].replace(np.nan,'0')
df['f']=df['f'].replace(np.nan,'0')
#df=df.loc[df['d'].str.contains('Hd|HD')]
##print(df['f'])
print(df.dtypes)
df=df.loc[df['a'].str.contains('https://www.pornhub.com/embed/ph')]
#df=df.loc[df['c'].str.contains('ア|イ|ウ|エ|オ|カ|キ|ク|ケ|コ|サ|シ|ス|セ|ソ|タ|チ|ツ|テ|ト|ナ|ニ|ヌ|ネ|ノ|ハ|ヒ|フ|ヘ|ホ|マ|ミ|ム|メ|モ|ャ|ユ|ヨ|リ|ル|レ|ロ|ワ|ヲ|ン')]
df=df.loc[df['c'].str.contains('あ|い|う|え|お|か|き|く|け|こ|さ|し|す|せ|そ|た|ち|つ|て|と|な|に|ぬ|ね|の|は|ひ|ふ|へ|ほ|ま|み|む|め|も|や|い|ゆ|え|よ|ら|り|る|れ|ろ|わ|を|ん')]
###df=df.loc[df['d'].str.contains('Japanese')]
#df=df[(df['f'].str.len())>4] #播放数很多的
##df=df.loc[df['d'].str.contains('Cartoon')]

#df=df.tail(500)
df['i']=21
df.to_csv('d:/okok.csv',sep='|',index=False)
print (df)
print(df.shape[0])
time2=time.time()
print (u'总共耗时：' + str(time2 - time1) + 's')
