secret_number = 33

print("Try and guess the secret number!")
number_guess = int(input())

if number_guess == secret_number:
    print("You Win!")
elif number_guess == secret_number + 1 or number_guess == secret_number - 1:
    print("So close!")
else:
    print("Try again!")