'''Body Mass Index Problem'''
'''Input of Weight and Height from the user'''
import abc
class Bmi(metaclass=abc.ABCMeta):
	@abc.abstractmethod
	def calculation(self):
		pass
	@abc.abstractmethod
	def prediction(self):
		pass

class BodyMassIndex(Bmi):
	def __init__(self):
		self.members_weight=list(map(int,input("Enter Weights of members :\n").split()))
		self.members_height=list(map(int,input("Enter Heights of members :\n").split()))
		self.unit=int(input("'1' : Kilograms,Centimeters\n'2' : Kilograms,Metres)\n'3' : Pounds,Inches\nUNIT : "))

	'''BMI Calculation part'''

	def calculation(self):
		if(len(self.members_weight)!=len(self.members_height)):
			print("Insufficient Data.\n")
			return
		else:
			self.members_bmi=[]
			for i in range(len(self.members_weight)):
				if(self.unit==1):
					self.members_bmi.append((self.members_weight[i]/self.members_height[i]/self.members_height[i])*10000)
				elif(self.unit==2):
					self.members_bmi.append(self.members_weight[i]/(self.members_height[i])**2)
				elif(self.unit==3):
					self.members_bmi.append((self.members_weight[i]/(self.members_height[i])**2)*703)
				else:
					print("Invalid Unit.")

	'''Health Prediction'''
	def prediction(self):
		print("Leading Healthy Life is more important to have a Healthy Heart so maintain a Healthy Life.\n")
		for i in range(len(self.members_bmi)):
			print("Member{} Body Mass Index is : {} kg/m^2".format(i+1,self.members_bmi[i]))
			if self.members_bmi[i]<18.5:
				print("Member{} is UNDERWEIGHT, should consult a nutrition doctor.\n".format(i+1))
			elif self.members_bmi[i]>=18.5 and self.members_bmi[i]<=24.9:
				print("Member{} is NORMAL and HEALTHY.\n".format(i+1))
			elif self.members_bmi[i]>24.9 and self.members_bmi[i]<30:
				print("Oh god! Member{} is OVERWEIGHT, should have some diet plan introduced.\n".format(i+1))
			else:
				print("Member{} is OBESE, should consult a nutrition doctor.\n".format(i+1))

class Main():
	obj=BodyMassIndex()
	obj.calculation()
	obj.prediction()
