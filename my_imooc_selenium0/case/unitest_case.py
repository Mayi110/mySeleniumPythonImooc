import  unittest

class Firstcase01(unittest.TestCase) :
	def  setUp(self):
		print('这是case的前置条件')

	def  tearDown(self):
		print('这是case的后置条件')

	#注意：用例case必须以‘test'开头,否则默认情况下在控制台不会打印
	def  testfirst01(self):
		print('这是第一条case')
	def  testfirst02(self):
		print('这是第二条case')


if  __name__  ==  '__main__':
	unittest.main()