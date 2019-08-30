def lin_srch(A, n):
	for i in A:
		if i == n:
			return True

	return False

A = []
num = int(input("Enter number of elements: "))
print("Enter the elements: ")
for i in range(num):
	A.append(int(input()))
k = int(input("Enter key: "))
print(lin_srch(A, k))
