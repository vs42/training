hidden = 13123

guess = int(input())

while guess != hidden:
    if guess > hidden:
        print("Too high")
    elif guess < hidden:
        print("Too low")
    guess = int(input())
