#!/usr/bin/env python 
# -*- coding:utf-8 -*-
# _author_= luo

# !/usr/bin/env python
# -*- coding:utf-8 -*-
# _author_ = luo

import os
import random
import configparser
import traceback

config = configparser.ConfigParser()
config.read("config.ini", encoding='UTF-8')
section_name = 'Data_10KB'  # 配置文件模块名称


def genSizeFile1(fileName, fileSize, numb, label, sign1, sign3, Max, Min, pre, kind):
    filePath = "Data_" + fileName + "KB.txt"
    ds = 0
    line = 1
    with open(filePath, "w", encoding="utf-8") as f:
        while ds < fileSize:
            if kind == 0:
                f.write(label + str(line) + sign1 + str(round(random.uniform(Min, Max), pre)))
            elif kind == 1:
                f.write(label + str(line) + sign1 + str(round(random.betavariate(Min, Max), pre)))
            elif kind == 2:
                f.write(label + str(line) + sign1 + str(round(random.expovariate(Min), pre)))
            elif kind == 3:
                f.write(label + str(line) + sign1 + str(round(random.gammavariate(Min, Max), pre)))
            elif kind == 4:
                f.write(label + str(line) + sign1 + str(round(random.gauss(Min, Max), pre)))
            elif kind == 5:
                f.write(label + str(line) + sign1 + str(round(random.lognormvariate(Min, Max), pre)))
            elif kind == 6:
                f.write(label + str(line) + sign1 + str(round(random.normalvariate(Min, Max), pre)))
            f.flush()
            for i in range(1, numb):
                if kind == 0:
                    f.write(sign3 + str(round(random.uniform(Min, Max), pre)))
                elif kind == 1:
                    f.write(sign3 + str(round(random.betavariate(Min, Max), pre)))
                elif kind == 2:
                    f.write(sign3 + str(round(random.expovariate(Min), pre)))
                elif kind == 3:
                    f.write(sign3 + str(round(random.gammavariate(Min, Max), pre)))
                elif kind == 4:
                    f.write(sign3 + str(round(random.gauss(Min, Max), pre)))
                elif kind == 5:
                    f.write(sign3 + str(round(random.lognormvariate(Min, Max), pre)))
                elif kind == 6:
                    f.write(sign3 + str(round(random.normalvariate(Min, Max), pre)))
                f.flush()
                ds = os.path.getsize(filePath)
                # print(os.path.getsize(filePath))
                if ds > fileSize:
                    break
            if ds > fileSize:
                break
            line += 1
            f.write('\n')
            f.flush()
            ds = os.path.getsize(filePath)
            # print(os.path.getsize(filePath))


def genSizeFile11(fileName, fileSize, numb, label, sign1, sign2, sign3, Max, Min, pre, kind):
    filePath = "Data_" + fileName + "KB.txt"
    ds = 0
    line = 1
    with open(filePath, "w", encoding="utf-8") as f:
        while ds < fileSize:
            if kind == 0:
                f.write(label + str(line) + sign1 + sign2[0] + str(round(random.uniform(Min, Max), pre)))
            elif kind == 1:
                f.write(label + str(line) + sign1 + sign2[0] + str(round(random.betavariate(Min, Max), pre)))
            elif kind == 2:
                f.write(label + str(line) + sign1 + sign2[0] + str(round(random.expovariate(Min), pre)))
            elif kind == 3:
                f.write(label + str(line) + sign1 + sign2[0] + str(round(random.gammavariate(Min, Max), pre)))
            elif kind == 4:
                f.write(label + str(line) + sign1 + sign2[0] + str(round(random.gauss(Min, Max), pre)))
            elif kind == 5:
                f.write(label + str(line) + sign1 + sign2[0] + str(round(random.lognormvariate(Min, Max), pre)))
            elif kind == 6:
                f.write(label + str(line) + sign1 + sign2[0] + str(round(random.normalvariate(Min, Max), pre)))
            f.flush()
            for i in range(1, numb):
                if kind == 0:
                    f.write(sign3 + str(round(random.uniform(Min, Max), pre)))
                elif kind == 1:
                    f.write(sign3 + str(round(random.betavariate(Min, Max), pre)))
                elif kind == 2:
                    f.write(sign3 + str(round(random.expovariate(Min), pre)))
                elif kind == 3:
                    f.write(sign3 + str(round(random.gammavariate(Min, Max), pre)))
                elif kind == 4:
                    f.write(sign3 + str(round(random.gauss(Min, Max), pre)))
                elif kind == 5:
                    f.write(sign3 + str(round(random.lognormvariate(Min, Max), pre)))
                elif kind == 6:
                    f.write(sign3 + str(round(random.normalvariate(Min, Max), pre)))
                f.flush()
                ds = os.path.getsize(filePath)
                # print(os.path.getsize(filePath))
                if ds > fileSize:
                    break
            f.write(sign2[1])
            if ds > fileSize:
                break
            line += 1
            f.write('\n')
            f.flush()
            ds = os.path.getsize(filePath)
            # print(os.path.getsize(filePath))


