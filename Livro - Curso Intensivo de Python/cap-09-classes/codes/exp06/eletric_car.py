#!/usr/bin/python3
# encoding: utf-8

from car import Car


class Battery():
	"""Uma tentativa simples de modelar uma bateria para um carro elétrico."""

	def __init__(self, battery_size=60):
		"""Inicializa os atributos de uma bateria."""
		self.battery_size = battery_size


	def describe_battery(self):
		"""Exibe uma frase que descreve a capacidade da bateria"""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")


	def get_range(self):
		"""Exibe frase sobre a distância que o carro pode percorrer com essa bateria"""

		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 85:
			range = 270
		else:
			range = 240 #Correção, sem inicializar a variável local range não funciona

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		print(message)


class EletricCar(Car):
	"""Modela aspectos de um carro específico de veículos elétricos."""

	def __init__(self, make, model, year):
		"""
		Inicializa os atributos da classe-pai.
		Em seguida, inicializa os atributos específicos de um carro elétrico.
		"""

		super().__init__(make, model, year)
		self.battery = Battery()

