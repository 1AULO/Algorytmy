#Algorytm z użyciem listy reduce i lambda
from functools import reduce

def decimal_to_binary(n):
    return reduce(lambda x, y: str(x) + str(y), reversed([n >> i & 1 for i in range(n.bit_length())]), '') or '0'
    # Używamy reduce, aby zredukować listę bitów do pojedynczego łańcucha znaków

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
