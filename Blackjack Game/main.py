from operator import index
from art import logo
import random
print(logo+"\n\n")
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while True:
    status = input("Do you want to play a game of blackjack?y/n ").lower()
    player_hand = []
    cpu_hand = []
    player_score = sum(player_hand)
    cpu_score = sum(cpu_hand)
    if status == "n":
        print("Goodbye!!")
        break
    for i in range(0, 2):
        player_hand.append(random.choice(cards))
        cpu_hand.append(random.choice(cards))
    player_score = sum(player_hand)
    cpu_score = sum(cpu_hand)

    print(f"Your hand:{player_hand}, Your score: {player_score}")
    print(f"Computer's first card: {cpu_hand[0]}")
    if cpu_score==21:
        print(f"Your final hand:{player_hand}, Your score: {player_score}")
        print(f"Computer's final hand: {cpu_hand}, Computer's score: {cpu_score}")
        print("Computer got the blackjack, You Lose")
        continue
    if player_score == 21:
        print("You got the blackjack, You Win")
        continue
    else:
        while True:
            card_draw = input("Do you want to draw another card? y/n ")
            if card_draw == "n":
                break
            player_hand.append(random.choice(cards))
            player_score = sum(player_hand)
            print(f"Your hand:{player_hand}, Your score: {player_score}")
            print(f"Computer's first card: {cpu_hand[0]}")
            if player_score > 21:
                if 11 in player_hand:
                    player_hand[player_hand.index(11)] = 1
                    player_score = sum(player_hand)
                    continue
                if player_score > 21:
                    print("You went over, You Lose")
                    break
            else:
                continue

        while cpu_score < 17:
            cpu_hand.append(random.choice(cards))
            cpu_score = sum(cpu_hand)
        if cpu_score > 21:
            if 11 in cpu_hand:
                cpu_hand[cpu_hand.index(11)] = 1
                cpu_score = sum(cpu_hand)
            if cpu_score > 21:
                print(f"Your final hand:{player_hand}, Your score: {player_score}")
                print(f"Computer's final hand: {cpu_hand}, Computer's score: {cpu_score}")
                print("Opponent went over, You Win")
                continue
        elif cpu_score == player_score:
            print(f"Your final hand:{player_hand}, Your score: {player_score}")
            print(f"Computer's final hand: {cpu_hand}, Computer's score: {cpu_score}")
            print("Draw")
            continue
        elif cpu_score == 21 or cpu_score > player_score:
            print(f"Your final hand:{player_hand}, Your score: {player_score}")
            print(f"Computer's final hand: {cpu_hand}, Computer's score: {cpu_score}")
            print("You Lose")
            continue
        else:
            if player_score < 21:
                print(f"Your final hand:{player_hand}, Your score: {player_score}")
                print(f"Computer's final hand: {cpu_hand}, Computer's score: {cpu_score}")
                print("You Win")
            continue






