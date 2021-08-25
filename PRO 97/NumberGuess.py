import random
randNum=random.randint(1,9)
userNum=int(input("Guess A No. Between 1-9"))
if(userNum==randNum):
    print("Congratulations!!")
elif(userNum>randNum):
    print("Guess A Small No.")
else:
    print("Guess A Big No.")
