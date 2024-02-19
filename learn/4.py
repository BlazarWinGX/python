# 第4章 操作列表

# 4.1 遍历整个列表
magicians = ['alice','david','carolina']
for magicians in magicians:
    print(magicians) #alice
                     #david
                     #carolina
# 4.1.1 深入研究循环

# 4.1.2 在for循环中执行更多的操作
magicians = ['alice','david','carolina']
for magicians in magicians:
    print(f"{magicians.title()}, that was a great trick!") #Alice, that was a great trick!
                                                           #David, that was a great trick!
                                                           #Carolina, that was a great trick!

magicians = ['alice','david','carolina']
for magicians in magicians:
    print(f"{magicians.title()}, that was a great trick!") 
    print(f"I can't wait to see your next trick, {magicians.title()}.\n") #Alice, that was a great trick!
                                                                          #I can't wait to see your next trick, Alice.

                                                                          #David, that was a great trick!
                                                                          #I can't wait to see your next trick, David.

                                                                          #Carolina, that was a great trick!
                                                                          #I can't wait to see your next trick, Carolina.
# 4.1.3 在for循环结束后执行一次操作
magicians = ['alice','david','carolina']
for magicians in magicians:
    print(f"{magicians.title()}, that was a great trick!") 
    print(f"I can't wait to see your next trick, {magicians.title()}.\n")
print("Thank you,everyone.That was a great magic show!")  #Alice, that was a great trick!
                                                                          #I can't wait to see your next trick, Alice.

                                                                          #David, that was a great trick!
                                                                          #I can't wait to see your next trick, David.

                                                                          #Carolina, that was a great trick!
                                                                          #I can't wait to see your next trick, Carolina.
                                                                        
                                                                          # Thank you,everyone.That was a great magic show!

# 4.2 避免缩进错误
# 4.2.1 忘记缩进
 #magicians = ['alice','david','carolina']
 #for magicians in magicians:
 #print(magicians)
# 4.2.2 忘记缩进额外的代码行
# 4.2.3 不必要的缩进
# 4.2.4 循环后不必要的缩进
# 4.2.5 遗漏冒号

# 4.3 创建数值列表
# 4.3.1 使用range()函数
for value in range(1,5):
    print(value) #1
                 #2
                 #3
                 #4
# 4.3.2 使用range()创建数值列表
number = list(range(1,6))
print(number) #[1, 2, 3, 4, 5]

even_number = list(range(2, 11, 2))
print(even_number) #[2, 4, 6, 8, 10]

squares = []
for value in range(1,11):
    square = value ** 2
    squares.append(square)
print(squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

squares = []
for value in range (1,11):
    squares.append(value**2)
print(squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 4.3.3 对数值列表执行简单的统计计算
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits)) #0
print(max(digits)) #9
print(sum(digits)) #45
# 4.3.4 列表推导式(list comprehension)
squares = [value**2 for value in range(1,11)]
print(squares) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 4.4 使用列表的一部分 #切片(slice)
# 4.4.1 切片
players = ['charles','martina','michael','florence','eli']
print(players[0:3]) #['charles', 'martina', 'michael']
print(players[1:4]) #['martina', 'michael', 'florence']
print(players[:4]) #['charles', 'martina', 'michael', 'florence'] #没有指定第一个索引，则从列表开头开始
print(players[2:]) #['michael', 'florence', 'eli'] #没有指定第二个索引，则从列表末尾结束
print(players[-3:]) #['michael', 'florence', 'eli'] #最后三位切片
# 4.4.2 历遍切片
players = ['charles','martina','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title()) #Here are the first three players on my team:
                          #Charles
                          #Martina
                          #Michael
# 4.4.3 复制列表
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
print("My favorite foods are:") #My favorite foods are:
print(my_foods) #['pizza', 'falafel', 'carrot cake']
print("\nMy friend's favorite foods are:") #My friend's favorite foods are:
print(friend_foods) #['pizza', 'falafel', 'carrot cake']

my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]
#这是行不通的:
#friend_foods = my_foods  #My favorite foods are:
                          #['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
                          #My friend's favorite foods are:
                          #['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:") #My favorite foods are:
print(my_foods) #['pizza', 'falafel', 'carrot cake', 'cannoli']
print("\nMy friend's favorite foods are:") #My friend's favorite foods are:
print(friend_foods) #['pizza', 'falafel', 'carrot cake', 'ice cream']
