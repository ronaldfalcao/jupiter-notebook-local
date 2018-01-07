#!/usr/bin/python3
# encoding: utf-8

"""Classe Restaurante"""
class Restaurant():
    
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Método para iniciar um objeto da classe Restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served
        
        
    def describe_restaurant(self):
        """Método para mostrar as informações disponíveis do restaurante."""
        print("O restaurante " + self.restaurant_name.title() + " é especialista em " + self.cuisine_type + ".")
        
        
    def open_restaurant(self):
        """Método para mostrar se o restaurante está aberto."""
        print("O restaurante " + self.restaurant_name.title() + " encontra-se aberto!")
        
        
    def set_number_served(self, number_served):
        """Método para atualizar o valor do atributo number_served"""
        self.number_served = number_served
        
        
    def increment_number_served(self, number_served_add):
        self.number_served = self.number_served + number_served_add
        
        
"""Classe IceCreamStand"""
class IceCreamStand(Restaurant):
    
    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        
        """Iniciando a classe-pai"""
        super().__init__(restaurant_name, cuisine_type, number_served)
        
        """Iniciando atributo da classe"""
        self.flavors = ['vanilla', 'chocolate', 'cookies & cream', 'mint chocolate chip','salted caramel pretzel']
        
    def describe_flavors(self):
        print("Nossos sabores hoje são: ")
        for flavor in self.flavors:
            print("- " + flavor.title())

