#Algorytm iteracyjny z użyciem pętli for
def decimal_to_binary(n):
    binary = ''  # Inicjalizacja pustego łańcucha na binarną reprezentację
    for i in range(n.bit_length()):  # Iterujemy przez wszystkie bity liczby
        binary = str(n >> i & 1) + binary  # Dodajemy bit na początek łańcucha
    return binary or '0'  # Zwracamy '0', jeśli n było równe 0

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
