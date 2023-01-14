import random
import hangmanWords as words

chosenWord = random.choice(words.wordList)
wordLength = len(chosenWord)
gameOver = False
lives = 6
display = []


for _ in chosenWord: 
    display += "_"


print(f"""
      * * * Welcome to the Hangman Python game! * * *\n"
      There is a secret word that the program chooses randomly from the HangmanWords file and has hidden the letters.
      You must enter a random letter to find the word.
      You have {lives} lives, of course, and every time you find a letter it is automatically added to the meter shown below.
      However, every time you miss a letter you lose a life.
      Good Luck!
      {display}\n
      """)

print(f"Psst, the word is {chosenWord}")


while gameOver != True:
    
        if "_" not in display:
            print("Congratulations! You won\n")
            gameOver = True
    
        guess = input("Please guess a letter: ").lower()
        
        if guess in display:
            print("\nalready selected, try again\n")
        
        for position in range(wordLength):
            letter = chosenWord[position]
            if letter == guess:
                display[position] = letter
                
                
        if guess not in chosenWord:
            lives -= 1
            print(f"\nyou have {lives} lives left\n")
            if lives == 0:
                print("\nOut of lives. You lost!\n")
                gameOver = True
        
        print(f"{' '.join(display)}")
    
