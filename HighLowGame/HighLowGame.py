import random
from game_data import data

from art import logo
from art import vs

import os

def assign():
    return(random.choice(data))

def compare(p1,p2,user_input):
    sum1=p1['follower_count']
    sum2=p2['follower_count']

    max=''
    if sum1>sum2:
        max=p1['name']
    elif sum1<sum2:
        max=p2['name']
    
    if max==user_input:
        return True
    else:
        return False

def play_higher_lower():
    playing_game =True
    while playing_game:
        score = 0
        still_guessing=True
        while still_guessing:
            os.system('clear')
            print(logo)

            person1=assign()
            person2=assign()

            if score >0:
                person1 = person2
                person2 = assign()
                if person1==person2:
                    person2=assign()
            
            print(f"Name:{person1['name']},Desc:{person1['description']}")

            print(vs)

            print(f"Name:{person2['name']},Desc:{person2['description']}")

            print(f"Your current score is:{score}")

            guess =input("Guess name of person with higher follower:")

            if compare(person1,person2,guess):
                score +=1
            else:
                still_guessing=False
        play_again=input("Play again?(Y/N):").lower()

        if play_again=='y':
            continue
        elif play_again=='n':
            playing_game=False
            os.system('clear')
            print("Game End.")
        else:
            playing_game=False
            print("Invalid Input")
play_higher_lower()