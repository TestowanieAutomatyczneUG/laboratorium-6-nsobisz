
def roman(liczba):
    liczby_rzymskie = {"X": 10, "IX": 9, "V": 5,"IV": 4, "I" : 1 }
    wynik=""
    if liczba <= 39:
        while liczba != 0:
            for i in liczby_rzymskie:
                if liczba >= liczby_rzymskie[i]:
                    liczba = liczba - liczby_rzymskie[i]
                    wynik += i
                    break

    return wynik

