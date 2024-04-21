import random

# create a greeting
print("Welcome to Chat-box")
# create your word list

words = ["hacker", "hunter", "bounty", "carlos" "random"]
# randomly choose a word from the list you have created
secret_word = random.choice(words)
print("You get 6 guesses")
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)

# ask the user to guess a letter
num = 0
# bonus make the program take the input from the user and make it a lowercase
gameOver = False
# check if the letter is in the word
while not gameOver:
    guess = input("Guess a letter ").lower()
    for position in range(len(secret_word)):
        letter = secret_word[position]
        if letter == guess:
            display_word[position] = letter
    if guess not in secret_word:
        num += 1
        guesses_left = 6 - num
        print(f"You have {guesses_left} guesses left")
        if num >= 6:
            print("You lose")
            gameOver = True
    print(display_word)

    if "_" not in display_word:
        print("You win")
        gameOver = True
