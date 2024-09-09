#Algorytm z użyciem deque (kolejki dwukierunkowej)
from collections import deque

def decimal_to_binary(n):
    binary = deque()  # Inicjalizacja deque, aby dodawać bity na początek
    while n > 0:
        binary.appendleft(str(n % 2))  # Dodawanie bitów na początek deque
        n = n // 2  # Dzielenie liczby przez 2
    return ''.join(binary) or '0'  # Konwersja deque na łańcuch znaków

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
