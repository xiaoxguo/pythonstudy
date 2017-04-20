#!/usr/bin/python
#encoding:utf-8
#Filename:while.py
number = 23 
running = True 

while (running) :
  #不加encoding:utf-8连中文注释都会报错 
  #这里如果不加int()会一直走到guess>number里面不知道为什
  guess = int(raw_input("Enter an integer :")) 

  if guess == number : 
    print "Congratulations, you guessed it "
    running = False
  elif guess > number : 
    print "No, it is a little lower than that ."
  else:
    print "No,it is a little highter than that ."
else: 
  print "The while loop is over" 
  #Do anything else you want to do here
print 'Done'

