#!/usr/bin/python3
# encoding: utf-8

from restaurant import Restaurant

# Fazendo os testes da classe implementada...        
restaurant = Restaurant("mommy's italian cuisine", "italian food", 50)
print("Mostrando os atributos do objeto:")
print("Nome do Restaurante: " + restaurant.restaurant_name.title())
print("Tipo de cozinha: " + restaurant.cuisine_type.title())

print("\nChamando os métodos da classe")
restaurant.describe_restaurant()
restaurant.open_restaurant()