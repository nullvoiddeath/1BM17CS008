li = []
n =int(input("Enter the number of elements: "))
print("Enter the elements in sorted order: ")
for i in range(n):
	li.append(int(input()))
key = int(input("Enter the key: "))
beg = 0;
end = len(li)
mid = (beg+end)//2
while beg < end:
	if li[mid] == key:
		print("Element found at position: " + str(mid+1))
		exit()
	elif key < li[mid]:
		end = mid - 1
	else:
		beg = mid + 1
	mid=(beg+end)//2
print("Element not found!")
