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
