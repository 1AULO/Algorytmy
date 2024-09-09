#Algorytm z użyciem stosu (rekurencyjny)
def decimal_to_binary(n, stack=[]):
    if n == 0 and not stack:
        return '0'  # Jeśli n jest 0 i stos jest pusty, zwracamy '0'
    if n == 0:
        return ''.join(map(str, reversed(stack)))  # Jeśli n jest 0, odwracamy stos i zwracamy wynik
    stack.append(n % 2)  # Dodawanie reszty z dzielenia przez 2 na stos
    return decimal_to_binary(n // 2, stack)  # Rekurencyjne dzielenie przez 2

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
