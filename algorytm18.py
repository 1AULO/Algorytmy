#Algorytm z użyciem XOR i AND
def decimal_to_binary(n):
    binary = ''  # Inicjalizacja pustego łańcucha na binarną reprezentację
    while n:
        binary = ('1' if n & 1 else '0') + binary  # Sprawdzamy najmniej znaczący bit z AND i dodajemy odpowiedni znak
        n >>= 1  # Przesunięcie bitów w prawo (dzielenie przez 2)
    return binary or '0'  # Zwracamy '0', jeśli n było równe 0

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
