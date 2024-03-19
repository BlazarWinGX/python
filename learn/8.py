# 第8章 函数
# 8.1 定义函数
def green_user():
    """显示简单问候语"""
    print("hello!")
green_user()
#hello!
# 8.1.1 向函数传递信息
def green_user(username):
    """显示简单的问候语"""
    print(f"Hello,{username.title()}!")
green_user('jesee')
#Hello,Jesee!
# 8.1.2 实参和形参
def green_user(username):
    """显示简单的问候语"""
    print(f"Hello,{username.title()}!")
green_user('jesee')
#Hello,Jesee!
#以上代码中：变量username是形参；值jesee是实参

# 8.2 传递实参
# 8.2.1 位置实参
def describe_pet(animal_type,pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster','harry')
#I have a hamster.
#My hamster's name is Harry.
# 01.调用函数多次
def describe_pet(animal_type,pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet('hamster','harry')
describe_pet('dog','willie')
#I have a hamster.
#My hamster's name is Harry.

#I have a dog.
#My dog's name is Willie.
# 02. 位置实参的顺序很重要
# 8.2.2 关键词实参
def describe_pet(animal_type,pet_name):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(animal_type='hamaster',pet_name='harry')
#I have a hamaster.
#My hamaster's name is Harry.
# 8.2.3 默认值
def describe_pet(pet_name,animal_type='dog'):
    """显示宠物信息"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
describe_pet(pet_name='willie')
#I have a dog.
#My dog's name is Willie.
# 8.2.4 等效的函数调用
# 一条名为 Willie 的小狗
describe_pet('willie')
describe_pet(pet_name='willie')
# 一只名为 Harry 的仓鼠
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harry')           
# 8.2.5 避免实参错误

# 8.3 返回值
# 8.3.1 返回简单值
def get_formatted_name(first_name,last_name):
    """返回标准格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)
#Jimi Hendrix
# 8.3.2 让实参变成可选的
def get_formatted_name(first_name,middle_name,last_name):
    """返回标准格式的姓名"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('john','lee','hooker')
print(musician)
#John Lee Hooker

def get_formatted_name(first_name,middle_name,last_name=''):
    """返回标准格式的姓名"""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()
musician = get_formatted_name('jimi','hendrix')
print(musician)
musician = get_formatted_name('john','lee','hooker')
print(musician)
#Jimi Hendrix 
#ohn Lee Hooker

# 8.3.3 返回字典
def build_person(first_name,last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name,'last': last_name}
    return person
musician = build_person('jimi','hendrix')
print(musician)
#{'first': 'jimi', 'last': 'hendrix'}
def build_person(first_name,last_name,age=None):
    """返回一个字典，其中包含有关一个人的"""
    person = {'first': first_name,'last': last_name}
    if age:
        person['age'] = age
    return person
musician = build_person('jimi','hendrix', age=27)
print(musician)
#{'first': 'jimi', 'last': 'hendrix', 'age': 27}
# 8.3.4 结合使用函数和while循环
def get_formatted_name(first_name,last_name):
    """返回规范格式的姓名"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name:")
    if l_name == 'q':
        break
formatted_name = get_formatted_name(f_name, l_name)
print(f"\nHello, {formatted_name}!")
#Please tell me your name:
#(enter 'q' at any time to quit)
#First name: eric
#Last name:matthes

#Please tell me your name:
#(enter 'q' at any time to quit)
#First name: q

#Hello, Q Matthes!

# 8.4 传递列表
def green_users(names):
    """向列表中每个用户发出简单的问候"""
    for name in names:
        msg = f"Hello, {name.title()}"
        print(msg)
usernames = ['hannah','ty','margot']
green_users(usernames)
#Hello, Hannah!
#Hello, Ty!
#Hello, Margot!
