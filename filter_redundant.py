# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-01 23:21:25
# LastEditTime: 2024-01-01 23:40:45
# Description: 

origin_file = '新增单词本/待完成/Pulp.Fiction.1994.720p.BluRay.H264.AAC.txt'
new_file = '新增单词本/已完成/Pulp.Fiction.1994.720p.BluRay.H264.AAC.txt'
output_dir = '我的单词本/第一遍'

# 读取
with open(origin_file, 'r') as f:
    words1 = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])
with open(new_file, 'r') as f:
    words2 = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])

redundant_words = words1 - words2 # 不用掌握

output_file = f'{output_dir}/{new_file.split("/")[-1]}'
with open(output_file, 'w') as f:
    for word in redundant_words:
        f.write(f'{word}\n')
