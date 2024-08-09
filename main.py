import random

words = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_len = int(input("Ingrese la cantidad de caracteres para la contraseña:"))

password = ""

for i in range(password_len):
    password += random.choice(words)

print(password)
