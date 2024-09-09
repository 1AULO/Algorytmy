#Algorytm z użyciem metody bit_length()
def decimal_to_binary(n):
    return ''.join(str((n >> i) & 1) for i in reversed(range(n.bit_length()))) or '0'
    # Korzystamy z bit_length(), aby określić liczbę bitów potrzebnych do reprezentacji liczby

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
