
from wordselection import word_bank
from tkinter import *
from tkinter import messagebox
import random


###Variables for GUI/game
word_chosen = random.choice(word_bank)
GREEN = "#1c8c31"
YELLOW = "#dbd221"
BLACK = "#0a0a00"
attempts = 1


###GUI setup
root = Tk()




###main
userWordInput = Entry(root)
userWordInput.grid(row=999, column=0, columnspan=3, padx=15, pady=15)

def getGuess():

    global word_chosen
    global attempts
    attempts += 1
    guess = userWordInput.get()

    if attempts <= 5:

        if len(guess) == 5:

            if guess == word_chosen:

                messagebox.showinfo("Correct!", f"The word was indeed {word_chosen}")

            else:

                for letter in guess:

                    label = Label(root, text=letter.upper())
                    label.grid(row=attempts, column=guess.index(letter), padx=10, pady=10)
                
                    if letter == word_chosen[guess.index(letter)]: #in word, right position
                        
                        label.config(bg=GREEN, fg=BLACK)

                    if letter in word_chosen and not letter == word_chosen[guess.index(letter)]: #in word, wrong position

                        label.config(bg=YELLOW, fg=BLACK)
                    
                    if letter not in word_chosen: #not in word

                        label.config(bg=BLACK, fg="#e1e8f2")


        if len(guess) != 5:

            messagebox.showerror("Error!", "Please use a 5 letter word for your guesses!")

    else:

        messagebox.showerror("Uh Oh!", f"You ran out of attempts! The word was {word_chosen}")


wordGuessButton = Button(root, text="ENTER", command=getGuess)
wordGuessButton.grid(row=999, column=3, columnspan=2)
















root.mainloop()







