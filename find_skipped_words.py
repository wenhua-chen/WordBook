# 找到在添加到多墨时, 漏掉的单词

if __name__ == '__main__':
    in_file1 = '新增单词本/待完成/PTE.txt' # 原有单词表
    in_file2 = 'PTE1-全部(160).txt' # 导入多墨后的单词表
    out_file = 'PTE2.txt' # 漏掉的单词表

    with open(in_file1,'r') as f:
        file1_words = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])
    with open(in_file2,'r') as f:
        file2_words = set([word.strip().lower() for word in f.readlines() if len(word.strip())>0])

    words = file1_words - file2_words
    with open(out_file, 'w') as f:
        for word in words:
            f.write(f'{word}\n')


