import random

event1 = "We pick out two cards from a standard deck of 52 cards without replacement. Event A is that we pick an Ace on the first draw. Event B is that we pick an Ace on the second draw."

event2 = "Suppose we flip a coin ten times. Event A is that we flip all heads on the first five flips. Event B is that we flip all heads on the second five flips."

event3 = "We roll a die once. Event A is rolling an odd number. Event B is rolling a number greater than four."

event4 = "We have a bag of five marbles: three are green and two are blue. Suppose that we pick one marble from the bag. Event A is that the marble is green. Event B is that the marble is blue."

event_lst = [event1, event2, event3, event4]


def guess_the_type(event):

    print(
        "Guess whether this is a \n 1)dependent \n 2)independent \n 3)mutually exclusive \n 4)not mutually exclusive event \n"
    )
    print(event)
    answer = int(input("Enter your answer : "))
    if event == event1:
        if answer == 1:
            print("You guessed it right")
        else:
            print("Your answer is wrong")

    if event == event2:
        if answer == 2:
            print("You guessed it right")
        else:
            print("Your answer is wrong")

    if event == event3:
        if answer == 4:
            print("You guessed it right")
        else:
            print("Your answer is wrong")

    if event == event4:
        if answer == 3:
            print("You guessed it right")
        else:
            print("Your answer is wrong")


for i in event_lst:
    guess_the_type(i)