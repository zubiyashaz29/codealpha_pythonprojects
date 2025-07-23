import random

# List of words to choose from
words = ['apple', 'banana', 'grape', 'mango', 'peach']
word_to_guess = random.choice(words)

# Create a list to show the progress
progress = ['_'] * len(word_to_guess)
attempts = 6
guessed_letters = []

print("Welcome to Hangman!")
print("You have", attempts, "chances to guess the word.\n")

while attempts > 0 and '_' in progress:
    print("Current word:", ' '.join(progress))
    print("Guessed letters:", ', '.join(guessed_letters))
    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter. Try something else.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Good job! Letter is in the word.\n")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                progress[i] = guess
    else:
        attempts -= 1
        print("Wrong guess! You have", attempts, "chances left.\n")

# Game end
if '_' not in progress:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Game over! The correct word was:", word_to_guess)
