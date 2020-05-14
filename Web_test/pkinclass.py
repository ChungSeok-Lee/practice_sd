# -*- coding: utf-8 -*-

class c_xy1():
  def __init__(self):  
    pass
  def getPredict1(self, first):
    result = first*2
    return result

class c_xy2():
  def __init__(self):
    pass 
  def getPredict2(self, first):
    result = first/2 + 2
    return result

class c_xy3():
  def __init__(self):
    pass
  def getPredict3(self, first, second):
    result = first + second
    return result

class c_xy4():
  def __init__(self):
    pass
  def getPredict4(self, a, b):
    c, aaa = divmod(a,2)
    cc = c/2
    result = b*3 - cc
    return result