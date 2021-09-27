import random
number_visa = random.randint(1000000000000000, 9999999999999999)
print(number_visa, number_visa % 10 ** 4, sep=';')