# -*- coding: utf-8 -*-
# !user/bin/env python3
# Created on Sun Oct 29 10:46:26 2017
# @author: gaiusyao

avengers = ['iron man', 'captain america', 'hulk', 'thor']

print("Output #1: ")
for avenger in avengers:
    if avenger == 'iron man':
        print("\t{0} is very rich.".format(avenger.title()))
    else:
        print("\t{0} has no money.".format(avenger.title()))
        
iron_man = 'tony stark'
iron_man == 'tony stark' #相等，返回True
iron_man == 'bruce wayne' #不等，返回False

iron_man = 'Tony Stark'
iron_man == 'tony stark' #不等，返回False

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("\nOutput #2: Hold the anchovies!")
          
answer = 13
if answer != 42:
    print("\nOutput #3: That is not the ultlimate answer!!!")

answer = 42
answer < 69 #True
answer > 69 #False
answer >= 30 #True
answer <= 83 #True

age_0 = 22
age_1 = 18
age_0 >= 21 and age_1 >= 21 #False
age_0 >= 21 or age_1 >= 21 #True

# in
requested_toppings = ['mushrooms', 'onions', 'pineapple']
'mushrooms' in requested_toppings #True
'pepperoni' in requested_toppings #False

# not in
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print("\nOutput #4: {0}, you can post a response if you wish.".format(user.title()))

# if语句
age = 19
if age >= 18:
    print("\nOutput #5: You are old enough to vote!")  
          
# if-else语句
age = 16
if age >= 18:
    print("\nOutput #6: You are old enough to vote!")
else:
    print("\nOutput #6: Sorry, you are too young to vote.")
    
# if-elif-else结构          
age = 91
if age >= 18 and age < 70:
    print("\nOutput #7: You are old enough to drive!")
elif age >= 70:
    print("\nOutput #7: Sorry, you are too old to drive.")
else:
    print("\nOutput #7: Sorry, you are too young to drive.")
      
# 处理多个条件          
requested_toppings = ['mushrooms', 'extra cheese']
print("\nOutput #8: ")
if 'mushrooms' in requested_toppings:
    print("\tAdding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("\tAdding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("\tAdding extra cheese.")
print("Finished making your pizza!")          

# 检查列表中的特殊值
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
print("\nOutput #9: ")
for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("\tSorry, we are out of green peppers right now.")
    else:
        print("\tAdding {0}.".format(requested_topping))
print("Finished making your pizza!")

# 检查列表是否为空
requested_toppings = []
print("\nOutput #10: ")
if requested_toppings:
    for requested_topping in requested_toppings:
        print("\tAdding {0}.".format(requested_topping))
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")
    
# 处理多个列表
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
print("\nOutput #11: ")
if requested_toppings:
    for requested_topping in requested_toppings:
        if requested_topping in available_toppings:
            print("\tAdding {0}.".format(requested_topping))
        else:
            print("\tSorry, we don't have {0}.".format(requested_topping))
    print("Finished making your pizza!")
else:
    print("Are you sure you want a plain pizza?") 
    
# for循环
ninja_turtles = ['Leonardo', 'Raphael', 'Michelangelo', 'Donatello']
print("\nOutput #12: ")
for ninja_turtle in ninja_turtles:
    print(ninja_turtle)

ninja_turtles = ['Leonardo', 'Raphael', 'Michelangelo', 'Donatello']
print("\nOutput #13: ")
for ninja_turtle in ninja_turtles:
    print("{0} is a ninja.".format(ninja_turtle))  
print("They\'re Ninja Turtles!")

# input()
'''
message = input("Tell me something, and I will repeat it back to you: ")
print(message)    
    
age = input("How old are you? ")
age #'42'
# age >= 18
age = int(age)
age >= 18 #True
'''

# while循环
current_number = 1
print("\nOutput #14: ")
while current_number <= 5:
    print(current_number)
    current_number += 1
    
prompt = "Tell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program: "
message = ""
print("\nOutput #15: ")
while message != 'quit':
    message = input(prompt)
    print(message)  

# 使用标志退出循环    
active = True
print("\nOutput #16: ")
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        print(message)    

# 通过break语句退出循环        
print("\nOutput #17: ")
while True:
    city = input(prompt)

    if city == 'quit':
        break
    else:
        print("I'd love to go to {0}!".format(city.title()))  
        
# 使用continue语句决定是否继续执行循环
current_number = 0
print("\nOutput #18: ")
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

# 首先，创建一个待验证用户列表和一个用于存储已验证用户的空列表
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

print("\nOutput #19: ")
# 验证每个用户，直到没有未验证用户为止
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print("Verifying user: {0}".format(current_user.title()))
    confirmed_users.append(current_user)

# 显示所有已验证的用户
print("The following users have been confirmed:")
for confirmed_user in confirmed_users:
    print("\t{0}".format(confirmed_user.title()))    

# 创建一个宠物列表，其中包含多个值为'cat'的元素    
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

print("\nOutput #20 (original): ".format(pets))
while 'cat' in pets:
    pets.remove('cat')

print("\nOutput #20 (removed): ".format(pets))    
      
# 创建一个空字典
responses = {}

# 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
    # 提示输入被调查者的名字和回答
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # 将答卷存储在字典中
    responses[name] = response

    # 看看是否还有人要参与调查
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False

# 调查结束，显示结果
print("\nOutput #21: ")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")      