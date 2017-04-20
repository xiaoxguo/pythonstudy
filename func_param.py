#!/usr/bin/python
#encoding:utf-8
#Filename:func_param.py

def printMax(a,b) :
  if a > b :
    print 'a : ',a , 'is Max param'
  elif b > a :
    print 'b : ',b , 'is Max param'
  else :
    print a,' = ',b

a = int(raw_input('Enter a:'))
b = int(raw_input('Enter b:'))

printMax(a,b)

