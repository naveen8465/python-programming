#conditional statements= if, else, if else, elif if else, nested if

#

#name = "kalyani"
#age = 22

# number guessing game

win_num = 42

guess_num=int(input("enter a guess num:"))

if win_num == guess_num:
    print(" you win")
else:
    if guess_num < win_num:
        print("too low")
    else:
        print("too high")
