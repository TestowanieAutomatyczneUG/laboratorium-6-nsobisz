
def roman(liczba):
    liczby_rzymskie = {"L": 50,"XL": 40, "X": 10, "IX": 9, "V": 5,"IV": 4, "I" : 1 }
    wynik=""
    if liczba <= 89:
        while liczba != 0:
            for i in liczby_rzymskie:
                if liczba >= liczby_rzymskie[i]:
                    liczba = liczba - liczby_rzymskie[i]
                    wynik += i
                    break

    return wynik

