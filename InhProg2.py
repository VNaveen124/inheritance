#InhProg2.py
class Company:
	def   getcompdet(self):
		self.cname="Wipro"
		self.loc="HYD"
class Food:
	def getfooddet(self):
		self.avfood="Biryani"
		self.drink="apple juice"

class Employee ( Company, Food ) :
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
		print("Today Food details")
		print("------------------------------------------------")
		print("Food in Company : {}".format(self.avfood))
		print("drink in Company : {}".format(self.drink))
		print("------------------------------------------------")

#main program
eo=Employee()
eo.getempdet()
eo.getcompdet()
eo.getfooddet()
eo.dispempdet()
