def multiplicar(a, b):
	result = 0;
	for i in range(1, b+1):
		result = result + a
	return result

a = 2
b = 8

print(multiplicar(a, b))
