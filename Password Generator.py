# ____PASSWORD GENERATOR_____

import random
import string
i=int(input('Enter the no. of characters you want = '))
a=(string.ascii_letters)
d=(string.digits)
p=(string.punctuation)
all= a+p+d
my_random=random.sample(all,i)
print(''.join(my_random))
