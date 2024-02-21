# 第5章 if语句

# 5.1 一个简单示例
cars = ['audi','bmw','subaru','toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title()) #Audi  
                          #BMW   
                          #Subaru
                          #Toyota
       
# 5.2 条件测试
# 5.2.1 检查是否相等
car = 'bmw'
print(car == 'bmw') #True

car = 'audi'
print(car == 'bmw') #False
# 5.2.2 如何在检查是否相等时忽略大小写
car = 'Audi'
print(car == 'audi') #False
print(car.lower() == 'audi') #True
print(car) #Audi
# 5.2.3 检查是否不等
requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!") #Hold the anchovies!
# 5.2.4 数值比较
age = 18
print(age == 18) #True

answer = 17
if answer != 42:
    print("That is not the correct answer. Please trt again!") 
    #That is not the correct answer. Please trt again!
age = 19
print(age < 21) #True
print(age <= 21) #True
print(age > 21) #False
print(age >= 21) #False
# 5.2.5 检查多个条件
# 01.使用and检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >= 21) #False
age_1 = 22
print(age_0 >= 21 and age_1 >= 21) #True
# 02.使用or检查多个条件
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >= 21) #True
age_0 = 18
print(age_0 >= 21 or age_1 >= 21) #False
# 5.2.6检查特定的值是否在列表中
requested_toppongs = ['mushrooms','onions','pineapple']
print('mushrooms' in requested_topping) #True
print('pepperoni' in requested_topping) #False
# 5.2.7 检查特定的值是否不在列表中
banned_users = ['andrew','carolina','david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")
#Marie, you can post a response if you wish.
# 5.2.8 布尔表达式
game_active = True
print(game_active) #True
can_edit = False
print(can_edit) #False

# 5.3 if语句
# 5.3.1 简单的if语句
age = 19
if age >= 18:
    print("You are old enough to vote!") #You are old enough to vote!

age = 19
if age >= 18:
    print("You are old enough to vote!") #You are old enough to vote!
    print("Have you registered to vote yet?") #Have you registered to vote yet?
# 5.3.2 if-else语句
age = 17
if age >= 18:
    print("You are old enough to vote!") 
    print("Have you registered to vote yet?")
else:
    print("Sorry,you are too young to vote.") #Sorry,you are too young to vote.
    print("Please,register to vote as soon as you turn 18!")
    #Please,register to vote as soon as you turn 18!
# 5.3.3 if-elif-else语句
age = 12
if age < 4:
    print("Your admission cost in $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")
    #Your admission cost is $25.

age =12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.") #Your admission cost is $25.
# 5.3.4 使用多个elif代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.") #Your admission cost is $25.
# 5.3.5 省略else代码块
age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:
    price = 20
print(f"Your admission cost is ${price}.") #Your admission cost is $25.
# 5.3.6 测试多个条件
requested_toppings = ['mushrooms','extra cheese']
if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppongs:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
print("\nFinished making your pizza!") #Adding mushrooms.
                                       #Adding extra cheese.

                                       #Finished making your pizza!
#此时使用if-elif-else语句，代码将不能运行

# 5.4 使用if语句处理列表
# 5.4.1 检查特殊元素
requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}")
print("\nFinished making your pizza!") #Adding mushrooms
                                       #Adding green peppers
                                       #Adding extra cheese

                                       #Finished making your pizza!

requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry,We are out of green peppers right now.")
    else:
        print(f"Adding {requested_topping}")
print("\nFinished making your pizza!")
#Adding mushrooms
#Sorry,We are out of green peppers right now.
#Adding extra cheese

#Finished making your pizza!
# 5.4.2 确定列表非空
requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinish making your pizza!")
else:
    print("Are you sure you want a plain pizza?") 
    #Are you sure you want a plain pizza?
# 5.4.3 使用多个列表
available_toppings = ['mushrooms','olives','green peppers',
                      'pepperoni','pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']
for requested_topping in requested_toppongs:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry,We don't have {requested_topping}.")
print("\nFinished making your pizza!")
#Adding mushrooms.
#Sorry,We don't have french fries.
#Adding pineapple.

#Finished making your pizza!

# 5.5 设置if语句的格式
#根据PEP8,在诸如==、>=和<=等运算符两边各添加一个空格
#if age < 4:
#要比
#if age<4:
#更好
