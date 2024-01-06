# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2023-12-28 11:14:52
# LastEditTime: 2024-01-06 14:34:23
# Description: 统计单词量

import glob

for path in ['我的单词本', '新增单词本']:
    files = glob.glob(f'{path}/**/*.txt', recursive=True)

    mywords = set()
    for file in files:
        with open(file,'r') as f:
            words = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])
        mywords = mywords.union(words)

    print(f'"{path}"的单词量: {len(mywords)}')
