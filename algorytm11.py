#Algorytm z użyciem ciągu znaków (rekurencyjny)
def decimal_to_binary(n):
    return decimal_to_binary(n // 2) + str(n % 2) if n > 1 else str(n)  # Jeśli n > 1, rekurencyjnie obliczamy bity, w przeciwnym razie zwracamy n

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
