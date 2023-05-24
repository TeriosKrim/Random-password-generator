import random
import string

def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

uppercaseLetter1 = random.choice(string.ascii_uppercase)
uppercaseLetter2 = random.choice(string.ascii_uppercase)
lowercaseLetter1 = random.choice(string.ascii_lowercase)
lowercaseLetter2 = random.choice(string.ascii_lowercase)
digit1 = random.choice(string.digits)
digit2 = random.choice(string.digits)
punctuationsign1 = random.choice(string.punctuation)
punctuationsign2 = random.choice(string.punctuation)

password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 + digit1 + digit2 + punctuationsign1 + punctuationsign2
password = shuffle(password)

print(password)
