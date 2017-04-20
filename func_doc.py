#!/usr/bin/python
#encoding=utf8
#Filename:func_doc.py

def printMax(x,y) :
  '''Prints the maximum of two numbers.

试试中文能用吗?
The two values must be integers.'''
  x = int(x) #convert to integers ,if possible
  y = int(y)

  if x > y :
    print x , 'is maximum'
  elif y > x :
    print y , 'is maximum'

printMax(3,5) 
print printMax.__doc__
