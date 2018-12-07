from  selenium import  webdriver
from  PIL import  Image
import  time
import  random
from imooc_selenium.ShowapiRequest import  ShowapiRequest
from base.find_element import  FindElement
# import  sys
# sys.path.append('E:\\测试学习\\my_imooc_selenium>')
# sys.path.append('E:/测试学习/my_imooc_selenium>')

#----------2.22将整个注册流程脚本进行模块化---------------
class RegisterFuntion(object):
	#__init__ 方法即构造方法，会在类的对象被实例化时先运行，可以将初始化的操作放置到该方法中
	def __init__(self,url,i  ):
		self.driver = self.get_driver(url ,i )

	#----2.24多浏览器跑case---
	def get_driver(self,url ,i ):
		if  i == 1:
			diver = webdriver.Chrome()
		elif i ==2:
			diver = webdriver.Edge()
		else :
			diver = webdriver.Firefox()
		diver.get(url)
		diver.maximize_window()
		return  diver

	#输入用户信息
	def send_user_info(self,key,data):
		self.get_user_element(key).send_keys(data)

	#定位用户信息，获取element.(通过导入封装好的定位元素find_element包)
	def get_user_element(self,key):
		find_element = FindElement(self.driver)
		user_element = find_element.get_element(key)
		return  user_element

	# 获取随机数
	def get_random_user(self):
		user_info = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz', 8))
		return user_info

	# 获取图片
	def get_code_image(self,file_name):
		self.driver.save_screenshot(file_name)
		# code_element = driver.find_element_by_id('getcode_num')将原find_element.py中的直接获取元素id改成通过读取LocalElement.ini读取对应key获得
		code_element = self.get_user_element('code_image')
		left = code_element.location['x']  # 获取验证码图片坐标
		top = code_element.location['y']
		right = code_element.size['width'] + left
		height = code_element.size['height'] + top
		im = Image.open(file_name)  # 导进PIL包的方法，打开上面打开的照片
		img = im.crop((left, top, right, height))  # 裁剪获取验证码图片，对象
		img.save(file_name)

	# 解析图片获取验证码
	def code_online(self,file_name):
		self.get_code_image(file_name)
		r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "d61950be50dc4dbd9969f741b8e730f5")
		r.addBodyPara("typeId", "35")
		r.addBodyPara("convert_to_jpg", "0")
		r.addFilePara("image", file_name)  # 文件上传时设置
		res = r.post()
		# print(res.text)
		text = res.json()['showapi_res_body']['Result']
		return text

	#运行主程序
	def  main(self):
		user_name = self.get_random_user()
		user_email = user_name + '@163.com'
		file_name = 'E:/测试学习/my_imooc_selenium/image/imooc01.png'  # 定义图片保存路径
		code_text = self.code_online(file_name)
		self.send_user_info('user_email',user_email)#输入邮箱
		self.send_user_info('user_name', user_name)#输入用户名
		self.send_user_info('password', '111111')#输入密码
		self.send_user_info('code_text', code_text)#输入验证码
		self.get_user_element('register_button').click()#点击注册
		code_error = self.get_user_element('code_text_error')
		#通过是否有验证码错误提示来判断是否注册成功，如果失败则截图处理
		if code_error == None :
			print('注册成功！')
		else :
			print('注册失败！')
			self.driver.save_screenshot('E:/测试学习/my_imooc_selenium/image/codeerror.png')
		time.sleep(5)
		self.driver.close()

# 主程序入口
if __name__ == '__main__':
	for  i in range(3):
		register_function = RegisterFuntion('http://www.5itest.cn/register',i)
		register_function.main()