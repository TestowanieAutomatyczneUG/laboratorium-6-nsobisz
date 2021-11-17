
def roman(liczba):
    liczby_rzymskie = {"CD": 400,"C": 100,"XC": 90, "L": 50,"XL": 40, "X": 10, "IX": 9, "V": 5,"IV": 4, "I" : 1 }
    wynik=""
    if liczba <= 499:
        while liczba != 0:
            for i in liczby_rzymskie:
                if liczba >= liczby_rzymskie[i]:
                    liczba = liczba - liczby_rzymskie[i]
                    wynik += i
                    break

    return wynik

