#InhProg1.py
class Company:
	def   getcompdet(self):
		self.cname="Wipro"
		self.loc="HYD"

class Employee ( Company ) :
	def  getempdet(self):
		self.eno=100
		self.ename="Rosum"
		self.sal=23.45
		self.dsg="author"
	def dispempdet(self):
		print("------------------------------------------------")
		print("Employee Details")
		print("------------------------------------------------")
		print("Empoyee Number: {}".format(self.eno))
		print("Empoyee Name: {}".format(self.ename))
		print("Empoyee Salary: {}".format(self.sal))
		print("Empoyee Designation: {}".format(self.dsg))
		print("Company Name: {}".format(self.cname))
		print("Company Location: {}".format(self.loc))
		print("------------------------------------------------")

#main program
eo=Employee()
eo.getempdet()
eo.getcompdet()
eo.dispempdet()
