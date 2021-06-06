#InhProg5.py
class  Univ:
	def getunivdet(self):
		self.uname=input("Enter Univ Name:")
		self.uloc=input("Enter Univ Location:")
	def dispunivdet(self):
		print("-----------------------------------------------")
		print("University Details:")
		print("-----------------------------------------------")
		print("University Name:{}".format(self.uname))
		print("University Location:{}".format(self.uloc))
		print("-----------------------------------------------")

class College(Univ):
	def  getColldet(self):
		self.cname=input("Enter College Name:")
		self.cloc=input("Enter College Location:")
		so.getunivdet();
	def dispcolldet(self):
		so.dispunivdet()
		print("College Details:")
		print("-----------------------------------------------")
		print("College Name:{}".format(self.cname))
		print("College Location:{}".format(self.cloc))
		print("-----------------------------------------------")

class Student(College):
	def  getstuddet(self):
		self.sno=int(input("Enter Student Number:"))
		self.sname=input("Enter Student Name:")
		self.crs=input("Enter Student Course:")
		so.getColldet()

	def  dispstuddet(self):
		so.dispcolldet()
		print("Studet Details:")
		print("-----------------------------------------------")
		print("Student Number:{}".format(self.sno))
		print("Student Name:{}".format(self.sname))
		print("Student Course:{}".format(self.crs))
		print("-----------------------------------------------")
		

#main program
so=Student()
so.getstuddet()
so.dispstuddet()
