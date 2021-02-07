# -*- coding: utf-8 -*-
'''
Created on 15 may. 2019

@author: djadrigo
'''

def area(base, altura):
    area = (base*altura)/2
    return area

print("Calcular area de un triangulo")
print("¿Que base tiene el triagulo?")
base = float(input())
print("¿Que altura tiene el triagulo?")
altura = float(input())
print("El area del triangulo es: " + str(area(base, altura)))