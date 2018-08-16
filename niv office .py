userguess=input("enter a word frome hello ,baloon,animle,mom,dad,winer")
word= [ "hello ","baloon","animle","mom","dad","winer"]
import random
index= str(random.choice(word))
while not index==userguess:
    print("here is a hint" + index[0])
    userguess=input("uess again")
print("winer winer chiken diner")
           
