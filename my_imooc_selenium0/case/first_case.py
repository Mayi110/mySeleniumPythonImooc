from  business.register_business import  RegisterBusiness
from  selenium import  webdriver

class FirstCase(object):
	def __init__(self):
		driver = webdriver.Firefox()
		driver.get('http://www.5itest.cn/register')
		self.login = RegisterBusiness(driver)

	def  test_login_email_error(self):
		email_error = self.login.login_email_error('11' , 'user111' , '111111' , 'qwe1')
		if  email_error == True :
			print('注册成功了，此条case执行失败')
		#通过assert判断是否为error


	def test_login_username_error(self):
		username_error = self.login.login_name_error('123@163.com','dd','2222222','wed3')
		if  username_error == True :
			print('注册成功了，此条case执行失败')

	def  test_login_password_error(self):
		password_error = self.login.login_name_error('123@163.com', 'd444d', '2222222', 'wed3')
		if password_error == True :
			print('注册成功了，此条case执行失败')


	def  test_login_code_error(self):
		code_error = self.login.login_name_error('123@163.com', 'dd', '2222222', 'wed3')
		if  code_error == True :
			print('注册成功了，此条case执行失败')

	def  test_login_success(self):
		self.login.user_base('123@163.com', 'dd', '2222222', 'wed3')
		if  self.login.register_success() == True :
			print('注册成功了')


if __name__ == '__main__':
	first = FirstCase()
	first.test_login_email_error()
	first.test_login_username_error()
	first.test_login_password_error()
	first.test_login_code_error()
	first.test_login_success()




