#Algorytm dzielenia przez 2 (rekurencyjny)
def decimal_to_binary(n):
    if n == 0:
        return ''  # Podstawa rekursji: jeśli n jest 0, zwracamy pusty łańcuch
    else:
        return decimal_to_binary(n // 2) + str(n % 2)  # Rekurencyjne obliczanie bitów

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number) or '0'}")
