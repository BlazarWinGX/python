#1.1 hello python world!
print('hello world!') #hello world!
print('hello python interpreter!') #hello python interpreter!
print('hello python world!') #hello python world!
#2.2 变量（variable）
message="hello python world!"
print(message) #hello python world!
message="hello python crash course world!"
print(message) #hello python crash course world!
mesage="hello python crash course world!"
print(mesage) #hello python crash course world!
#2.3 字符串（string）
'This is a string.'
"This is a string."
'"This is a string."'
#2.3.1 修改字符串的大小写
name="ada lovelace"
print(name.title()) #Ada Lovelace #title.() 以首字母大写形式显示每个单词
name="ada lovelace"
print(name.upper()) #ADA LOVELACE #name.upper() 以全部大写显示每个单词
print(name.lower()) #ada lovelace #name.lower() 以全部小写显示每个单词
#2.3.2 字符串中使用变量
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}" #f字符串（formet）
print(f"Hello,{full_name.title()}!") #Hello,Ada Lovelace!

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello,{full_name.title()}!"
print(message) #Hello,Ada Lovelace!
#2.3.3 使用制表符或换行符来添加空白