def genSizeFile2(fileName, lineSize, numb, label, sign1, sign3, Max, Min, pre, kind):
    filePath = "Data_" + fileName + "line.txt"
    line = 1
    with open(filePath, "w", encoding="utf-8") as f:
        while 1:
            if kind == 0:
                f.write(label + str(line) + sign1 + str(round(random.uniform(Min, Max), pre)))
            elif kind == 1:
                f.write(label + str(line) + sign1 + str(round(random.betavariate(Min, Max), pre)))
            elif kind == 2:
                f.write(label + str(line) + sign1 + str(round(random.expovariate(Min), pre)))
            elif kind == 3:
                f.write(label + str(line) + sign1 + str(round(random.gammavariate(Min, Max), pre)))
            elif kind == 4:
                f.write(label + str(line) + sign1 + str(round(random.gauss(Min, Max), pre)))
            elif kind == 5:
                f.write(label + str(line) + sign1 + str(round(random.lognormvariate(Min, Max), pre)))
            elif kind == 6:
                f.write(label + str(line) + sign1 + str(round(random.normalvariate(Min, Max), pre)))
            for i in range(1, numb):
                if kind == 0:
                    f.write(sign3 + str(round(random.uniform(Min, Max), pre)))
                elif kind == 1:
                    f.write(sign3 + str(round(random.betavariate(Min, Max), pre)))
                elif kind == 2:
                    f.write(sign3 + str(round(random.expovariate(Min), pre)))
                elif kind == 3:
                    f.write(sign3 + str(round(random.gammavariate(Min, Max), pre)))
                elif kind == 4:
                    f.write(sign3 + str(round(random.gauss(Min, Max), pre)))
                elif kind == 5:
                    f.write(sign3 + str(round(random.lognormvariate(Min, Max), pre)))
                elif kind == 6:
                    f.write(sign3 + str(round(random.normalvariate(Min, Max), pre)))
            line += 1
            if line > lineSize:
                break
            f.write('\n')
            f.flush()


def genSizeFile22(fileName, lineSize, numb, label, sign1, sign2, sign3, Max, Min, pre, kind):
    filePath = "Data_" + fileName + "line.txt"
    ls = 1
    with open(filePath, "w", encoding="utf-8") as f:
        while 1:
            if kind == 0:
                f.write(label + str(ls) + sign1 + sign2[0] + str(round(random.uniform(Min, Max), pre)))
            elif kind == 1:
                f.write(label + str(ls) + sign1 + sign2[0] + str(round(random.betavariate(Min, Max), pre)))
            elif kind == 2:
                f.write(label + str(ls) + sign1 + sign2[0] + str(round(random.expovariate(Min), pre)))
            elif kind == 3:
                f.write(label + str(ls) + sign1 + sign2[0] + str(round(random.gammavariate(Min, Max), pre)))
            elif kind == 4:
                f.write(label + str(ls) + sign1 + sign2[0] + str(round(random.gauss(Min, Max), pre)))
            elif kind == 5:
                f.write(label + str(ls) + sign1 + sign2[0] + str(round(random.lognormvariate(Min, Max), pre)))
            elif kind == 6:
                f.write(label + str(ls) + sign1 + sign2[0] + str(round(random.normalvariate(Min, Max), pre)))
            for i in range(1, numb):
                if kind == 0:
                    f.write(sign3 + str(round(random.uniform(Min, Max), pre)))
                elif kind == 1:
                    f.write(sign3 + str(round(random.betavariate(Min, Max), pre)))
                elif kind == 2:
                    f.write(sign3 + str(round(random.expovariate(Min), pre)))
                elif kind == 3:
                    f.write(sign3 + str(round(random.gammavariate(Min, Max), pre)))
                elif kind == 4:
                    f.write(sign3 + str(round(random.gauss(Min, Max), pre)))
                elif kind == 5:
                    f.write(sign3 + str(round(random.lognormvariate(Min, Max), pre)))
                elif kind == 6:
                    f.write(sign3 + str(round(random.normalvariate(Min, Max), pre)))
            ls += 1
            f.write(sign2[1])
            if ls > lineSize:
                break
            f.write('\n')
            f.flush()


# program start
try:
    Label = config.get(section_name, 'label')
    numb = int(config.get(section_name, 'numb'))
    sign1 = config.get(section_name, 'sign1')
    issign2 = config.get(section_name, 'issign2')
    pre = int(config.get(section_name, 'precision'))
    kind = int(config.get(section_name, 'kind'))
    if issign2 == '0':
        sign3 = config.get(section_name, 'sign3')
        Max = int(config.get(section_name, 'Max'))
        Min = int(config.get(section_name, 'Min'))
        way = int(config.get(section_name, 'way'))

        if way == 1:
            size = config.get(section_name, 'size')
            genSizeFile1(size, int(size) * 1024.0 * 0.994, numb, Label, sign1[1:len(sign1) - 1], sign3, Max, Min, pre, kind)
        elif way == 2:
            size = config.get(section_name, 'size')
            genSizeFile2(size, int(size), numb, Label, sign1[1:len(sign1) - 1], sign3, Max, Min, pre, kind)

    else:
        sign2 = config.get(section_name, 'sign2')
        sign3 = config.get(section_name, 'sign3')
        Max = int(config.get(section_name, 'Max'))
        Min = int(config.get(section_name, 'Min'))
        way = int(config.get(section_name, 'way'))

        if way == 1:
            size = config.get(section_name, 'size')
            genSizeFile11(size, int(size) * 1024.0 * 0.994, numb, Label, sign1[1:len(sign1) - 1], sign2, sign3, Max, Min,
                          pre, kind)
        elif way == 2:
            size = config.get(section_name, 'size')
            genSizeFile22(size, int(size), numb, Label, sign1[1:len(sign1) - 1], sign2, sign3, Max, Min, pre, kind)
except :
    traceback.print_exc()

else:
    print ('生成文件成功!')
