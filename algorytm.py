#Algorytm z użyciem str.zfill() (dodawanie zer na początku)
def decimal_to_binary(n):
    return bin(n)[2:].zfill(n.bit_length()) or '0'
# Używamy zfill() do uzupełnienia zerami na początku, jeśli jest to konieczne

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
