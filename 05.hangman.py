import random
from wordlist import words
import string

def get_valid_word(words):
    word=random.choice(words) #randomly chooses somthing from the list
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word

def hangman():
    word=get_valid_word(words)
    word_letters=set(word) # letters in the word #Using the set() constructor to make a set:
    alphabet=set(string.ascii_uppercase)
    used_letters=set() #What the user has guessed
    
    #Getting user input
    while len(word_letters) > 0:
        #Letters used
        # ' '.join(['a','b','cd]) --> 'a b cd'
        print("you have used these letters: ", ' '.join(used_letters))

        # what the current word is (ie W-R D)
        word_list = [letter if letter in used_letters else '_' for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter=input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in used_letters:
            print("you have already used that character. try again!")
            
        else:
            print("Invalid character. please try again!")

    #Gets here when len(word_letters) == 0

hangman()
