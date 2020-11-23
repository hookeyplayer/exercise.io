#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 01:19:09 2020

@author: xiaofan
"""

from random import choice
# 创建一个类，随机选择前进方向
class RandomWalk():
    def __init__(self, num_points=10):
        self.num_points = num_points
        self.x_values = [0]
        self.y_values = [0]
# 生成随机漫步包含的点
    def fill_walk(self):
# 不断漫步，直到所需数量的点
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4]) 
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4]) 
            y_step = y_direction * y_distance
# 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
# 计算下一个点的x和y值
        next_x = self.x_values[-1] + x_step
        next_y = self.y_values[-1] + y_step
        self.x_values.append(next_x) 
        self.y_values.append(next_y)

import matplotlib.pyplot as plt
rw = RandomWalk()
rw.fill_walk()
plt.scatter(rw.x_values, rw.y_values, s=15)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

# 设置绘图窗口的尺寸 
plt.figure(figsize=(10, 6))
plt.show()
        
    