from  util.read_ini import  ReadIni

#---------2.11设计封装定位元素类----------
# 注意：.ini节点中的文本不要添加空格，否则会在定位元素时无法定位返回None
# 通过调用ReadIni来封装元素定位，并进行简单的容错处理
class FindElement(object) :
	def __init__(self,driver):
		self.driver = driver
	def get_element(self,key):
		read_ini = ReadIni()
		data = read_ini.get_vslue(key)
		#由于data得到的值为id > register_nickname，所以通过下面的定位方式by和定位值value来获得最终结果register_nickname。
		# split() 通过指定分隔符对字符串进行切片，切片后得到['id','register_nickname'],。更多用法需百度
		by = data.split('>')[0]
		value = data.split('>')[1]
		#try... except....容错处理
		try :
			if  by == 'id':
				return  self.driver.find_element_by_id(value)
			elif  by == 'name' :
				return  self.driver.find_element_by_name(value)
			elif  by == 'className' :
				return  self.driver.find_element_by_class_name(value)
			else :
				return  self.driver.find_element_by_xpath(value)
		except :
			return  None