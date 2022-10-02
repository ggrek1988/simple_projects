def plansza_w(plansza1):
    # wyswietlenie tablicy
    print('     a  b  c')
    print('   ----------')
    print('1 |  ' + str(plansza1[0]) + '  ' + str(plansza1[1]) + '  ' + str(plansza1[2]))
    print('2 |  ' + str(plansza1[3]) + '  ' + str(plansza1[4]) + '  ' + str(plansza1[5]))
    print('3 |  ' + str(plansza1[6]) + '  ' + str(plansza1[7]) + '  ' + str(plansza1[8])+'\n\n')

def wynik(plansza2,gracz1):
    if gracz == 1:
        znacznik = 'X'
    if gracz == 2:
        znacznik = 'o'
    if plansza2[0] == znacznik and plansza2[1] == znacznik and plansza2[2] == znacznik:
        return 1
    if plansza2[3] == znacznik and plansza2[4] == znacznik and plansza2[5] == znacznik:
        return 1
    if plansza2[6] == znacznik and plansza2[7] == znacznik and plansza2[8] == znacznik:
        return 1
    if plansza2[0] == znacznik and plansza2[3] == znacznik and plansza2[6] == znacznik:
        return 1
    if plansza2[1] == znacznik and plansza2[4] == znacznik and plansza2[7] == znacznik:
        return 1
    if plansza2[2] == znacznik and plansza2[5] == znacznik and plansza2[8] == znacznik:
        return 1
    if plansza2[0] == znacznik and plansza2[4] == znacznik and plansza2[8] == znacznik:
        return 1
    if plansza2[6] == znacznik and plansza2[4] == znacznik and plansza2[3] == znacznik:
        return 1

def use_par(x):

    if str(plansza[x]) == '_':
        return 1

    elif str(plansza[x]) != '_':
        return 2


plansza = [('_'),('_'),('_'),('_'),('_'),('_'),('_'),('_'),('_')]
plansza_w(plansza)

a = 0
x = 0
gracz = 1
kolejka = [1]

while a != 1:
    b = 0



    while b != 1:
        if gracz == 1:
            parametr = input('podaj ruch dla gracza pierwszego:')
            znacznik_gracza = 'X'



        if gracz == 2:
            parametr = input('podaj ruch dla gracza drugiego:')
            znacznik_gracza = 'o'




        if parametr == 'a1':
            x = 0

            if use_par(x) == 1:
                b = 1
                continue
            if use_par(x) == 2:

                print ('wartosc zajeta')
                continue


        if parametr == 'a2':
            x = 3
            if use_par(x) == 1:
                b = 1
                continue
            if use_par(x) == 2:
                print ('wartosc zajeta')
                continue


        if parametr == 'a3':
            x = 6
            if use_par(x) == 1:
                b = 1
                continue
            if use_par(x) == 2:
                print ('wartosc zajeta')
                continue


        if parametr == 'b1':
            x = 1
            if use_par(x) == 1:
                b = 1
                continue
            if use_par(x) == 2:
                print ('wartosc zajeta')
                continue


        if parametr == 'b2':
            x = 4
            if use_par(x) == 1:
                b = 1
                continue
            if use_par(x) == 2:
                print ('wartosc zajeta')
                continue


        if parametr == 'b3':
            x = 7
            if use_par(x) == 1:
                b = 1
                continue
            if use_par(x) == 2:
                print ('wartosc zajeta')
                continue


        if parametr == 'c1':
            x = 2
            if use_par(x) == 1:
                b = 1
                continue
            if use_par(x) == 2:
                print ('wartosc zajeta')
                continue


        if parametr == 'c2':
            x = 5
            if use_par(x) == 1:
                b = 1
                continue
            if use_par(x) == 2:
                print ('wartosc zajeta')
                continue
        if parametr == 'c3':
            x = 8
            if use_par(x) == 1:
                b = 1
                continue
            if use_par(x) == 2:
                print ('wartosc zajeta')
                continue
        if (parametr != 'a1') or (parametr != 'a2') or parametr != 'a3' or parametr != 'b1' or parametr != 'b2' or parametr != 'b3' or parametr != 'c1' or parametr != 'c2' or parametr != 'c3':
            print ('nieprawidlowa wartosc')
            b = 0


    plansza[x] = znacznik_gracza
    #plansza.update(x,'X')
    if wynik(plansza,gracz) == 1:
        plansza_w(plansza)
        print('koniec gry')
        a = 1
    else:



        if plansza.count('X') > plansza.count('o'):
            gracz = 2
        if plansza.count('X') <= plansza.count('o'):
            gracz = 1


        plansza_w(plansza)