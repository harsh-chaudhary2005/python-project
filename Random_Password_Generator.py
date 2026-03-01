import random
import string
from itertools import cycle

def generate_password(length=12):
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation


    base = random.choice(letters) + random.choice(digits) + random.choice(symbols)
    
    all_char = letters + digits + symbols
    rest = ''.join(random.choice(all_char) for _ in range(length - len(base)))


    password = list(base + rest)
    random.shuffle(password)

    return ''.join(password)

for i in range(1):
    print(generate_password(12))