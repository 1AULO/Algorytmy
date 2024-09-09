#Algorytm z użyciem stosu (iteracyjny)
def decimal_to_binary(n):
    stack = []  # Inicjalizacja stosu do przechowywania bitów
    while n > 0:
        stack.append(n % 2)  # Dodawanie reszty z dzielenia przez 2 na stos
        n = n // 2  # Dzielenie liczby przez 2
    return ''.join(map(str, reversed(stack))) or '0'  # Odwracamy stos i konwertujemy go na łańcuch znaków

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
