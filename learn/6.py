# 第6章 字典

# 6.1 一个简单的字典
alien_0 = {'color': 'green','points': 5}
print(alien_0['color']) #green
print(alien_0['points']) #5

#6.2 使用字典
#字典(dictionary)是一系列键值对
# 6.2.1 访问字典中的值
alien_0 = {'color': 'green'}
print(alien_0['color']) #green

alien_0 = {'color': 'green','points': 5}
new_points = alien_0['points']
print(f"You just earned {new_points} points!") #You just earned 5 points!
# 6.2.2 添加键值对
alien_0 = {'color': 'green','points': 5}
print(alien_0)
#{'color': 'green', 'points': 5}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
#{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}
# 6.2.3  从创建一个空字典开始
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
#{'color': 'green', 'points': 5}
# 6.2.4 修改字典中的值
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.") #The alien is green.
alien_0['color'] = 'yellow'
print(f"The alien is new {alien_0['color']}.") #The alien is new yellow.

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position:{alien_0['x_position']}") #Original position:0
# 向右移动外星人
# 根据当前速度确定将外星人向右移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # 这个外星人的移动速度肯定很快
    x_increment = 3
# 新位置为旧位置加上移动距离
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}") #New position: 2
# 6.5.2 删除键值对
alien_0 = {'color': 'green','points': 5}
print(alien_0) #{'color': 'green', 'points': 5}
del alien_0 ['points']
print(alien_0) #{'color': 'green'}
# 6.2.6 由类似的对象组成的字典
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'rust',
    'phil': 'python',
} 
language = favorite_languages['sarah'].title()
print(f"Sarah's favorite_languages is {language}.") 
#Sarah's favorite_languages is C.
# 6.2.7 使用 get()来访问值
alien_0 = {'color': 'green','speed': 'slow'}
point_value = alien_0.get('points','No point value assigned.')
print(point_value) #No point value assigned.
