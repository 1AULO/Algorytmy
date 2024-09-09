#Algorytm z użyciem generatora
def decimal_to_binary(n):
    return ''.join(str((n >> i) & 1) for i in reversed(range(n.bit_length()))) or '0'
    # Używamy generatora do iteracyjnego tworzenia bitów i łączenia ich w łańcuch

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
