from selenium import  webdriver
from selenium.webdriver.support import  expected_conditions as  EC
import  time
from  selenium.webdriver.support.wait import  WebDriverWait
from selenium.webdriver.common.by import  By
import  random
from  PIL import  Image
from imooc_selenium.ShowapiRequest import  ShowapiRequest

driver = webdriver.Firefox()
driver.get('http://www.5itest.cn/register')
time.sleep(10)
#通过title_contains判断页面时否正常打开，检查标题是否包含‘注册’
print(EC.title_contains('注册'))
email_element = driver.find_element_by_id('register_email')

# -------2-13如何解决验证码:-------
# 1、保存整页截图
# 2、计算验证码图片位置坐标
# 3、下载并导入PIL库，使用Image方法打开已保存的截图
# 4、裁剪验证码图片
# 5、转化验证码图片的文字
# 6、输入验证码
driver.save_screenshot('E:/测试学习/《selenium3+python3自动化测试实战》/imooc.png') #保存整页页截图
code_element = driver.find_element_by_id('getcode_num')
print(code_element.location) #{"x":"123","y":"345"}
left = code_element.location['x']  #获取验证码图片坐标
top = code_element.location['y']
right = code_element.size['width'] + left
height = code_element.size['height'] + top
im = Image.open('E:/测试学习/《selenium3+python3自动化测试实战》/imooc.png') #导进PIL包的方法，打开上面打开的照片
img = im.crop((left,top,right,height)) #裁剪获取验证码图片，对象
img.save('E:/测试学习/《selenium3+python3自动化测试实战》/imooc1.png')

#-------读取验证码-------
r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", 'E:/测试学习/《selenium3+python3自动化测试实战》/imooc1.png') #文件上传时设置
res = r.post()
time.sleep(1)
#print(res.text)
# 打印结果{"showapi_res_error":"","showapi_res_id":"06d165386e6a4ccd99f0d54c86278fd0","showapi_res_code":0,"showapi_res_body":{"Id":"26ad0b26-6b18-4c9f-a5e3-673c18a68f02","Result":"FLMVN","ret_code":0}}
#json获取最终结果
text = res.json()['showapi_res_body']['Result']
print(text)  #返回信息
time.sleep(2)
#输入验证码
driver.find_element_by_id('captcha_code').send_keys(text)
time.sleep(5)


#------2-11如何生成用户名-------
for i in range(5):
	# user_email = random.sample('1234567890abcdefg',5) #从字符串1234567890abcdefg中任意选取5个作为用户邮箱,这样会打印list类型
	user_email = ' '.join(random.sample('1234567890abcdefg',5))+'@163.com'
	print(user_email)

element = driver.find_element_by_class_name('controls')
locator = (By.CLASS_NAME,'controls')
#2-8判断传入的元素是否在页面可见
#EC.visibility_of_element_located(element)
#智能等待，以免未加载完成元素导致找不到本有的元素。传入定位值，在规定时间内找元素，如果找到就往下运行，找不到就返回false
WebDriverWait(driver,10).until(EC.visibility_of_element_located(locator))

# 判断元素是否在再dom元素里面
#EC.presence_of_element_located()

# 2-10获取注册用户名字及获取用户信息
print(email_element.get_attribute('placeholder')) #获取并打印属性信息
email_element.send_keys('test@163.com')
print(email_element.get_attribute('value')) #获取元素的value值，获取账户打印





driver.close()