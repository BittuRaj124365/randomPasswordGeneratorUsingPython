# we will use random modult to generate random numbers

import random
import string

passLength=10
charValue=string.ascii_letters+string.digits+string.punctuation

password=""
for i in range(passLength):
    password+=random.choice(charValue)
print("Your password is:",password)