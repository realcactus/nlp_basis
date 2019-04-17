# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     input_parsing
   Description :
   Author :       xszhou
   date：          2019/4/17
-------------------------------------------------
"""
__author__ = 'xszhou'

# 将原始输入文本转化为编号序列，编号即词在词典中的序号

RAW_DATA = 'ptb/data/ptb.train.txt'
# 数据样例
#  a <unk> <unk> said this is an old story
VOCAB_FILE = 'ptb/out/ptb.vocab'

# 将单词替换为单词编号后的输出文件
OUTPUT_DATA = 'ptb/out/ptb.train'


# 低频词 返回<unk>的索引
def get_id(word, word_to_id):
    if word in word_to_id:
        return word_to_id[word]
    else:
        return word_to_id['<unk>']


if __name__ == '__main__':
    # 读取词汇表，建立词汇到单词编号的映射
    with open(VOCAB_FILE, 'r', encoding='utf-8') as f_vocab:
        vocab = [x.strip() for x in f_vocab.readlines()]
    # 这里用了这个zip函数
    # python3中zip返回的是一个对象，需要手动转化为list，当然这里不用list()也行，因为zip对象也是iterable的
    word_to_id = {w: v for (w, v) in list(zip(vocab, range(len(vocab))))}

    fin = open(RAW_DATA, 'r', encoding='utf-8')
    fout = open(OUTPUT_DATA, 'w', encoding='utf-8')
    for line in fin.readlines():
        # 单词结尾加上<EOS>
        words = line.strip().split() + ['<EOS>']
        # 用序号替换单词本身
        # 这里加换行只是因为将这个中间结果输出到文件中 有换行比较清晰
        out_line = ''.join([str(get_id(w, word_to_id))+' ' for w in words]) + '\n'
        fout.write(out_line)
    fin.close()
    fout.close()
