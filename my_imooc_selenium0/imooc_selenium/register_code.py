from  selenium import  webdriver
import  time
import  random
from  PIL import  Image
from imooc_selenium.ShowapiRequest import  ShowapiRequest

# ---------2.17注册流程梳理及封装----------
driver = webdriver.Firefox()
#浏览器初始化
def  driver_init_():
	driver.get('http://www.5itest.cn/register')
	driver.maximize_window()
	time.sleep(5)

# 获取element信息
def  get_element(id ):
	element = driver.find_element_by_id(id )
	return  element

#获取随机数
def  get_random_user():
	user_info = ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz', 8))
	return  user_info

# 获取图片
def  get_code_image(file_name):
	driver.save_screenshot(file_name)
	code_element = driver.find_element_by_id('getcode_num')
	left = code_element.location['x']  # 获取验证码图片坐标
	top = code_element.location['y']
	right = code_element.size['width'] + left
	height = code_element.size['height'] + top
	im = Image.open(file_name)  # 导进PIL包的方法，打开上面打开的照片
	img = im.crop((left, top, right, height))  # 裁剪获取验证码图片，对象
	img.save(file_name)

# 解析图片获取验证码
def  code_online(file_name):
	r = ShowapiRequest("http://route.showapi.com/184-4", "62626", "d61950be50dc4dbd9969f741b8e730f5")
	r.addBodyPara("typeId", "35")
	r.addBodyPara("convert_to_jpg", "0")
	r.addFilePara("image", file_name)  # 文件上传时设置
	res = r.post()
	# print(res.text)
	text = res.json()['showapi_res_body']['Result']
	return  text

# -运行主程序-
def  run_main():
	user_name = get_random_user()
	user_email = get_random_user() + '@163.com'
	file_name = 'E:/测试学习/《selenium3+python3自动化测试实战》/imooc03.png'  #定义图片保存路径
	driver_init_()   #初始化浏览器
	get_element('register_email').send_keys(user_email)   #输入邮箱
	get_element('register_nickname').send_keys(user_name)   #输入用户名
	get_element('register_password').send_keys('111111')			#输入密码
	get_code_image(file_name)  #获取截图
	text = code_online(file_name)   #解析验证码
	get_element('captcha_code').send_keys(text)    #输入验证码
	get_element('register-btn').click()   #点击注册
	driver.close()

run_main()
