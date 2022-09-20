from random import choice
import string


t = ''.join(choice(string.ascii_letters + string.digits) for _ in range(15))

print(t)