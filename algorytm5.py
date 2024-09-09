#Algorytm bit-shifting (iteracyjny)
def decimal_to_binary(n):
    binary = ''  # Inicjalizacja pustego łańcucha na binarną reprezentację
    while n > 0:
        binary = str(n & 1) + binary  # & 1 sprawdza najmniej znaczący bit liczby
        n = n >> 1  # Przesunięcie bitów liczby w prawo (dzielenie przez 2)
    return binary or '0'  # Zwracamy '0', jeśli n było równe 0

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
