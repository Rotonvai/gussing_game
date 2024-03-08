from random import randint

while True:
    guessing_number = int(input("Enter your guess between 1 to 5: "))
    random_number = randint(1, 5)

    if guessing_number == random_number:
        print("You have won!")
        print("Random number was", random_number)
    else:
        print("You have lost.")
        print("Random number was", random_number)