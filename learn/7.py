# 第7章 用户输入和while循环

# 7.1 input()函数的工作原理
message = input("Tell me something, and I will repeat it back to you: ")
print(message)
#Tell me something, and I will repeat it back to you: hello
#hello
# 7.1.1 编写清晰的提示
name = input("Please enter your name: ")
print(f"\nHello,{name}!")
#Please enter your name: eric

#Hello,eric!
# 7.1.2 使用int()来获取数值输入
age = input("How old are you? ")
print(age)
#How old are you? 21
#21

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
    #How tall are you, in inches? 71

    #You're tall enough to ride!

# 7.1.3 求模运算符(%)
number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")
    #Enter a number, and I'll tell you if it's even or odd: 42

    #The number 42 is even.

#7.2 while 循环简介
# 7.2.1 使用while循环
current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1
    #1
    #2
    #3
    #4
    #5
# 7.2.2 让用户选择何时退出
prompt= "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end program."
message = ""
while message != 'quit':
    message = input(prompt)
    print(message)
    #Tell me something,and I will repeat it back to you:
    #Enter 'quit' to end program.Hello everyone!
    #Hello everyone!

    #Tell me something,and I will repeat it back to you:
    #Enter 'quit' to end program.Hello again.
    #Hello again.

    #Tell me something,and I will repeat it back to you:
    #Enter 'quit' to end program.quit
    #quit

prompt= "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end program."
message = ""
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(message)
        #Tell me something,and I will repeat it back to you:
        #Enter 'quit' to end program.Hello everyone!
        #Hello everyone!

        #Tell me something,and I will repeat it back to you:
        #Enter 'quit' to end program.Hello again.
        #Hello again.

        #Tell me something,and I will repeat it back to you:
        #Enter 'quit' to end program.quit
# 7.2.3 使用标志
prompt= "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end program."
active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False 
    else:
        print(message)
        #Tell me something,and I will repeat it back to you:
        #Enter 'quit' to end program.hello!
        #hello!

        #Tell me something,and I will repeat it back to you:
        #Enter 'quit' to end program.hello world!
        #hello world!

        #Tell me something,and I will repeat it back to you:
        #Enter 'quit' to end program.quit
# 7.2.4 使用break退出循环
prompt= "\nTell me something,and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end program."
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
        #Tell me something,and I will repeat it back to you:
        #Enter 'quit' to end program.New York
        #I'd love to go to New York!

        #Tell me something,and I will repeat it back to you:
        #Enter 'quit' to end program.San Francisco
        #I'd love to go to San Francisco!

        #Tell me something,and I will repeat it back to you:
        #Enter 'quit' to end program.quit
# 7.5.2 在循环中使用continue
current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)
    #1
    #3
    #5
    #7
    #9
# 7.2.6 避免无限循环
x = 1
while x <= 5:
    print(x)
    x += 1
    #1
    #2
    #3
    #4
    #5

# 7.3 使用while循环处理列表和字典
# 7.3.1 在列表之间移动元素
# 首先，创建一个待验证用户列表
#和一个用于存储已验证的用户列表
unconfirmed_users = ['alice','brian','candace']
confirmed_users = []
# 验证每个用户，直到没有未验证的用户为止
# 将每个经过验证的用户都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
# 显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
    #Verifying user: Candace
    #Verifying user: Brian
    #Verifying user: Alice

    #The following users have been confirmed:
    #Candace
    #Brian
    #Alice
# 7.3.2 删除为特定值的所有列表元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)
while 'cat' in pets:
    pets.remove('cat')
print(pets)
#['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
#['dog', 'dog', 'goldfish', 'rabbit']
# 7.3.3 使用用户输入填充字典
responses = {}
# 设置一个用户标志，指出调查是否继续
polling_active = True
while polling_active:
    #提示输入被调查者的名字和回答
    name = input("\nWhat is your name?")
    response = input("Which mountain would you like to climb someday?")
    #将回答存储在字典中
    responses[name] = response
    #查看是否还有人要参与调查
    repeat = input("Would you like to let another person respond?(yes/no)")
    if repeat == 'no':
        polling_active = False
#调查结果，显示结果
print("\n---Poll Results---")
for name,response in responses.items():
    print(f"{name} would like to climb {response}") 
    #What is your name?Eric
    #Which mountain would you like to climb someday?Denali
    #Would you like to let another person respond?(yes/no)yes

    #What is your name?Lynn
    #Which mountain would you like to climb someday?Devil's Thumb
    #Would you like to let another person respond?(yes/no)no

    #---Poll Results---
    #Eric would like to climb Denali       
    #Lynn would like to climb Devil's Thumb
