# -*- coding: utf-8 -*-
# !user/bin/env python3
# Created on Mon Oct 30 12:01:52 2017
# @author: gaiusyao

# 1.定义函数的简单示例
def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end = ' ')
        a, b = b, a+b

print("Output #1: ")        
fib(2000)

# 2&3.调用实参
def describe_pet(animal_type, pet_name):
    """显示宠物的信息"""
    print("I have a {0}.".format(animal_type))
    print("My {0}'s name is {1}.".format(animal_type, pet_name.title()))

print("\n\nOutput #2: ")        
describe_pet('hamster', 'harry') #位置实参
print("\nOutput #3: ")  
describe_pet(pet_name='harry', animal_type='hamster') #关键字实参

# 4.默认值
def describe_pet(pet_name, animal_type='dog'): #默认值
    """显示宠物的信息"""
    print("I have a {0}.".format(animal_type))
    print("My {0}'s name is {1}.".format(animal_type, pet_name.title()))
print("\nOutput #4: ")      
describe_pet(pet_name='willie')

# 5.返回简单值
def get_formatted_name(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()
musician = get_formatted_name('jimi', 'hendrix')
print("\nOutput #5: \n{0}".format(musician))

# 6.让实参变成可选的
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
print("\nOutput #6: ")  
musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

# 7.返回字典
def build_person(first_name, last_name):
    """返回一个字典，其中包含有关一个人的信息"""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print("\nOutput #7: \n{0}".format(musician))

# 8.结合使用函数和while循环      
def get_formatted_name(first_name, last_name, middle_name=''):
    """返回整洁的姓名"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()

print("\nOutput #8: ")  
while True:
    print("Please tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

# 9.传递列表   
def greet_users(names):
    """向列表中的每位用户都发出简单的问候"""
    for name in names:
        print("Hello, {0}!".format(name.title()))

usernames = ['hannah', 'ty', 'margot']
print("\nOutput #9: ")
greet_users(usernames)  

# 10.结合使用位置实参和任意数量实参
def make_pizza(size, *toppings):
    """概述要制作的比萨"""
    print("\nMaking a {0}-inch pizza with the following toppings:".format(str(size)))
    for topping in toppings:
        print("- {0}".format(topping))

print("\nOutput #10: ") 
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')  

# 11.结合使用位置实参和任意数量实参
def build_profile(first, last, **user_info):
    """创建一个字典，其中包含我们知道的有关用户的一切"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last 

    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
print("\nOutput #11: ") 
print(user_profile)  