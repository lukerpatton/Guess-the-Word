# Part 1
# Step 1 - Secret Word Variable
secret_word = ""
guess_count = 1

# Step 2 - Retrieve User's Guess
def get_guess():
    
    while True: 

        guess = input("What is your guess?")
        
        if len(guess) == 1 and guess.islower():
            return guess
        else:
            print("Your guess must be exactly one lowercase letter.")

# START
guess = get_guess()
print("Your guess was: " + guess)
