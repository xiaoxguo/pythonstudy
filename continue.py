#!/usr/bin/python
#encoding:utf-8
#Filename:continue.py

while True :
  s = raw_input("Enter something :")
  if s == 'quit' :
    break 
  elif len(s) < 3 :
    print '<3'
    continue
  print "Input is of sufficient length" 
  #Do other kinds of processing here 
