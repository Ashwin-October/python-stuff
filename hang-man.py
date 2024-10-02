import random
wordlist = ["python", "interpreted", "dunder", "pytorch", "anaconda", "docstring"]
word = random.choice(wordlist)
attempts = 1
guess = []
correct = ""
print(f"A Word has been selected. You have {attempts} Attempts!")
while attempts < 6:
    x = input(f"Attempt {attempts}: ").lower()
    if correct != word:
        if x in word and x not in guess:
            attempts += 1
            guess.append(x)
            correct = "".join(j if j in guess else "_" for j in word)
            print(f"CORRECT! {correct}")
        elif x in guess: 
            print(f"Letter: {x} is already guessed!")
        else: 
            attempts += 1
            print(f"WRONG! {correct}")

if correct == word: print("Congratulations! You got the Word right!")
else: print("Sorry! You didn't make it!")