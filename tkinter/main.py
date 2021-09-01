from tkinter import *
# ked down function
def click():
    entered_text=textentry.get()
    print(entered_text)
    output.delete(0.0, END)
    try:
        definition = dict[entered_text]
    except:
        definition = "sorry, no word like this"
    output.insert(END, definition)


#main
window = Tk()
window.title("my title")
window.configure(background="black")

# photo
photo1 = PhotoImage(file="python.png")
Label (window, image=photo1, bg="black") .grid(row=0, column=0, sticky=W)

# create label
Label (window, text="Enter the word you would like a definition for:", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
# text entry box
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=2, column=0, sticky=W)
# Button
Button(window, text="SUBMIT", width=6, command=click) .grid(row=3, column=0, sticky=W)

#create another label
Label (window, text="\nDefinition:", bg="black", fg="white", font="none 12 bold") .grid(row=4, column=0, sticky=W)

#create a text box
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, columnspan=2, sticky=W)

# dicttionary
dict = {'niebieski':'blue', 'czarny':'black', 'zielony':'green'}

window.mainloop()