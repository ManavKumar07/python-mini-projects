 #PROJECT 1  NUMBER GUESSING GAME

num = 25
for i in range(1, 100):
    guess = int(input("Enter your number you think of: "))
    if guess == num:
        print("Your guess is right")
        print("No. of attempts:", i)
        break
    elif guess > num:
        print("Choose some lower")
    else:
        print("Choose some higher")
