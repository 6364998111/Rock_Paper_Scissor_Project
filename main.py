import random

def validate(computer,user):
    if computer == user:
        return None
    elif user == "rock" and computer == "scissor":
        return True
    elif user == "paper" and computer == "rock":
        return True
    elif user == "scissor" and computer == "paper":
        return True
    else:
        return False

mylist=["rock","paper","scissor"]
computer=random.choice(mylist)
print("Rule: if match draw each one will get 1 point")
print("enter number of matches for each league:")
computercount=0
usercount=0
n=int(input())
for i in range(n):
    print("choose rock or paper or scissor:")
    user=input()
    result=validate(computer,user)
    print(f"you choosen {user} and computer choosen {computer}")
    if computer == user:
        print("drawn")
        usercount+=1
        computercount+=1
    elif result:
        print("You won")
        usercount+=1
    else:
        print("you loose")
        computercount+=1
    if computercount == n or usercount == n:
        if usercount == n:
            print("you won the league")
            break
        else:
            print("you loose the league")
            break
