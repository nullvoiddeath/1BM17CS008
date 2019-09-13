import math
f1 = open('file1.txt', 'w')
f2 = open('file2.txt', 'w')
f3 = open('file3.txt', 'w')
s1 = input('Enter the first string: ')
f1.write(s1)
f1.close()
s2 = input('Enter the second string: ')
f2.write(s2)
f2.close()
f1 = open('file1.txt', 'r')
f2 = open('file2.txt', 'r')
f1r = f1.read()
f2r = f2.read()
print('\nContents of first file: ' + f1r)
print('Contents of second file: ' + f2r)
f1_words = f1r.split(' ')
f2_words = f2r.split(' ')
f3_words = []
len1 = len(f1_words)
len2 = len(f2_words)
if len1 > len2:
	big = len1
else:
	big = len2

for i in range(0 , big):
	half1 = ''
	half2 = ''
	if i < len1:
		half1 = half1 + f1_words[i][0:math.ceil(len(f1_words[i])/2)]
	if i < len2:
		half2 = half2 + f2_words[i][0:math.ceil(len(f2_words[i])/2)]
	f3_words.append(half1 + half2)

f3_words = ' '.join(f3_words)
f3.write(f3_words)
f3 = open('file3.txt', 'r')
print("\nContents of third final: " + f3.read())

