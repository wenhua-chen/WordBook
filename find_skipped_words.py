# 找到在添加到多墨时, 漏掉的单词

if __name__ == '__main__':
    in_file1 = '我的单词本/未掌握/alfred_2023_1.txt' # 原有单词表
    in_file2 = 'alfred_1-全部(235).txt' # 导入多墨后的单词表

    with open(in_file1,'r') as f:
        file1_words = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])
    with open(in_file2,'r') as f:
        file2_words = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])

    words = file1_words - file2_words
    with open(in_file2, 'w') as f:
        for word in words:
            f.write(f'{word}\n')
