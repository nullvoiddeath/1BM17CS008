class Check:
	def __init__(self, paraList):
		self.charList = paraList
		self.stack = []
		self.openList = ['(','[','{']
		self.closeList = [')',']','}']
	def checkValidity(self):
		for i in self.charList:
			if i in self.openList:
				self.stack.append(i)
			elif i in self.closeList:
				pos = self.closeList.index(i)
				if len(self.stack) > 0	and self.openList[pos] == self.stack[len(self.stack)-1]:
					self.stack.pop()
				else:
					return 'Unbalanced'
			if len(self.stack) == 0:
				return 'Balanced'

newList = []
size = int(input('Enter number of characters: '))
print('Enter characters: ')
for i in range(0,size):
	newList.append(input())
newObj = Check(newList)
res = newObj.checkValidity()
print('Result is: ' + res)
