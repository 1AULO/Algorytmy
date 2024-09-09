#Algorytm oparty na sumowaniu bitów
def decimal_to_binary(n):
    return ''.join(str((n >> i) & 1) for i in reversed(range(n.bit_length()))) or '0'
    # Sumujemy wartości bitów przez przesunięcie i sprawdzenie każdego bitu

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
