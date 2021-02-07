# -*- coding: utf-8 -*-
'''
Created on 13 may. 2019

@author: djadrigo
'''
print("Convertir de Celsius a Fahrenheit")
print("¿Que temperatura desea cambiar?")
celsius = float(input())
fah = (9.0/5.0) * celsius + 32
print("La temperatura " + str(celsius) + "ºC es igual a " + str(fah) + "ºF")