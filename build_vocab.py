# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     input_parsing
   Description :
   Author :       xszhou
   date：          2019/4/15
-------------------------------------------------
"""
__author__ = 'xszhou'

'''
输入时一个个句子
词汇表是1000个词汇（包括unk和结束符）
因此需要把句子中的词转化为词汇表中的索引
'''


import collections
from operator import itemgetter

# 这个itemgetter是为了按照counter的值进行排序，实际上用lambda也行
# 另外对于Counter的使用，Counter是dict的子类

RAW_DATA = 'ptb/data/ptb.train.txt'
# 数据样例
#  a <unk> <unk> said this is an old story
VOCAB_OUTPUT = 'ptb/out/ptb.vocab'


counter = collections.Counter()
with open(RAW_DATA, 'r', encoding='utf-8') as f:
    for line in f:
        # 原始数据一行就是一条数据，是用空格隔开的单词序列
        for word in line.strip().split():
            counter[word] += 1

# 按照词频顺序对单词进行排序
sorted_word_cnt = sorted(counter.items(),
                         key=itemgetter(1),
                         reverse=True)
# 从字典中取出第一个值，也就是词本身
sorted_words = [x[0] for x in sorted_word_cnt]
# <EOS>符号表示句子结束符
sorted_words = ['<EOS>'] + sorted_words

# 写入词典
with open(VOCAB_OUTPUT, 'w', encoding='utf-8') as file_out:
    for word in sorted_words:
        file_out.write(word + '\n')
