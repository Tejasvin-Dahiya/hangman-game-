from replit import clear
#Code for The hangman game
import random
#importing the list of words for the game
import hangman_words
word_list=hangman_words.word_list

 
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
#setting up a condition for the ending of the game 
end_of_game = False
lives = 6 #6 lives are given to the user


import hangman_art
logo=hangman_art.logo
print(logo)
#creating the blanks 
display = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()


    if guess in display:
      print("You have already guessed this word")
      
   
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:

        lives -= 1
        print(f"{guess} is not in the chosen word")
        if lives == 0:
            end_of_game = True
            print("You lose.")
            print(f"The word was {chosen_word}")

    
    print(f"{' '.join(display)}")


    if "_" not in display:
        end_of_game = True
        print("You win.")

  
    stages=hangman_art.stages
    print(stages[lives])