'''
Created on 31 jul. 2019

@author: djadrigo
'''

#Calcular e imprimir la suma 50+48+46+44+...+20
n = 50
res = 0
while n >= 20:
    res += n
    n -= 2
print(res)