# 2.2 变量（variable）
message="hello python world!"
print(message) #hello python world!
message="hello python crash course world!"
print(message) #hello python crash course world!
mesage="hello python crash course world!"
print(mesage) #hello python crash course world!
# 2.3 字符串（string）
'This is a string.'
"This is a string."
'"This is a string."'
# 2.3.1 修改字符串的大小写
name="ada lovelace"
print(name.title()) #Ada Lovelace #title.() 以首字母大写形式显示每个单词
name="ada lovelace"
print(name.upper()) #ADA LOVELACE #name.upper() 以全部大写显示每个单词
print(name.lower()) #ada lovelace #name.lower() 以全部小写显示每个单词
# 2.3.2 字符串中使用变量
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #f字符串（formet）
print(f"Hello,{full_name.title()}!") #Hello,Ada Lovelace!

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello,{full_name.title()}!"
print(message) #Hello,Ada Lovelace!
# 2.3.3 使用制表符或换行符来添加空白
print("\tpython") #         python #添加制表符\t
print("Languages:\npython\nc\nJavascript") #Languages:
                                           #python
                                           #c
                                           #Javascript #换行符\n
print("Languages:\n\tpython\n\tc\n\tJavascript") #Languages:
                                                        #python
                                                        #c
                                                        #Javascript #制表+换行\n\t
# 2.3.4 删除空白 #strip() #rstrip() lstrip()
 #暂时删除 
  #>>> favorite_language ='python '
  #>>> favorite_language 
  #'python '
  #>>> favorite_language.rstrip() 
  #'python'
  #>>> favorite_language 
  #'python '
 #永久删除 
  #>>> favorite_language ='python '
  #>>> favorite_language = favorite_language.rstrip()
  #>>> favorite_language
  #'python'
 #删除左右空白
  #>>> favorite_language =' python '
  #>>> favorite_language.rstrip()
  #' python'
  #>>> favorite_language.lstrip()
  #'python '
  #favorite_language.strip()
  #'python'
 # 2.3.5 删除前缀 removeprefix()
  #暂时删除 
  #>>> nostarch_url = 'https//nostarch.com'
  #>>> nostarch_url.removeprefix('https://') 
  #'nostarch.com'
  #永久删除 
  #>>> simple_url = nostarch_url.removeprefix('https://')
#2.3.6 如何在使用字符串时避免错误
message = "One of python's strengths is its diverse community."
  # message = 'One of python's strengths is its diverse community.'# 输出中包含'使用""避免语法错误
print(message)
# 2.4 数
print(2+3) #5 加   
print(5-3) #2 减
print(3*3) #9 乘
print(12/4) #3.0 除
print(3**3) #27 乘方
print(2+3*4) #14
print((2+3)*4) #20 调整运算顺序
# 2.4.2 浮点数float
print(0.1+0.1) #0.2
print(0.1+0.2) #0.30000000000000004
print(3*0.1) #0.30000000000000004 所有语言存在的问题，暂时忽略即可
# 2.4.3 整数和浮点数
print(4/2) #2.0
print(2*3.0) #6.0
print(3.0**2) #9.0 只要操作数中有浮点数，结果总是浮点数
# 2.4.4 数中的下滑线
universe_age = 14_000_000_000
print(universe_age) #python存储这种数时会忽略下滑线，此法既适用于整数，又适用于浮点数
# 2.4.5 同时给多个变量赋值
x,y,z = 1,2,3
print(x+y+z) #6
# 2.4.6 常量constant
MAX_CONNECTIONS = 5000
print(MAX_CONNECTIONS) #5000 全大写将变量视为常量
# 2.5 注释(#)
#略
# 2.6 python之禅
import this 
