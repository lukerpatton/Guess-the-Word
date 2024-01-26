import random

# Secret Word Variables
guess_count = 1
guesses_left = 10
win = False

# Step 1 - Make a List
words = ["hello", "python", "code", "yoyo", "seven", "lakes", "band",
    "marimba", "flute", "banana", "computer", "library", "beach", 
    "apple", "candy", "music", "flower", "mouse", "radio", "smile", 
    "zebra", "oboe", "drum", "snare", "tuba", "cube", "island", 
    "exam", "test", "quiz", "minor", "major", "other", "panda",
    "queen", "piano", "unicorn"]
    
# Step 2 - Pick From the List
secret_word = random.choice(words)


# Variable For Dashes
dashes = "-" * len(secret_word)

# Retrieve User's Guess
def get_guess():
    
    while True: 

        print(dashes)
        guess = input("What is your guess? ")
        
        if len(guess) == 1 and guess.islower():
            return guess
        else:
            print("Your guess must be exactly one lowercase letter.")
            
            
# Update the Dashes
def update_dashes(secret_word, dashes, guess):
    updated_dashes = ""
    for i in range(len(secret_word)):
        if guess == secret_word[i]:
            updated_dashes += guess
        else:
            updated_dashes += dashes[i]
            
    return updated_dashes

# START
while guesses_left > 0 and not win: 
    guess = get_guess()
    print("Your guess was:", guess)
    
    if guess in secret_word:
        print("Congratulations! Your guess is in the secret word.")
        
        # Put It All Together
        dashes = update_dashes(secret_word, dashes, guess)
        
    else:
        print("Sorry, your guess is not in the secret word.")
        # Tracking guesses
        guesses_left = guesses_left - 1
    
    # Letting the User Win
    if '-' not in dashes:
    	win = True

# Win or lose
if (win):
	print("Congrats! You won! The word was:", secret_word)
else:
	print("You lose. The word was: ", secret_word)
