import random

length = 12
password_char = "abcdefghijklmnopqrstuvwxyz0123456789"
password = " "
for i in range(length):
    password += random.choice(password_char)

print("Random Password is -->",password)