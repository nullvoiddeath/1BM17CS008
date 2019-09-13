f = open('rev.txt', 'w')
x = raw_input('Enter string: ')
f.write(x)
f.close
f = open('rev.txt', 'r')
f.seek(0,2)
str = ''
size = f.tell()
for i in range(0, size+1):
	f.seek(-i, 2)
	str += f.read(1)
print('Reading from bottom of file: ' + str)
