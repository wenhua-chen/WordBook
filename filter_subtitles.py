# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-27 12:17:19
# LastEditTime: 2023-12-31 11:32:32
# Description: 过滤字幕文件, 输出生词本, 计算生词率

from collections import Counter, defaultdict
from pysubs2 import SSAFile
from tqdm import tqdm
import re
import os
import glob
import spacy
nlp = spacy.load('en_core_web_sm')


# 参数
# file = '字幕文件/处理中/Oppenheimer.2023.1080p.BluRay.x264.AAC5.1.srt'
# file = '字幕文件/待处理/Leave.The.World.Behind.2023.1080p.WEBRip.x264.AAC5.1-[YTS.MX].srt'
# file = '字幕文件/待处理/Pulp.Fiction.1994.720p.BluRay.H264.AAC.srt'
# file = '字幕文件/待处理/Taylor.Swift.The.Eras.Tour.2023.EXTENDED.1080p.WEBRip.x264.AAC5.1.srt'
path = '字幕文件'

if os.path.isdir(path):
    files = glob.glob(f'{path}/*.srt')
else:
    files = [path]


# 我的单词列表
txts = '我的单词本/*'
mywords = set()
for txt in glob.glob(txts):
    with open(txt,'r') as f:
        words = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])
    mywords = mywords.union(words)

for file in files:
    print('\n'+file)

    # 获得所有字幕
    subs = SSAFile.load(file)
    text = '\n'.join([line.plaintext for line in tqdm(subs)])

    # 获得专有名词
    ents = nlp(text).ents
    names = set(re.findall("[a-zA-Z]+", ' '.join(map(str, ents))))

    # 合并计数
    words = defaultdict(int)
    counter = Counter(re.findall("[a-zA-Z]+", text))
    for k, v in counter.items():
        # 过滤
        if (len(k) > 2) and (k not in names) and (k.lower() not in mywords):
            k = k.lower()
            if k.endswith('s') and ((k[:-1] in counter) or (k[:-1] in mywords)):
                continue
            if (k.endswith('ed') or k.endswith('in')) and ((k[:-2] in counter) or (k[:-2] in mywords)):
                continue
            if k.endswith('ing') and ((k[:-3] in counter) or (k[:-3] in mywords)):
                continue
            words[k] += v

    # 按照(频率, len(word))排序
    words = sorted([(k,v) for k, v in words.items()], key=lambda x: (-x[1], len(x[0])))
    
    # 输出
    print(f'生词率: {len(words)}/{len(subs)} = {len(words)*100/len(subs):.2f}%')
    s_words = []
    char3_words = []
    with open(f'{file[:-4]}.txt', 'w') as f:
        for k,v in words:
            if len(k) == 3:
                char3_words.append((k,v))
            elif k.endswith('s'):
                s_words.append((k,v))
            else:
                f.write(f'{v:<10}{k}\n')
        # 筛选出s结尾的单词, 放在一起
        for k, v in s_words:
            f.write(f'{v:<10}{k}\n')
        # 筛选出3个char的单词, 放在一起
        for k, v in char3_words:
            f.write(f'{v:<10}{k}\n')