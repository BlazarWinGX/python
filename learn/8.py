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
