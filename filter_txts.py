# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-24 10:29:10
# LastEditTime: 2023-12-31 11:34:13
# Description: 过滤txt文件, 输出生词本(覆盖原文件), 计算生词率

import glob
import os
from tqdm import tqdm

# 输入准备
path = '新增单词本/待完成'
if os.path.isdir(path):
    files = glob.glob(f'{path}/*.txt')
else:
    files = [path]

# 我的单词列表
txts = '我的单词本/*'
mywords = set()
for txt in glob.glob(txts):
    with open(txt,'r') as f:
        words = set([word.strip() for word in f.readlines()])
    mywords = mywords.union(words)

for file in files:
    print(f'\n{file}')
    
    # 读取
    with open(file, 'r') as f:
        words = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])
    
    # 过滤
    new_words = set()
    for word in tqdm(words):
        if word.endswith('s') and ((word[:-1] in words) or (word[:-1] in mywords)):
            continue
        if (word.endswith('ed') or word.endswith('in')) and ((word[:-2] in words) or (word[:-2] in mywords)):
            continue
        if word.endswith('ing') and ((word[:-3] in words) or (word[:-3] in mywords)):
            continue
        new_words.add(word)

    # 输出
    print(f'生词率: {len(new_words)}/{len(words)} = {len(new_words)*100/len(words):.2f}%')
    s_words = []
    char3_words = []
    with open(f'{file[:-4]}.txt', 'w') as f:
        for word in new_words:
            if len(word) == 3:
                char3_words.append(word)
            elif word.endswith('s'):
                s_words.append(word)
            else:
                f.write(f'{word}\n')
        # 筛选出s结尾的单词, 放在一起
        for word in s_words:
            f.write(f'{word}\n')
        # 筛选出3个char的单词, 放在一起
        for word in char3_words:
            f.write(f'{word}\n')
