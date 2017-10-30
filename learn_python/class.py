# -*- coding: utf-8 -*-
# !user/bin/env python3
# Created on Mon Oct 30 16:46:25 2017
# @author: gaiusyao
from collections import OrderedDict

# 创建Dog类
class Dog():
    """一次模拟小狗的简单尝试"""

    def __init__(self, name, age):
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self):
        """模拟小狗被命令时蹲下"""
        print("{0} is now sitting.".format(self.name.title()))

    def roll_over(self):
        """模拟小狗被命令时打滚"""
        print("{0} rolled over!".format(self.name.title()))
        
# 1.根据类创建实例
my_dog = Dog('willie', 6)
print("Output #1: ")
print("My dog's name is {0}.".format(my_dog.name.title()))
print("My dog is {0} years old.".format(str(my_dog.age)))
my_dog.sit()        

# 2.创建Car类
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print("\nOutput #2: ")
print(my_new_car.get_descriptive_name())    

# 3.给属性设置默认值
class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

my_new_car = Car('audi', 'a4', 2016)
print("\nOutput #3: ")
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 修改属性值
#my_new_car.odometer_reading = 23；

class Car():
    """一次模拟汽车的简单尝试"""

    def __init__(self, make, model, year):
        """初始化描述汽车的属性"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """返回整洁的描述性信息"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        """打印一条指出汽车里程的消息"""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles  

# 4.子类ElectricCar
class ElectricCar(Car):
    """电动汽车的独特之处""" 

    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print("\nOutput #4: ")
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

# 5.将实例用作属性
class Battery():
    """一次模拟电动汽车电瓶的简单尝试"""
    def __init__(self, battery_size=70):
        """初始化电瓶的属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
    """电动汽车的独特之处""" 

    def __init__(self, make, model, year):
        """初始化父类的属性，再初始化电动汽车特有的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """打印一条描述电瓶容量的消息"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
print("\nOutput #5: ")
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

# 6.Pytho标准库
favorite_languages = OrderedDict()

favorite_languages['jen'] = 'python'
favorite_languages['sarah'] = 'c'
favorite_languages['edward'] = 'ruby'
favorite_languages['phil'] = 'python'

print("\nOutput #6: ")
for name, language in favorite_languages.items():
    print("{0}'s favorite language is {1}.".format(name.title(), language.title()))