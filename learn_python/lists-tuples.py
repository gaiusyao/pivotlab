# -*- coding: utf-8 -*-
# !/usr/bin/env python3
# Created on Sat Oct 28 10:03:11 2017
# @author: gaiusyao

band = ['Bon Jovi', 'Guns & Roses', 'Radiohead', 'Simple Plan']
print("Output #1: {0}".format(band)) #将列表打印出来，包括方括号

print("Output #2: {0}".format(band[0])) #列表索引也是从0开始      
print("Output #3: {0}".format(band[-1])) #同样可以使用负数索引  
      
print("Output #4: {0}".format(band[-3:]))       
      
message = "My favorite band is " + band[0].title() + "!"
print("Output #5: {0}".format(message))
      
band.append('Zard') #使用append(),将元素附加到列表末尾
print("Output #6: {0}".format(band)) 
band.insert(1, 'Sum 41') #使用insert(),将元素插入到列表中第二个位置
print("Output #7: {0}".format(band)) 
      
band[1] = "Sum 42"
print("Output #8: {0}".format(band[1])) 

#方法1：使用del语句删除指定位置的元素
del band[1] 
print("Output #9: {0}".format(band)) 
#方法2：使用pop()函数删除列表末尾的元素，或者更形象的称之为弹出
popped_band = band.pop()
print("Output #10 (band): {0}".format(band)) 
print("Output #10 (popped_band): {0}".format(popped_band)) 
#方法3：使用pop()来删除列表中指定位置的元素
first_band = band.pop(0)
print("Output #11 (band): {0}".format(band)) 
print("Output #11 (first_band): {0}".format(first_band)) 
#方法4：使用remove()根据元素值删除元素
band.remove('Simple Plan')
print("Output #12 (band): {0}".format(band)) 

# sort() & sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort() #sort()排序将会永久性的改变列表的顺序
print("Output #13: {0}".format(cars))       
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Output #13 (sorted): {0}".format(sorted(cars)))
print("Output #13 (original): {0}".format(cars)) 
      
# reverse()
cars.reverse()
print("Output #15 (reversed): {0}".format(cars))
cars.reverse()
print("Output #15 (original): {0}".format(cars))
      
# len()
print("Output #16: {0}".format(len(cars))) #4    

# try IndexError
# band[42] 

ninja_turtles = ['Leonardo', 'Raphael', 'Michelangelo', 'Donatello']
print("Output #17: ")
for ninja_turtle in ninja_turtles:
    print(ninja_turtle)
print("Output #18: ")
for ninja_turtle in ninja_turtles:
    print(ninja_turtle.title() + ", is a ninja!")   
    
print("Output #19: ") 
for value in range(1,5):
    print(value)
#range()中第1、2个参数分别是起始值，第3个参数为步长，从2开始数，然后不断地加2，直到达到或超过终值（11）
numbers = list(range(2,11,2)) 
print("Output #20: {0}".format(numbers))
      
squares = []
for square in range(1,11):
    squares.append(square**2)
print("Output #21: {0}".format(squares))  
squares = [value**2 for value in range(1,11)]
print("Output #22: {0}".format(squares))      

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print("Output #23 (min): {0}".format(min(digits))) #0
print("Output #23 (max): {0}".format(max(digits))) #9
print("Output #23 (sum): {0}".format(sum(digits))) #45
      
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Here are the first three players on my team:")
for player in players[:3]: #遍历切片
    print(player.title())
other_players = players[3:] #复制列表的剩余部分
print("Here are the first three players on my team:")
for player in other_players [:]: #遍历切片
    print(player.title())
    
# Tuples
dimensions = (200, 120)
print("Output #24 (length): {0}".format(dimensions[0]))
print("Output #24 (width): {0}".format(dimensions[1]))    

for dimension in dimensions: #遍历元组
    print("Output #25: {0}".format(dimension))    

dimensions = (400, 100) #修改元组变量
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)          