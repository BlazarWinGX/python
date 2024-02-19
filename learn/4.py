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
