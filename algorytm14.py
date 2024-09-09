#Algorytm z użyciem join() i listy bitów
def decimal_to_binary(n):
    return ''.join(map(str, [(n >> i) & 1 for i in reversed(range(n.bit_length()))])) or '0'
    # Generujemy listę bitów przez przesunięcie bitowe i łączymy je w łańcuch

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
