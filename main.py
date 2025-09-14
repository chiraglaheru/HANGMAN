# `task1- randomly choose a word from the word_list` is a comment indicating the purpose of the following code snippet in Python. The code snippet uses the `random` module to randomly select a word from the `word_list` list and then prints out the chosen word.
import random
word_list =["aadrvarj","babooon","camel"]
chosen_word =random.choice(word_list)
print(chosen_word)

# task 2 - ask user to guess a letter and assign their ans to var called guess 
guess = input("guess a letter:").lower()
print(guess)

# task - 4 check if letter is guessed corrc print"right else wrong
for letter in chosen_word:
    if letter == guess:
        print("right")
    else:
        print("wrong")
