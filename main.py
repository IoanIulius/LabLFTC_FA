import json

import FA
def print_menu():
    print("###Hello")
    print("0. Exit")
    print("1. Read finite automaton")


def get_file_input():

    file = "C:\\Users\\Johnny\\PycharmProjects\\Lab4_FA\\date.txt"
    with open(file) as f:
        return json.load(f)


def select_read_option(option):
    if option != "1" and option != "2":
        print("Invalid option")
        return

    print("1. File")
    print("2. Std input")
    read_option = input()
    if read_option != "1" and read_option != "2":
        print("Invalid option")
        return

    if read_option == "1":
        main_input = get_file_input()
    else:
        main_input = json.load(input())

    if option == "1":
        process_finite_automaton(main_input)


def print_fa_menu():
    print("0. Back")
    print("1. Print States")
    print("2. Print Alphabet")
    print("3. Print Transitions")
    print("4. Print Final States")
    print("5. Convert to Finite Automaton")


def process_finite_automaton(json):
    fa = FA.FiniteAutomaton(json)
    while True:
        print_fa_menu()
        option = input()
        if option == "0":
            break
        elif option == "1":
            print(fa.get_states())
        elif option == "2":
            print(fa.get_alphabet())
        elif option == "3":
            print(fa.get_transitions())
        elif option == "4":
            print(fa.get_final_states())
        elif option == "5":
            print(fa.convert())
        else:
            print("Invalid option")


if __name__ == '__main__':
    while True:
        print_menu()
        option = input()
        if option == "0":
            break
        try:
            select_read_option(option)
        except Exception as e:
            print(e)
            print("Something went wrong, please try again")