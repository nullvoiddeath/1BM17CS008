li = []
even_li = []
n = int(input("Number of elements: "))
print("Enter the elements: ")
for i in range(n):
	li.append(int(input()))
	if li[i] % 2 == 0:
		even_li.append(li[i])

print("List with only even elements: ")

for x in even_li:
	print(x)
