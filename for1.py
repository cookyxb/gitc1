#!/usr/bin/python
# -*- coding: UTF-8 -*-

for num in range(10,20):  # 迭代 10 到 20 之间的数字
   for a in range(2,num): # 根据因子迭代
      if num%a == 0:      # 确定第一个因子
         j=num/a          # 计算第二个因子
         print '%d 等于 %d * %d' % (num,a,j)
         break            # 跳出当前循环
   else:                  # 循环的 else 部分
      print num, '是一个质数'