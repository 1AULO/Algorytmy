def to_binary(n):
    if n == 0:
        return ""
    else:
        return to_binary(n // 2) + str(n % 2)

number = input()

try:
    number = int(number)
except ValueError:
    print("Podana wartość nie jest liczbą całkowitą.")
    exit()

if number == 0:
    binary_representation = "0"
else:
    binary_representation = to_binary(number)

print(f"{binary_representation}")