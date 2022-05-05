import os
import random

trainval_percent = 0.1
train_percent = 0.9
xmlfilepath = 'C:/Users/pc/Desktop/煤矸数据集/VOC2007/Annotations'
txtsavepath = 'C:/Users/pc/Desktop/煤矸数据/VOC2007/ImageSets'
total_xml = os.listdir(xmlfilepath)

num = len(total_xml)
list = range(num)
tv = int(num * trainval_percent)
tr = int(tv * train_percent)
trainval = random.sample(list, tv)
train = random.sample(trainval, tr)

ftrainval = open('C:/Users/pc\Desktop/煤矸数据集/VOC2007/ImageSets/Main/trainval.txt', 'w')
ftest = open('C:/Users/pc/Desktop/煤矸数据集/VOC2007/ImageSets/Main/test.txt', 'w')
ftrain = open('C:/Users/pc/Desktop/煤矸数据集/VOC2007/ImageSets/Main/train.txt', 'w')
fval = open('C:/Users/pc/Desktop/煤矸数据集/VOC2007/ImageSets/Main/val.txt', 'w')

for i in list:
    name = total_xml[i][:-4] + '\n'
    if i in trainval:
        ftrainval.write(name)
        if i in train:
            ftest.write(name)
        else:
            fval.write(name)
    else:
        ftrain.write(name)

ftrainval.close()
ftrain.close()
fval.close()
ftest.close()
