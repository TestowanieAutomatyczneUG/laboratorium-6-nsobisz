
def roman(liczba):
    liczby_rzymskie = {"IX": 9, "V": 5,"IV": 4, "I" : 1 }
    wynik=""
    if liczba <= 9:
        while liczba != 0:
            for i in liczby_rzymskie:
                if liczba >= liczby_rzymskie[i]:
                    liczba = liczba - liczby_rzymskie[i]
                    wynik += i

    return wynik
