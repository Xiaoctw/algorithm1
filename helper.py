import numpy as np
import random
from typing import *

'''
创建点

'''


def make_data(num_data, bound) -> List:
    res = []
    for i in range(num_data):
        x = random.random() * bound
        y = random.random() * bound
        res.append((x, y))
    return res


'''
利用枚举方法找到凸包
'''


def enumerate_data(data: List):
    num_data = len(data)
    # 在三角形内部的点
    in_triangle = set()
    for i in range(num_data):
        for j in range(i + 1, num_data):
            for k in range(j + 1, num_data):
                '''
                i,j,k构成了三角形
                '''
                for p in range(num_data):
                    if p != i and p != j and p != k and judge_in_triangle(data[i][0], data[i][1], data[j][0],
                                                                          data[j][1], data[k][0], data[k][1],
                                                                          data[p][0], data[p][1]):
                        #print(p)
                        in_triangle.add(p)
    left1, right1,left2,right2 = [], [],[],[]
   # print(in_triangle)
    for i in range(num_data):
        if i not in in_triangle:
            left1.append(data[i][0])
            right1.append(data[i][1])
        else:
            left2.append(data[i][0])
            right2.append(data[i][1])
    return left1, right1,left2,right2


'''
判断x,y是否在三角形内部
'''
def judge_in_triangle(ax, ay, bx, by, cx, cy, x, y):
    signT=(bx-ax)*(cy-ay)-(by-ay)*(cx-ax)
    sign1=(bx-ax)*(y-ay)-(by-ay)*(x-ax)
    sign2=(ax-cx)*(y-cy)-(ay-cy)*(x-cx)
    sign3=(cx-bx)*(y-cy)-(cy-by)*(x-cx)
    d1=signT*sign1>0
    d2=signT*sign2>0
    d3=signT*sign3>0
    return d1 and d2 and d3

'''
考虑Graham算法
'''
def graham_scan(data:List):

