def ankieta():
    print("Ankieta na twoj temat :)")
    try:
        wzrost = float(input("Wzrost [cm] : "))
    except ValueError:
        print("Wzrost powinien być podany jako liczba :(")
        exit()
    kolor_oczu = input("Kolor oczu: ")
    kolor_wlosow = input("Kolor wlosow: ")
    print("Dziekujemy za udzial <3")


