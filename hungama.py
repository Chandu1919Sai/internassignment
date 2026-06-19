import random

HANGMAN_STAGES = ["""
   -----       -----       -----
   |   |       |   |       |   |
       |       O   |       O   |
       |           |       |   |
       |           |      /|   |
       |           |           |
=========   =========   =========
""",
]  # 7 stages total (0 wrong → 6 wrong)

WORDS = ["python", "hangman", "coding", "laptop", "rocket"]

def display_word(word, guessed):
    return " ".join(l if l in guessed else "_" for l in word)

def play_hangman():
    word = random.choice(WORDS)
    guessed = set()
    wrong = 0

    while wrong < 6:
        print(f"\n  Word : {display_word(word, guessed)}")
        print(f"  Wrong guesses left : {6 - wrong}")

        if all(l in guessed for l in word):
            print(f"  You WIN! The word was: '{word}'")
            return

        guess = input("  Guess a letter: ").strip().lower()
        if len(guess) != 1 or not guess.isalpha():
            print("  Enter a single letter."); continue
        if guess in guessed:
            print("  Already guessed!"); continue

        guessed.add(guess)
        if guess in word:
            print(f"  '{guess}' is in the word!")
        else:
            wrong += 1
            print(f"  '{guess}' is NOT in the word!")

    print(f"  Game Over! The word was: '{word}'")

if __name__ == "__main__":
    play_hangman()
