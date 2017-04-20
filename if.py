#!/usr/bin/python
#Filename:if.py
number = 23 
guess = (raw_input("Enter an integer : "))

if guess == number :
  print "Congrtulations you guessed it ." #New block starts here
elif guess < number :
  print "No, it is a little higher than that " #Another block
else : 
  print "No , it is a little lower than that"
  #you must have guess > number to reach here 

print "Done " 
