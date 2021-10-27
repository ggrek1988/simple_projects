
rzymskie = ("M", "CM", "D", "CD", "C","XC", "L", "XL", "X", "IX", "V", "IV", "I")
cyfry1 = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)


parametr = int(raw_input('podaj liczbe do przekonwertowania:'))

suma = -1
wyjscie = ''
for x in cyfry1:
    suma = suma + 1
    while int(parametr) >= int(cyfry1[suma]):

        wyjscie += rzymskie[suma]
        parametr -= int(cyfry1[suma])

print wyjscie