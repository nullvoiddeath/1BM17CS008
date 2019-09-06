import random
import string
alpha = string.ascii_letters + string.digits + string.punctuation
l = int(input("Enter the length of password: "))
passw = []
for i in range(l):
	rand = random.randrange(0,len(alpha))
	print(rand)
	passw.append(alpha[rand])

r = ''.join(passw)
print('Generated random password is: ' + r)

