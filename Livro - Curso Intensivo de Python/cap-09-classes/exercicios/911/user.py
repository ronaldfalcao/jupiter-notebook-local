#!/usr/bin/python3
# encoding: utf-8

class User:
    
    def __init__(self, first_name, last_name, user, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user = user
        self.email = email
        self.password = password
        self.login_attempts = 0
        
        
    def describe_user(self):
        print("\nDescrição do usuário")
        print("="*20)
        
        print("Nome: " + self.first_name + " " + self.last_name)
        print("Usuário: " + self.user)
        print("E-mail: " + self.email)
        print("Senha: " + self.password)
        
        
    def greet_user(self):
        print("Bem vindo(a), " + self.first_name.title() + " " + self.last_name.title() + ".\n")
        
        
    def get_login_attempts(self):
        return self.login_attempts
        
        
    def increment_login_attempts(self, attempts):
        self.login_attempts = self.login_attempts + attempts
        
        
    def reset_login_attempts(self):
        self.login_attempts = 0


"""Classe Admin"""
class Admin(User):
    """Iniciando método da classe pai"""
    def __init__(self, first_name, last_name, user, email, password):
        super().__init__(first_name, last_name, user, email, password)
        
        
        """Atributo exclusivo da classe filha"""
        self.privileges = Privileges()


"""Classe Privileges"""            
class Privileges():
    
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']
        
    
    def show_privileges(self):
        for privilege in self.privileges:
            print("- " + privilege)
