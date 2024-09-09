#Algorytm iteracyjny z konwersją na listę
def decimal_to_binary(n):
    binary = []  # Inicjalizacja listy na bity
    while n > 0:
        binary.append(str(n % 2))  # Dodawanie reszty z dzielenia przez 2 do listy
        n = n // 2  # Dzielenie liczby przez 2
    return ''.join(binary[::-1]) or '0'  # Odwracamy listę i konwertujemy na łańcuch znaków

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
