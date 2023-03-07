#Maciej Łatosz s24435 12c
import Calc
import Ankieta

choice = input("1 -> calc   2 -> ankieta:  ")
if choice == "1":
    Calc.calc()
elif choice == "2":
    Ankieta.ankieta()
else:
    print (" :( zly wybor")
