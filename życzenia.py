__author__ = 'Asia'

print("Dzisiaj jest Dzień Chłopaka. Siontko chce Ci coś przekazać.")


def get_user_choice():
    print("Wpisz 1, 2 lub 3:")
    choice = get_usr_input()
    return choice


def get_usr_input():
    tmp = input()
    if represents_int(tmp):
        return int(tmp)
    else:
        print("Źle!")
        return get_usr_input()


def represents_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


def odpowiedzi(choice):
    if choice == 1:
        print("Siontko jest Twoją kizią mizią.")
    elif choice == 2:
        print("Siontko może być nawet Twoim pudelkiem.")
    elif choice == 3:
        print("Siontko bardzo Cię kocha.")


def main_program():
    odpowiedzi(get_user_choice())
    user_answer = input("A Ty kochasz jeszcze Siontko? Odpowiedz: Tak!/Nie!")
    if user_answer == "Tak!":
        print("Siontko Ciebie też.")
        main_program()
    else:
        print("Foch.")
        exit()

main_program()