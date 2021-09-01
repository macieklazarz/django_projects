import pandas as pd
import random
from tkinter import *

# ked down function
def click():
    b2.config(state=NORMAL)
    b1.config(state=DISABLED)
    odpowiedz = textentry.get()
    if odpowiedz == answers[random_question_number]:                                    # sprawdzamy czy odpowiedz jest zgodna z tym co mamy w slowniku answers z odpowiedziami
        question_try[random_question_number] = question_try[random_question_number] - 1 #jesli odpowiedz jest poprawna to zmniejszamy o 1 liczbe prob w macierzy question_try z liczba pozostalych prob dla kazdego pytania
        if question_try[random_question_number] == 0:
            question_try.pop(random_question_number)                                    #jesli liczba prob to 0 to wyrzucamy pytanie z macierzy question_try z liczba pozostalych prob dla kazdego pytania
            question_numbers.remove(random_question_number)                             #jesli liczba prob to 0 to wyrzucamy pytanie ze slownika question_numbers przechowywujacego numery pytan z posrod ktorych odbywa sie losowanie
        # print('Prawidlowa odpowiedz')
        wynik.delete(0.0, END)
        wynik.insert(END, "Prawidlowa odpowiedz")
    else:
        # print('Zla odpowiedz')
        wynik.delete(0.0, END)
        wynik.insert(END, "Zla odpowiedz")

def next_question():
    pytanie.delete(0.0, END)
    wynik.delete(0.0, END)
    b1.config(state=NORMAL)
    b2.config(state=DISABLED)
    # textentry.delete(0.0, END)

    global random_question_number
    random_question_number = random.choice(question_numbers)
    pytanie.insert(END, questions[random_question_number])



window = Tk()
window.title("my title")
window.configure(background="black")

# label pytanie
Label (window, text="Pytanie to", bg="black", fg="white", font="none 12 bold") .grid(row=1, column=0, sticky=W)
# text box na pytanie
pytanie = Text(window, width=75, height=6, wrap=WORD, background="white")
pytanie.grid(row=2, column=0, columnspan=2, sticky=W)

# label odpowiedz
Label (window, text="\nOdpowiedz:", bg="black", fg="white", font="none 12 bold") .grid(row=3, column=0, sticky=W)

#  entry box na odpowiedz
textentry = Entry(window, width=20, bg="white")
textentry.grid(row=4, column=0, sticky=W)
# Button submit
b1 = Button(window, text="SUBMIT", width=6, command=click)
b1.grid(row=5, column=0, sticky=W)
b1.config(state=DISABLED)

# Button next question
b2 = Button(window, text="Next question", width=12, command=next_question)
b2.grid(row=5, column=3, sticky=W)

# label wynik
Label (window, text="\nWynik:", bg="black", fg="white", font="none 12 bold") .grid(row=6, column=0, sticky=W)

# text box na wynik
wynik = Text(window, width=75, height=6, wrap=WORD, background="white")
wynik.grid(row=7, column=0, columnspan=2, sticky=W)



# # dicttionary
# dict = {'niebieski':'blue', 'czarny':'black', 'zielony':'green'}


excel_content = pd.read_excel('data.xlsx') #czytam dane z pliku data.xls do zmiennej excel_content
df = pd.DataFrame(excel_content)            #zmieniam zawartość excel_content na dataframe w zmiennej df

q = df['question'].tolist()                 #tworze liste w zmiennej q w ktorej mam to co w kolumnie questions w pliku xlsx
questions = {}                              #tworze slownik o nazwie questions
question_numbers = []                       #w macierzy question_numbers będę przechowywał nymery pytan
question_try = {}                           #w tym slowniku przechowuje numer pytania i liczbe prob jakie pozostaly do zaliczenia pytania
for i, row in enumerate(q):
    questions[i] = row                      #wrzucam rekordy do slownika questions - SLOWNIK BEDZIE WYGLADAL TAK: {1:"pytanie 1", 2:pytanie 2" ...}
    question_numbers.append(i)              #wrzucam numery pytan do macierzy
    question_try[i] = 1                     #w tym slowniku przechowuje numer pytania i liczbe prob jakie pozostaly do zaliczenia pytania

a = df['answer'].tolist()
answers = {}#tworze liste w zmiennej a w ktorej mam to co w kolumnie questions w pliku xlsx
for i, row in enumerate(a):
    answers[i] = row                        #wrzucam rekordy do slownika - SLOWNIK BEDZIE WYGLADAL TAK: {1:"odpowiedz 1", 2:odpowiedz 2" ...}

window.mainloop()




