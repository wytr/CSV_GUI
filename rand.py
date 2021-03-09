# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 00:50:02 2021

@author: Martin
"""

import random
randlist = []
charlist = []

for i in range(0,200):
    randlist.append(random.randint(20,160))

for i in range(0,200):
    for j in range(0, randlist[i]):
        print('a', end='')
    print('a')