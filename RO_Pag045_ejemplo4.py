#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 18:22:17 2023

@author: linkat
"""
# RO_Pag045_ejemplo4.py


a = int(input("a = "))
b = int(input("b = "))

x = 0

if a < 5 :
    x = x + a - b
    print("x = ", x)
else:
    x = x + a
    while x <= b :
        x = x + a
    print("x = ", x)
print("x = ", x)

        