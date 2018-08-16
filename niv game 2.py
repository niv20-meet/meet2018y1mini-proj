
print("i think of a number between 1-100 guess the number ")
import random
number = random.randint(1,100)
guess=int(input("guess"))
if guess < number:
	 print ("to low")
	    
if guess > number:
	 print("to hgih")  
while not guess==number:
	guess=int(input("guess"))
	if guess < number:
	    print ("to low")
	    
	if guess > number:
	     print("to hgih")  

print("winer winer chicken dine")

