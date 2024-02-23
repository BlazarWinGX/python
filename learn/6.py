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
# 6.2.4 修改字典中的值(P142)
alien_0 = {'color': 'green'}
