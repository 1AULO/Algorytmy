#Metoda formatująca format()
def decimal_to_binary(n):
    return format(n, 'b')  # Funkcja format() z parametrem 'b' konwertuje liczbę na binarną reprezentację

number = int(input("Podaj liczbę dziesiętną: "))
print(f"Reprezentacja binarna liczby {number} to: {decimal_to_binary(number)}")
