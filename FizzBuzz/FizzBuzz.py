class FizzBuxx:
	def get(self, numbers):
		values = []
		for i in range(len(numbers)):
			values.append(self.check(numbers[i]))
		return values
	def check(self, number):
		if (number % 15 == 0) :
			return 'fizz buzz'
		elif (number % 3 == 0) :
			return 'fizz'
		elif (number % 5 == 0) :
			return 'buzz'

		return number


fz = FizzBuxx()

print(fz.get([1,2,3,4,5,6,7,15,30]))

