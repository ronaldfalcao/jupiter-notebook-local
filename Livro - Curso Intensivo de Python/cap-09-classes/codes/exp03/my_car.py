#!/usr/bin/python3
# encoding: utf-8

from car import Car, EletricCar

my_beetle = Car("volkswagen", "beetle", 2016)
print(my_beetle.get_descriptive_name())


my_tesla = EletricCar("tesla", "roadster", 2016)
print(my_tesla.get_descriptive_name())
