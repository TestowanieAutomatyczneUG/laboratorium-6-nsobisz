
def roman(liczba):
    liczby_rzymskie = {"I" : 1 }
    wynik=""
    if liczba <= 3:
        while liczba != 0:
            for i in liczby_rzymskie:
                if liczba >= liczby_rzymskie[i]:
                    liczba = liczba - liczby_rzymskie[i]
                    wynik += i

    return wynik
