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
root.config(bg=BLACK)
root.title("Wordle")



###main
def clear_text():
   userWordInput.delete(0, END)

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

                for letter in enumerate(list(guess)):

                    label = Label(root, text=letter[1].upper())

                    label.grid(row=attempts, column=letter[0], padx=15, pady=15)

                    if letter[1] == word_chosen[letter[0]]: #in word, right position
                        
                        label.config(bg=GREEN, fg=BLACK)

                    if letter[1] in word_chosen and not letter[1] == word_chosen[letter[0]]: #in word, wrong position

                        label.config(bg=YELLOW, fg=BLACK)
                    
                    if letter[1] not in word_chosen: #not in word

                        label.config(bg=BLACK, fg="#e1e8f2")

                
                messagebox.showinfo("Correct!", f"The word was indeed {word_chosen}")

            else:

                for letter in enumerate(list(guess)):

                    label = Label(root, text=letter[1].upper())

                    label.grid(row=attempts, column=letter[0], padx=15, pady=15)

                    if letter[1] == word_chosen[letter[0]]: #in word, right position
                        
                        label.config(bg=GREEN, fg=BLACK)

                    if letter[1] in word_chosen and not letter[1] == word_chosen[letter[0]]: #in word, wrong position

                        label.config(bg=YELLOW, fg=BLACK)
                    
                    if letter[1] not in word_chosen: #not in word

                        label.config(bg=BLACK, fg="#e1e8f2")


        if len(guess) != 5:

            messagebox.showerror("Error!", "Please use a 5 letter word for your guesses!")

    else:

        messagebox.showerror("Uh Oh!", f"You ran out of attempts! The word was {word_chosen}")


wordGuessButton = Button(root, text="ENTER", command=lambda:[getGuess, clear_text])
wordGuessButton.grid(row=999, column=3, columnspan=2)


root.mainloop()







