#Algorytm z użyciem f-stringów
def decimal_to_binary(n):
    return f"{n:b}"  # Używamy formatu f-string do konwersji liczby na binarną reprezentację

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
