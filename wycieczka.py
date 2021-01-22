question = ["Napisz wiadomość:", "Skarga na panią Jagódkę bo robi fikołki pokoju recepcjonistek"]
person_list={"1":"Kacper Gazda"}
number_question={"Jagódka Wacławczyk" : "789654231"}
problem_dic={int : str}
days_dic={"1": "Wyjazd z Polski o 4:00. ", "2": "Śniadanie w Macedoni.\nPrzyjazd do Grecji w godzinach: 14-16", "3": "Zwiedzenie góry Olimp oraz saloników"}

print("Wycieczka do Grecji\n")

password_check = "123"
login_check = "user"
choice_start = -1
choice = -1
choice_dp = -1
choice_log = "-1"

def sendmessage():
    question.append(input("Napisz swoje pytanie:\n\n"))

def login_start():
    a = login_check
    b = password_check
    if a == input("Wpisz login: ") and b == input("Wpisz hasło: "):
        print("Zostałeś zalogowany!")
    else:
        print("Niepoprawne dane... Wybierz opcję:")
        print("1. Spróbuj ponownie")
        print("2. Wyjdź")
        choice_log = int(input("Wybór: "))
        if choice_log == 1:
            login_start()
        elif choice_log == 2:
            key_exit()
        else:
            bad_choice()


def bad_choice():
    print("--------------------")
    print("Niepoprawna wartość!")
    key_continue

def first_choice():
    print("Wybierz kim jesteś: \n")
    print("1. Uczestnik")
    print("2. Opiekun")
    print("3. Wyjście")

def key_continue():
    input("Kontynuuj... [Enter]")

def key_back():
    input("Powrót... [Enter]")

def key_exit():
    print("\nŻegnaj !")
    quit()

def addDay():
    input("Dodaj dzień:\n")

if choice_start:
    first_choice()
    try:
        choice_start = int(input("Podaj odpowiedni numer: "))
        print()
    except ValueError:
        bad_choice()
    
    if choice_start == 1:
        while choice:
            print("Wybierz jedną z opcji:\n")
            print("1. Pokaż plan wycieczki")
            print("2. Pokaż uczestników wycieczki")
            print("3. Pokaż numer do opiekunów")
            print("4. Masz problem? Zgłoś go nam")
            print("5. Wyjście")
            
            try:
                choice = int(input("Podaj odpowiedni numer: "))
                print()
            except ValueError:
                bad_choice()
            
            if choice == 1:
                print("Wycieczka składa się z: 7dni")
                for days , plan in days_dic.items():
                    print("-----------\n" + days + "\n" + plan)
                key_continue()
            elif choice == 2:
                print("Uczestnicy wycieczki:\n")
                print(person_list)
                key_continue()
            elif choice == 3:
                print("Numer do opiekunów:\n")
                print(number_question)
                key_continue()
            elif choice == 4:
                print("Zgłoś problem:\n")
                sendmessage()
                key_continue()
            elif choice == 5:
                key_exit()
            else:
                print("\nZły wybór\n")
                continue
            
    elif choice_start == 2:
        login_start()
        print("Nie działa")
        while choice:
            print("Wybierz jedną z opcji:\n")
            print("1. Pokaż plan wycieczki")
            print("2. Modyfikuj plan wycieczki")
            print("3. Pokaż uczestników")
            print("4. Modyfikuj uczestników")
            print("5. Pokaż numer do opiekuna")
            print("6. Modyfikuj numer do opiekuna")
            print("7. Przeczytaj wiadomości")
            print("8. Wyjście")
            
            try:
                choice = int(input("Podaj odpowiedni numer: "))
                print()
            except ValueError:
                bad_choice()
            
            if choice == 1:
                print("Wycieczka składa się z: 7dni")
                for days , plan in days_dic.items():
                    print("-----------\n" + days + "\n" + plan)
                key_continue()
            elif choice == 2:
                days_dic[input("Podaj dzień:\n")]= input("Podaj plan dnia:\n")
                key_continue()
            elif choice == 3:
                print("Uczestnicy wycieczki:\n")
                for number , name in person_list.items():
                    print("---" + number + "--- " + name)
                key_continue()
            elif choice == 4:
                print(" ")
                print("1. Dodaj uczestnika")
                print("2. Usuń uczestnika")
                print("3. Zaktualizuj uczestnika")
                
                try:
                    choice_dp = int(input("\nPodaj odpowiednią liczbę: "))
                    print()
                except ValueError:
                    bad_choice()

                if choice_dp == 1:
                    person_list[input("Podaj numer uczestnika: ")]= input("Podaj imię i nazwisko uczestnika: ")
                elif choice_dp == 2:
                    person_list.pop(input("Wpisz numer uczestnika: "))
                else:
                    print("Niepoprawna treść")
                key_continue()
            elif choice == 5:
                for name , number in number_question.items():
                    print("---" + name + "--- " + number)
                key_continue()
            elif choice == 6:
                print("1. Dodaj numer")
                print("2. Usuń numer")
                print("3. Zaktualizuj numer")
                
                try:
                    choice_dp = int(input("\nPodaj odpowiednią liczbę: "))
                    print()
                except ValueError:
                    bad_choice()

                if choice_dp == 1:
                    number_question[input("Podaj nazwę opiekuna: ")]= input("Podaj numer opiekuna: ")
                elif choice_dp == 2:
                    number_question.pop(input("Wpisz nazwę opiekuna: "))
                elif choice_dp == 3:
                    number_question[input("Podaj nazwę opiekuna: ")]= input("Podaj nowy numer opiekuna: ")
                else:
                    print("Nieprawidłowa wartość")
            elif choice == 7:
                print("Przeczytaj wiadomości:\n")
                for val in question:
                    print("---" + val + "---")
                print()
                key_continue()
            elif choice == 8:
                key_exit()
            else:
                print("\nNiepoprawna wartość\n")
                continue
    elif choice_start == 3:
        key_exit()
