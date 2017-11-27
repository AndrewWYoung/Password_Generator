import random
import string

def generate_random_password():
    password = []
    for char in range(1, 15):
        random_number = random.randint(33, 126)
        password.append(chr(random_number))
    return "".join(password)

print(generate_random_password())
print(string.ascii_letters)
