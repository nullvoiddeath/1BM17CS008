def rev_string(A):
	w = A.split(' ')
	word = ' '.join(w[::-1])
	print("Words reversed: " + word)	
	print("Characters reversed: " + word[::-1])
	print("Characeters and words reversed: " + A[::-1])
	



string1 = input("Enter the string to reversed: ")
rev_string(string1)

