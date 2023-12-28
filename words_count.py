# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-28 11:14:52
# LastEditTime: 2023-12-28 14:37:09
# Description: 统计单词量

import glob

# path = '我的单词本'
path = '新增单词本'

files = glob.glob(f'{path}/**/*.txt', recursive=True)

mywords = set()
for file in files:
    with open(file,'r') as f:
        words = set([word.strip() for word in f.readlines()])
    mywords = mywords.union(words)

print(f'"{path}"的单词量: {len(mywords)}')
