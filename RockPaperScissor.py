import random
import time

print("rock...")
time.sleep(1)
print("paper...")
time.sleep(1)
print("scissor...")

sys = random.randint(0, 2)

if sys == 0:
    me = "rock"
elif sys == 1:
    me = "paper"
elif sys == 2:
    me = "scissor"

sys = me

myScore = 0
yourScore = 0

while yourScore < 3 and myScore < 3:

    print (f"Your score = {yourScore} and My score = {myScore}")
    print("************************")
    time.sleep(1)
    you = input("Make your choice :").lower() 
    print(f"it's my turn : {me}")

    if you == me:
        print("We are both equal!")
    elif you == "rock":
        if me == "paper":
            time.sleep(0.5)
            print("I won!")
            myScore += 1
        elif me == "scissor":
            time.sleep(0.5)
            print("You won!")
            yourScore += 1
    elif you == "paper":
        if me == "scissor":
            time.sleep(0.5)
            print("I won!")
            myScore += 1
        elif me == "rock":
            time.sleep(0.5)
            print("You won!")
            yourScore += 1
    elif you == "scissor":
        if me == "rock":
            time.sleep(0.5)
            print("I won!")
            myScore += 1
        elif me == "paper":
            time.sleep(0.5)
            print("You won!")
            yourScore += 1
    else:
        print("Check the spelling, please")
print (f"\n Final score==> You = {yourScore} and Me = {myScore}")


