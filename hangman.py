import random

# Wir importieren die Datei namens HangmanWords.py und nennen sie als ,,Wörter"
import hangmanWords as words

# wichtige Variabeln
chosenWord = random.choice(words.wordList)
wordLength = len(chosenWord)
gameOver = False
lives = 6
display = []


#Leerstellen erstellen
for _ in chosenWord: 
    display += "_"



print("* * * Willkommen beim Hangman-Python-Spiel! * * *\n")
print("Es gibt ein geheimes Wort, das das Programm zufällig aus der Datei HangmanWords ausgewählt und")
print("die Buchstaben versteckt hat.\n")
print("Sie müssen einen zufälligen Buchstaben eingeben, um das Wort zu finden.")
print(f"Sie haben natürlich {lives} Leben, und jedes Mal, wenn Sie einen Buchstaben finden")
print("es wird automatisch der unten gezeigten Anzeige hinzugefügt\n")
print("Jedes Mal, wenn Sie eine Buchstabe nicht finden, verlieren Sie jedoch ein Leben")
print("Also viel Glück!\n")
print(f"{display}\n")


#Code testen
print(f"Psst, das Wort ist {chosenWord}")


while game_over != True:
        guess = input("Bitte erraten Sie einen Buchstaben: ").lower()
                
        if guess in display:
            print("\nbereits ausgewählt, versuchen Sie es erneut")
        
        for position in range(wordLength):
            letter = chosenWord[position]
            if letter == guess:
                display[position] = letter
                
        #überprüfen, ob der Benutzer falsch liegt
        if guess not in chosenWord:
            lives -= 1
            if lives == 0:
                print("Aus dem Leben. du hast verloren")
                game_over = True
        
        #verbinde alle Elemente in der Liste und verwandle sie in einen String.
        print(f"{' '.join(display)}")
    
        #überprüfen, ob der Benutzer alle Buchstaben hat.
        if "_" not in display:
            print("Herzlichen Glückwunsch! Du hast gewonnen")
            game_over = True