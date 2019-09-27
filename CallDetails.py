class CallDetail:
	def __init__(self,calls):
		self.call_details = calls
		self.show_details()
		
	def show_details(self):
		Details = self.call_details.split(',')
		Attr = ['From','To', 'Time', 'Type']
		print('\nCall details are: ')
		for i in range(0,4):
			print(Attr[i] + ':' + Details[i])
	
class Util:
	def __init__(self):
		self.CallList = None
		
	def parse_customers(self, objs):
		ObjList = []
		for i in objs:
			ObjList.append(CallDetail(i))
		CallList = ObjList

call = '1234567890,9963457812,23,STD'
call1 = '1234465464,1233453812,89,International'
call2 = '1234879797,1616317812,31,Local'

CList = [call, call1, call2]

Util().parse_customers(CList)
