'''
Created on 31 jul. 2019

@author: djadrigo
'''

#Calcula e imprime el producto de la serie 2x4x6x8x...x20.
n = 2
resultado = 1 
while n <= 20:
    resultado *= n
    n += 2
print(resultado)