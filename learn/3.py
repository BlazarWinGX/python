# 三、列表简介
# 3.1 列表是什么 #列表(list [])
bicycles =['trek','cannondale','redline','specialized']
print(bicycles) #['trek', 'cannondale', 'redline', 'specialized']
# 3.1.1 访问列表元素
bicycles =['trek','cannondale','redline','specialized']
print(bicycles[0]) #trek #返回第一个元素
print(bicycles[0].title()) #Trek
# 3.1.2 索引从0而不是1开始
###注意差一错误###
bicycles =['trek','cannondale','redline','specialized']
print(bicycles[1]) #cannondale #返回第二个元素
print(bicycles[3]) #specialized #返回第四个元素
print(bicycles[-1]) #specialized #返回倒数第一个元素
print(bicycles[-3]) #cannondale #返回倒数第三个元素
# 3.1.3 使用列表的各个值
bicycles =['trek','cannondale','redline','specialized']
message = f"My first bicycle was a {bicycles[0].title()}." 
print(message) #My first bicycle was a Trek.
# 3.2 修改、添加和删除元素
# 3.2.1 修改列表元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles) #['honda', 'yamaha', 'suzuki']
motorcycles[0] = 'ducati'
print(motorcycles) #['ducati', 'yamaha', 'suzuki']
# 3.2.2 在列表中添加元素
# 01.在列表末尾添加元素 #追加(append)
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles) #['honda', 'yamaha', 'suzuki']
motorcycles.append('ducati')
print(motorcycles) #['honda', 'yamaha', 'suzuki', 'ducati']
# 02.在列表中插入元素 #insert()
motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles) #['ducati', 'honda', 'yamaha', 'suzuki']
# 3.2.3 从列表中删除元素
# 01.使用del语句删除元素
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles) #['honda', 'yamaha', 'suzuki']
del motorcycles[0]
print(motorcycles) #['yamaha', 'suzuki']

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles) #['honda', 'yamaha', 'suzuki']
del motorcycles[1]
print(motorcycles) #['honda', 'suzuki']
# 02.使用pop()方法删除元素 #弹出(pop)
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles) #['honda', 'yamaha', 'suzuki']
popped_motorcycles = motorcycles.pop()
print(motorcycles) #['honda', 'yamaha']
print(popped_motorcycles) #suzuki

motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.") #The last motorcycle I owned was a Suzuki.
# 03.删除列表中任意位置的元素
motorcycles = ['honda','yamaha','suzuki']
last_owned = motorcycles.pop(0)
print(f"The last motorcycle I owned was a {last_owned.title()}.") #The last motorcycle I owned was a Honda.
# 04.根据值删除元素 #remove()
motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles) #['honda', 'yamaha', 'suzuki', 'ducati']
motorcycles.remove('ducati')
print(motorcycles) #['honda', 'yamaha', 'suzuki']

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles) #['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive) 
print(motorcycles) #['honda', 'yamaha', 'suzuki']
print(f"\nA {too_expensive.title()} is too expensive for me.") #A Ducati is too expensive for me.
