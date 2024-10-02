import random

wordlist = ["python", "interpreted", "dunder", "pytorch", "anaconda", "docstring"]
word = random.choice(wordlist)
attempts = 1
max_attempts = 6
guess = []
correct = ""

print(f"A word has been selected. You have {max_attempts} attempts!")

while attempts <= max_attempts:
    x = input(f"Attempt {attempts}: ").lower()

    if correct == word:
        break

    if x in guess:
        print(f"Letter '{x}' is already guessed!")
        continue

    guess.append(x)

    if x in word:
        correct = "".join(j if j in guess else "_" for j in word)
        print(f"CORRECT! {correct}")
    else:
        print(f"WRONG! {correct}")
        attempts += 1

if correct == word:
    print("Congratulations! You got the word right!")
else:
    print(f"Sorry! You've used all attempts. The word was '{word}'")