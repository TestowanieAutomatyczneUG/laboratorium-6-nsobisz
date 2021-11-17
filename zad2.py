
def roman(liczba):
    liczby_rzymskie = {"IV": 4, "I" : 1 }
    wynik=""
    if liczba <= 4:
        while liczba != 0:
            for i in liczby_rzymskie:
                if liczba >= liczby_rzymskie[i]:
                    liczba = liczba - liczby_rzymskie[i]
                    wynik += i

    return wynik
