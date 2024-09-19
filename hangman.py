import random

def hangman():
    words = ['python', 'java', 'kotlin', 'javascript', 'hangman']
    word = random.choice(words)
    guessed_word = ['_'] * len(word)
    attempts = 6
    guessed_letters = set()

    print("Welcome to Hangman!")
    
    while attempts > 0:
        print("\nWord: " + ' '.join(guessed_word))
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single alphabetic character.")
            continue
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Correct!")
            for idx, char in enumerate(word):
                if char == guess:
                    guessed_word[idx] = guess
        else:
            print("Wrong guess.")
            attempts -= 1
        
        if '_' not in guessed_word:
            print("\nCongratulations! You've guessed the word:", word)
            break
    else:
        print("\nYou've run out of attempts! The word was:", word)

hangman()
