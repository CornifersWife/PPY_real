def calc():
    choice = input("operation + - * / : ")
    no1 = float(input("first number: "))
    no2 = float(input("second number: "))

    if choice == '+':
        print(no1 + no2)
    elif choice == '-':
        print(no1 - no2)
    elif choice == '*':
        print(no1 * no2)
    elif choice == '/':
        print(no1 / no2)
    else:
        print(" :( ")
