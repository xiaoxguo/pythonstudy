#!/usr/bin/python
#encoding:utf-8
#Filename:func_global.py

def func(number) :
  global x
  print "x is " , x
  
  x = number
  print "Changed local x to " , x 

x = 50 
print x 
local = raw_input('Enter something :')
func(local)

print "Value of x is " , x

