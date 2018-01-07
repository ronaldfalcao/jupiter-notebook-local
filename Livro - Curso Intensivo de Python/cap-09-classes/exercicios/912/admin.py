#!/usr/bin/python3
# encoding: utf-8

from privileges import Privileges
from user import User

"""Classe Admin"""
class Admin(User):
    """Iniciando método da classe pai"""
    def __init__(self, first_name, last_name, user, email, password):
        super().__init__(first_name, last_name, user, email, password)
        
        
        """Atributo exclusivo da classe filha"""
        self.privileges = Privileges()

