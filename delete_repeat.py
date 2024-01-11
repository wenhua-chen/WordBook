# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-10 12:27:03
# LastEditTime: 2024-01-10 12:31:33
# Description: 删除第二个文件中与file1重复的words

file1 = '我的单词本/第二遍/Pulp.Fiction.1994.720p.BluRay.H264.AAC.txt'
file2 = '我的单词本/第一遍/Pulp.Fiction.1994.720p.BluRay.H264.AAC.txt'

with open(file1,'r') as f:
    file1_words = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])
with open(file2,'r') as f:
    file2_words = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])

file2_words -= file1_words
with open(file2, 'w') as f:
    for word in file2_words:
        f.write(f'{word}\n')

