# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:09:35 2024

@author: TAM PC
"""

def tim_bo_nghiem(target):
  for x in range(1, target//2 + 1):
    for y in range(1, (target - 2*x)//7 + 1):
      z = (target - 2*x - 7*y) // 9
      if z > 0 and 2*x + 7*y + 9*z == target:
        print(f"Bộ nghiệm: ({x}, {y}, {z})")