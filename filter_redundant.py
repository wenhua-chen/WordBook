# -*- coding:utf-8 -*- 
# Author: 陈文华(Steven)
# Website: https://wenhua-chen.github.io/
# Github: https://github.com/wenhua-chen
# Date: 2024-01-01 23:21:25
# LastEditTime: 2024-01-08 15:52:26
# Description: 

origin_file = '新增单词本/待完成/Oppenheimer.2023.1080p.BluRay.x264.AAC5.1.txt'
new_file = '新增单词本/已完成/Oppenheimer.2023.1080p.BluRay.x264.AAC5.1.txt'
# output_dir = '我的单词本/第一遍'

# 读取
with open(origin_file, 'r') as f:
    words1 = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])
with open(new_file, 'r') as f:
    words2 = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])

redundant_words = words1 - words2 # 不用掌握

# output_file = f'{output_dir}/{new_file.split("/")[-1]}'
output_file = '我的单词本/useless.txt'
with open(output_file, 'a') as f:
    f.write('\n\n')
    for word in redundant_words:
        f.write(f'{word}\n')
