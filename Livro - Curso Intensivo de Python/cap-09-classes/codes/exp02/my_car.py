#!/usr/bin/python3
# encoding: utf-8

from car import EletricCar

my_tesla = EletricCar("tesla" ,"model S" ,2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()