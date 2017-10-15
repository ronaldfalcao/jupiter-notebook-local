#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Regras
======
1) usar comentário docstring;
2) não usar espaços ao lado de valores default;
3) não usar espaços ao lado de argumentos nomeados;
4) linhas com 79 caracters;
5) usar duas linhas para separar funções de um mesmo módulo.

"""

def show_magicians(magicians):
"""Exibe os mágicos passados como parâmetro"""
    for magician in magicians:
        print(magician.title())
        

def make_great(magicians, change_magicians):
	"""Insere o adjetivo O Grande na lista de mágicos passada como parâmetro"""
    while magicians:
        change_magician = magicians.pop()
        change_magicians.append("O Grande " + change_magician.title())
        

def describe_city(nomeCidade, nomePais="Brasil"):
    """Exibe o nome da cidade e o país onde ela se localiza, padrão default
	   como país é Brasil
    """
    print(nomeCidade.title() + " está localizada no " + nomePais.upper())
