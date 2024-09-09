#Algorytm dzielenia przez 2 (iteracyjny)
def decimal_to_binary(n):
    binary = ''  # Inicjalizacja pustego łańcucha na binarną reprezentację
    while n > 0:
        binary = str(n % 2) + binary  # Dodawanie reszty z dzielenia przez 2 na początek łańcucha
        n = n // 2  # Dzielenie liczby przez 2, aby kontynuować obliczanie kolejnych bitów
    return binary or '0'  # Zwracamy '0', jeśli n było równe 0

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
