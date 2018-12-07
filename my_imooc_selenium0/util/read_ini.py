import  configparser

#--------2.20重构封装读取配置文件--------
class  ReadIni(object):                                       #这个类继承object，括号内的object可写可不写

	#添加一个构造函数，使得cf函数初始化就有，使得后面其他方法可引用
	def __init__(self,file_name = None,node = None):
		if  file_name  == None :
			file_name = 'E:/测试学习/my_imooc_selenium/config/LocalElement.ini'
		if node  == None :
			self.node = 'RegisterElement'      #node为节点
		else :
			self.node = node
		self.cf = self.load_ini(file_name)

	#加载文件
	def  load_ini(self,file_name):
		cf = configparser.ConfigParser()
		cf.read(file_name)
		return  cf

	#获取value值
	def get_vslue(self,key):
		data = self.cf.get(self.node,key)
		return  data


	#-------2.19-------
	# cf = configparser.ConfigParser()
	# cf.read('E:\TestStudy\imooc_selenium\config\LocalElement.ini')
	# print(cf.get('RegisterElement', 'user_email'))  # 获取.ini文件节点的信息

#实例化对象
if __name__ == '__main__' :
	read_ini = ReadIni()
	print(read_ini.get_vslue('user_name'))