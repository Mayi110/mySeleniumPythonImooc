import  pytesseract
import  time
from  PIL import  Image
from  imooc_selenium.ShowapiRequest import ShowapiRequest


# 2-14使用pytesseract识别干扰较少图片的文字：
# 1、下载pytesseract库，第三方库
# 2、打开验证码图片对象
# iamge = Image.open('E:/测试学习/《selenium3+python3自动化测试实战》/imooc2.png')
# text = pytesseract.image_to_string(iamge)
# print(text)
# 执行报错，下次解决
# pytesseract.pytesseract.TesseractNotFoundError: tesseract is not installed or it's not in your path
#已解决，成功转换成图片。解决方法：见文档

# 2-15showapiRequest解决图片验证码识别（较复杂），需付费
# 1、把showapiRequest.py下载后复制到文件目录下，且showapiRequest.py需要导入requests库
# 2、把showapiRequest库导入
r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "0")
r.addFilePara("image", 'E:/测试学习/《selenium3+python3自动化测试实战》/imooc1.png') #文件上传时设置
res = r.post()
time.sleep(1)
text = res.json()['showapi_res_body']['Result']
print(text)  #返回信息