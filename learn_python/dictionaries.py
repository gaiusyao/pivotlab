# -*- coding: utf-8 -*-
# ！user/bin/env python3
# Created on Sat Oct 28 19:29:27 2017
# @author: gaiusyao

simple_dict = {'one':1, 'two':2, 'three':3}
print("Output #1: {0}".format(simple_dict)) #将字典打印出来，包括花括号
      
ninja_turtle_0 = {'name':'Leonardo', 'color':'blue', 'weapon':'sword'}
print("Output #2: {0}".format(ninja_turtle_0['name']))
      
ninja_turtle_0['x_position'] = 190
ninja_turtle_0['y_position'] = 250
print("Output #3: {0}".format(ninja_turtle_0))
      
master_rat = {}
master_rat['name'] = "Splinter"
master_rat['color'] = "grey"
print("Output #4: {0}".format(master_rat))

ninja_turtle_0['x_position'] = 250
ninja_turtle_0['y_position'] = 200
print("Output #5: {0}, {1}".format(ninja_turtle_0['x_position'], ninja_turtle_0['y_position']))

del ninja_turtle_0['weapon'] #删除武器
print("Output #6: {0}".format(ninja_turtle_0))     
      
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("Output #7:\nSarah's favorite language is " + favorite_languages['sarah'].title() + ".")    
      
print("Output #8: ")
for key, value in favorite_languages.items():
    print(key.title() + "'s favorite language is " + value.title() + ".")
    
print("Output #9: ")
for name in favorite_languages.keys():
    print(name.title())

print("Output #10: ")
for name in sorted(favorite_languages.keys()):
    print("{0}, thank you for taking the poll.".format(name.title())) 
    
print("Output #11: ")
for language in favorite_languages.values():
    print(language.title())    
    
print("Output #12: ")
for language in set(favorite_languages.values()):
    print(language.title())

ninja_turtle_0 = {'name':'Leonardo', 'color':'blue', 'weapon':'katana'}
ninja_turtle_1 = {'name':'Raphael', 'color':'red', 'weapon':'sai'}
ninja_turtle_2 = {'name':'Michelangelo', 'color':'orange', 'weapon':'double-cut stick'}
ninja_turtle_3 = {'name':'Donatello', 'color':'purple', 'weapon':'bo'}

ninja_turtles = [ninja_turtle_0, ninja_turtle_1, ninja_turtle_2, ninja_turtle_3]
print("Output #13: ")
for ninja_turtle in ninja_turtles:
    print(ninja_turtle)
    
#创建一个空列表
foot_ninjas = []

#创建30个脚帮杂兵
for foot_ninja_num in range(30):
    new_foot_ninja = {'color': 'black', 'weapon':'sword'}
    foot_ninjas.append(new_foot_ninja)

#显示前5个脚帮杂兵的详细信息，和总数
print("Output #14: ")
for foot_ninja in foot_ninjas[:5]:
    print(foot_ninja)
print("Total number of foot ninjas: " + str(len(foot_ninjas)))    

print("Output #15: ")
for foot_ninja in foot_ninjas[3:9]:
    if foot_ninja['weapon'] != 'bow':
        foot_ninja['weapon'] = 'bow'
    print(foot_ninja)
    
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }
# 概述所点的比萨
print("Output #16: \nYou ordered a {0}-crust pizza with the following toppings:".format(pizza['crust']))
for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

print("Output #17: ")
for name, languages in favorite_languages.items():
    print("\n{0}'s favorite languages are:".format(name.title()))
    for language in languages:
        print("\t{0}".format(language.title()))    
        
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }
    
for username, user_info in users.items():
    print("\nUsername: {0}".format(username))
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    print("\tFull name: {0}".format(full_name.title()))
    print("\tLocation: {0}".format(location.title()))   