# 删除“我的单词本”中重复的单词, 确保每个词只出现1次

import glob
from tqdm import tqdm

txts = glob.glob(f'未掌握/**/*.txt', recursive=True)
txts += glob.glob(f'基本掌握/**/*.txt', recursive=True)
txts += glob.glob(f'完全掌握/**/*.txt', recursive=True)

mywords = set()
for txt in tqdm(txts):
    # 读取
    with open(txt,'r') as f:
        words = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])
    
    # 去重
    words = [word for word in words if word not in mywords]
    
    # 写入
    with open(txt, 'w') as f:
        for word in words:
            f.write(f'{word}\n')

    # 合并
    mywords = mywords.union(words)
