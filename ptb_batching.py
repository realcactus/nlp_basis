# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ptb_batching
   Description :
   Author :       xszhou
   date：          2019/4/18
-------------------------------------------------
"""
__author__ = 'xszhou'

# 本来不打算实现语言模型，后来因为这个batch比较奇怪我shape没太搞懂，因此想跑一下调试一下

import numpy as np
import tensorflow as tf

TRAIN_DATA = 'ptb/out/ptb.train'
TRAIN_BATCH_SIZE = 20
TRAIN_NUM_STEP = 35


# 从文件中读取数据，并返回包含单词编号的数组
def read_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as fin:
        # 将整个文档读进一个长字符串
        id_string = ' '.join([line.strip() for line in fin.readlines()])
        id_list = [int(w) for w in id_string.split()]
        return id_list


def make_batches(id_list, batch_size, num_step):
    num_batches = (len(id_list) - 1) // (batch_size * num_step)

    data = np.array(id_list[:num_batches * batch_size * num_step])
    # 这样其实就是最后一个batch后的一部分数据不要了
    # 这里用到了一个技巧，就是先转化成batch_size,*的形状，然后再分
    # 能保证每一个batch里面的数据不是连续的数据
    data = np.reshape(data, [batch_size, num_batches * num_step])
    data_batches = np.split(data, num_batches, axis=1)

    # 前面是输入序列，这里是预测序列label，其实就是比输入序列右移了一位
    label = np.array(id_list[1:num_batches * batch_size * num_step + 1])
    label = np.reshape(label, [batch_size, num_batches * num_step])
    label_batches = np.split(label, num_batches, axis=1)

    return list(zip(data_batches, label_batches))


def main():
    train_batches = make_batches(read_data(TRAIN_DATA), TRAIN_BATCH_SIZE, TRAIN_NUM_STEP)
    # 这里插入模型训练代码
    print('hello')


if __name__ == '__main__':
    main()
