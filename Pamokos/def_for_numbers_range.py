#arašykite programą, kuri atspausdina visus skaičius nuo 1 iki 1000, kurie dalijasi iš 6.
numbers = list(range(1, 1000))
def number_mani(numbers):
    return [number for number in numbers if number % 6 == 0]
print(number_mani(numbers))