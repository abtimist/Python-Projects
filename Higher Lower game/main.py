from art import logo,vs
import random
from game_data import data

def contentgen():
        return random.choice(data)
temp={}
score = 0
while True:
    print(logo+"\n")
    if score!=0:
        print(f"U R RIGHT!!,  Your score is {score}")
    if temp=={}:
        person1=contentgen()
    else:
        person1=temp
    print(f"Compare A: {person1["name"]} a {person1["description"]}, {person1["country"]}")
    print(vs)
    while True:
        person2=contentgen()
        if person2!=person1:
            break
        else:
            continue
    print(f"Compare B: {person2["name"]} a {person2["description"]}, {person2["country"]}")
    guess=input("Who has more followers, a or b: ").lower()
    content=[person1, person2]
    if person1["follower_count"]>person2["follower_count"]:
        correct_guess=0
    else:
        correct_guess=1
    if guess=="a":
        guess=int(0)
    elif guess=="b":
        guess=int(1)
    else:
        print(f"Your final score was {score}")
        break
    print("\n"*20)
    if guess == correct_guess:
        score+=1
        temp=person2
    else:
        print(f"Your final score is {score}\nGame Over!")
        break







