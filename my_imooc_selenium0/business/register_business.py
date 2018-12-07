from  handle.register_handle import  RegisterHandle

#执行操作（业务层。case与handle之间的中介）
class  RegisterBusiness(object):
	def __init__(self,driver):
		self.register_h = RegisterHandle(driver)   #register_h是局部的，改成self.register_h就变成全局的？self的作用是什么

	def user_base(self,email,name,password,code):
		self.register_h.send_user_email(email)  # 后面的用户名、密码和验证码其实不用输完，只要邮箱失去焦点就能验证了
		self.register_h.send_user_name(name)
		self.register_h.send_user_password(password)
		self.register_h.send_user_code(code)
		self.register_h.click_register_button()

	def  register_success(self):
		if  self.register_h.get_register_text() == None :
			return  True
		else :
			return  False

	#email错误
	def  login_email_error(self,email,name,password,code):
		self.user_base(email,name,password,code)
		if  self.register_h.get_user_text('email_error',"请输入有效的电子邮件地址") :
			print('邮箱检验不成功')
			return  True
		else  :
			return  False

	#name错误
	def login_name_error(self,email,name,password,code):
		self.user_base(email,name,password,code)
		if self.register_h.get_user_text('name_error', "字符长度必须大于等于4，一个中文字算2个字符"):
			print('用户名检验不成功')
			return True
		else:
			return False

	#密码错误
	def login_password_error(self,email,name,password,code):
		self.user_base(email,name,password,code)
		if self.register_h.get_user_text('password_error', "字符长度必须大于等于4，一个中文字算2个字符"):
			print('密码检验不成功')
			return True
		else:
			return False

	#验证码错误
	def login_code_error(self,email,name,password,code):
		self.user_base(email,name,password,code)
		if self.register_h.get_user_text('code_error', "字符长度必须大于等于4，一个中文字算2个字符"):
			print('验证码检验不成功')
			return True
		else:
			return False





