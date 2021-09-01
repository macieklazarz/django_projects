import pandas as pd
import random



excel_content = pd.read_excel('data.xlsx')  #czytam dane z pliku data.xls do zmiennej excel_content
df = pd.DataFrame(excel_content)            #zmieniam zawartość excel_content na dataframe w zmiennej df

q = df['question'].tolist()                 #tworze liste w zmiennej q w ktorej mam to co w kolumnie questions w pliku xlsx
questions = {}                              #tworze slownik o nazwie questions
question_numbers = []                       #w macierzy question_numbers będę przechowywał nymery pytan
question_try = {}                           #w tym slowniku przechowuje numer pytania i liczbe prob jakie pozostaly do zaliczenia pytania
for i, row in enumerate(q):
    questions[i] = row                      #wrzucam rekordy do slownika questions - SLOWNIK BEDZIE WYGLADAL TAK: {1:"pytanie 1", 2:pytanie 2" ...}
    question_numbers.append(i)              #wrzucam numery pytan do macierzy
    question_try[i] = 1                     #w tym slowniku przechowuje numer pytania i liczbe prob jakie pozostaly do zaliczenia pytania

a = df['answer'].tolist()                   #tworze liste w zmiennej a w ktorej mam to co w kolumnie questions w pliku xlsx
answers = {}                                #tworze slownik o nazwie questions
for i, row in enumerate(a):
    answers[i] = row                        #wrzucam rekordy do slownika - SLOWNIK BEDZIE WYGLADAL TAK: {1:"odpowiedz 1", 2:odpowiedz 2" ...}

# print(question_try)
# print(type(question_try[3]))
# print(questions)
# print(answers)
# print(question_numbers)


while(question_numbers):                    # program bedzie wykonywal sie w petli dopoki w macierzy question_numbers przechowywujacej numery pytan beda dane
    random_question_number = random.choice(question_numbers)    #losuje numer pytania z macierzy z numerami pytan o nazwie question_numbers uzupelnianej w linijce 16
    # print(random_question_number)

    odpowiedz = input(f"Pytanie to: {questions[random_question_number]}\n") #wypisujemy pytanie w konsoli i przypisujemy odpowiedz do zmiennej odpowiedz
    print(f'Podana odpowiedz to: {odpowiedz} \n')

    if odpowiedz == answers[random_question_number]:                                    # sprawdzamy czy odpowiedz jest zgodna z tym co mamy w slowniku answers z odpowiedziami
        question_try[random_question_number] = question_try[random_question_number] - 1 #jesli odpowiedz jest poprawna to zmniejszamy o 1 liczbe prob w macierzy question_try z liczba pozostalych prob dla kazdego pytania
        if question_try[random_question_number] == 0:
            question_try.pop(random_question_number)                                    #jesli liczba prob to 0 to wyrzucamy pytanie z macierzy question_try z liczba pozostalych prob dla kazdego pytania
            question_numbers.remove(random_question_number)                             #jesli liczba prob to 0 to wyrzucamy pytanie ze slownika question_numbers przechowywujacego numery pytan z posrod ktorych odbywa sie losowanie
        print('Prawidlowa odpowiedz')
    else:
        print('Zla odpowiedz')


    # print(f'pozostalo prob: {question_try}')
    # print(question_numbers)