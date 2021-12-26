import random
print('''Hello!
    You are in the game, guess the random number from 1 to 10.
    You have only 3 attempts.''')

ran_number = random.randint(1,10)
user_attempts = 0


while user_attempts <= 3:

    user_choose_ran_num = int(input("Select a number:  "))


    if user_choose_ran_num < ran_number:
        print("Random number is bigger")
        user_attempts += 1

    if user_choose_ran_num > ran_number:
        print("Random number is smaller")
        user_attempts += 1

    if user_choose_ran_num == ran_number:
        user_attempts -= user_attempts
        print(f"You are guessed a {ran_number} - random number, in {user_attempts} attempts.")
        user_choose = int(input("\n1 - play again., 2 - quit:  "))
        if user_choose == 1:
            continue
        elif user_choose == 2:
            break

    if user_attempts == 3:
        user_attempts -= user_attempts
        print(f"You lose ,{ran_number} - random number")
        user_choose = int(input("\n1 - play again., 2 - quit:  "))
        if user_choose == 1:
            continue
        elif user_choose == 2:
            break


