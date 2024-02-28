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
# 6.2.5 删除键值对
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

# 6.3 遍历字典
# 6.3.1 遍历所有键值对
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")
    #Key: username
    #Value: efermi

    #Key: first
    #Value: enrico

    #Key: last
    #Value: fermi

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'rust',
    'phil': 'python',
}  
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is{language.title()}.")  
    #Jen's favorite language isPython.
    #Sarah's favorite language isC.
    #Edward's favorite language isRust.
    #Phil's favorite language isPython.
# 6.3.2 遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'rust',
    'phil': 'python',
} 
for name in favorite_languages.keys():
    print(name.title())
    #Jen
    #Sarah
    #Edward
    #Phil

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'rust',
    'phil': 'python',
} 
friends = ['phil','sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")
        #Hi Jen.
        #Hi Sarah.
                #Sarah, I see you love C!
        #Hi Edward.
        #Hi Phil.
               #Phil, I see you love Python!

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'rust',
    'phil': 'python',
} 
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")
    #Erin, please take our poll!
# 6.3.3 按指定的顺序遍历字典中的所有键
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'rust',
    'phil': 'python',
} 
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()},thank you for talking the poll.")
    #Edward,thank you for talking the poll.
    #Jen,thank you for talking the poll.
    #Phil,thank you for talking the poll.
    #Sarah,thank you for talking the poll.
# 6.3.4 遍历字典中的所有值
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'rust',
    'phil': 'python',
} 
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
    #The following languages have been mentioned:
    #Python
    #C
    #Rust
    #Python

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward':'rust',
    'phil': 'python',
} 
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
#集合(set) 集合中的每个元素必须独一无二
    print(language.title())
    #The following languages have been mentioned:
    #C
    #Python
    #Rust

languages = {'python','rust','python','c'}
print(languages)
#{'python', 'rust', 'c'}

# 6.4 嵌套
# 6.4.1 字典列表
alien_0 = {'color': 'green','points': 5}
alien_1 = {'color': 'yellow','points': 10}
alien_2 = {'color': 'red','points': 15}
aliens = [alien_0,alien_1,alien_2]
for alien in aliens:
    print(alien)
    #{'color': 'green', 'points': 5}
    #{'color': 'yellow', 'points': 10}
    #{'color': 'red', 'points': 15}

# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
#显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print(...)
# 显示创建了多少个外星人
print(f"Total number of aliens: {len(aliens)}")
#{'color': 'green', 'points': 5, 'speed': 'slow'}
#{'color': 'green', 'points': 5, 'speed': 'slow'}
#{'color': 'green', 'points': 5, 'speed': 'slow'}
#{'color': 'green', 'points': 5, 'speed': 'slow'}
#{'color': 'green', 'points': 5, 'speed': 'slow'}
#Ellipsis
#Total number of aliens: 30

# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个绿色外星人
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print(...) 
#{'color': 'yellow', 'points': 10, 'speed': 'medium'}
#{'color': 'yellow', 'points': 10, 'speed': 'medium'}
#{'color': 'yellow', 'points': 10, 'speed': 'medium'}
#{'color': 'green', 'points': 5, 'speed': 'slow'}
#{'color': 'green', 'points': 5, 'speed': 'slow'}
#Ellipsis

# 创建一个用于存储外星人的空列表
aliens = []
# 创建30个黄色外星人
for alien_number in range(30):
    new_alien = {'color': 'yellow', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
# 显示前5个外星人
for alien in aliens[:5]:
    print(alien)
print(...) 
#{'color': 'red', 'points': 15, 'speed': 'fast'}
#{'color': 'red', 'points': 15, 'speed': 'fast'}
#{'color': 'red', 'points': 15, 'speed': 'fast'}
#{'color': 'yellow', 'points': 5, 'speed': 'slow'}
#{'color': 'yellow', 'points': 5, 'speed': 'slow'}
#Ellipsis
