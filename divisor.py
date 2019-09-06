def divisor(n):
	div = []
	for i in range(1, n//2):
		if n%i == 0:
			div.append(i)
	div.append(n)
	return div

num = int(input("Enter the number: "))
r = divisor(num)
print("Divisors are: ")
for i in r:
	print(i) 
