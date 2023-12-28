# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-27 23:23:06
# LastEditTime: 2023-12-27 23:23:22
# Description: 

from collections import Counter, defaultdict
from pysubs2 import SSAFile
from tqdm import tqdm
import re
import glob
import spacy
nlp = spacy.load('en_core_web_sm')


# 参数
file = '字幕文件/待处理/Taylor.Swift.The.Eras.Tour.2023.EXTENDED.1080p.WEBRip.x264.AAC5.1.srt'
print(file)

# 我的单词列表
txts = '单词本/我的单词本/*'
mywords = set()
for txt in glob.glob(txts):
    with open(txt,'r') as f:
        words = set([word.strip() for word in f.readlines()])
    mywords = mywords.union(words)

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
        words[k] += v

# 分开'首字母大写的word'和'全小写的word'
lower_words = {k:v for k, v in words.items() if k.islower()}
title_words = defaultdict(int)
for k, v in words.items():
    if not k.islower():
        if k.lower() in lower_words:
            lower_words[k.lower()] += v
        else:
            title_words[k.lower()] += v

# 按照(频率, len(word))排序
lower_words = sorted([(k,v) for k, v in lower_words.items()], key=lambda x: (-x[1], len(x[0])))
title_words = sorted([(k,v) for k, v in title_words.items()], key=lambda x: (-x[1], len(x[0])))

# 输出
with open(f'{file[:-4]}.txt', 'w') as f:
    for k,v in title_words:
        f.write(f'{v:<10}{k}\n')
    for k,v in lower_words:
        f.write(f'{v:<10}{k}\n')
