import random

def read_words(filename):
    with open(filename, 'r') as file:
        words = [word.strip() for word in file]
    return words

def select_random_word(words):
    return random.choice(words)

def display_word(word, guessed_letters):
    display = []
    for letter in word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append('_')
    return ' '.join(display)

def play_hangman():
    words = read_words('dictionary.txt')
    word = select_random_word(words)

    guessed_letters = set()
    incorrect_guesses = 0

    while incorrect_guesses <= 5:
        print(display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You have already guessed this letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            if all(letter in guessed_letters for letter in word):
                print("Congratulations! You won!")
                print(f"The word was: {word}")
                break
        else:
            incorrect_guesses += 1
            print(f"Incorrect guess. You have {5 - incorrect_guesses} incorrect guesses left.")

            if incorrect_guesses > 5:
                print("Sorry, you lost.")
                print(f"The word was: {word}")

if __name__ == "__main__":
    play_hangman()
