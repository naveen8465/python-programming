win_num = 63
guess = 1
game_over= False
num=int(input("enter a number between 0 and 100:"))

while not game_over:
    if num == win_num:
        print("You win!")
        print(f"you guessed this win num in {guess} times")
        game_over = True
    elif num < win_num:
        print("Too low!")
        guess +=1
        num = int(input("Enter a number between 0 and 100: "))
    else:  # This handles the case where num > win_num
        print("Too high!")
        guess +=1
        num = int(input("Enter a number between 0 and 100: "))

while True:
    if num == win_num:
        print("you win!")
        print(f"you guessed this win num in {guess} times")
        break
    else:
        if num < win_num:
            print("too low")
            guess +=1
        else:
            print("too high")
            guess +=1
            num = int(input("Enter a number between 0 and 100: "))
            




