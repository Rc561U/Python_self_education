import re
from string import ascii_lowercase, ascii_uppercase, digits
import random


CREATE_EMAIL = ascii_uppercase + ascii_lowercase + '_-.'


num = random.choice(range(4,20))
em = ''
for i in range(num):
	em += random.choice(CREATE_EMAIL)

print(em)