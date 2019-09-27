class CollegeAdm:
	def __init__(self):
		self.sid = None
		self.age = None
		self.marks = None
	
	def getData(self):
		print('Enter student data-> ')
		sid = input('Student ID: ')
		age = int(input('Age: '))
		marks = int(input('Marks: '))
		self.setData(sid, age, marks)
	
	def setData(self, sid, age, marks):
		self.sid = sid
		self.age = age
		self.marks = marks
		if self.check_qualifications():
			print('Student is eligible!\n')
		else:
			print('Student is not eligible!\n')
	
	def validate_marks(self):
		if(self.marks >= 0 and self.marks <= 100):
			return True
		return False

	def validate_age(self):
		if(self.age > 20):
			return True
		return False
	
	def check_qualifications(self):
		if(self.validate_marks() and self.validate_age()):
			if self.marks > 65:	
				return True
			return False
		return False

n = int(input('Enter number of students: '))
ObjList = []

for i in range (0,n):
	ObjList.append(CollegeAdm())
for i in ObjList:
	i.getData()
