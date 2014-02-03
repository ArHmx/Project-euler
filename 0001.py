#Find the sum of all the multiples of 3 or 5 below 1000

suma=0 
a=0
for i in range (1000):

	if a%3 == 0:
		suma=suma+a
		a=a+1
     
	elif a%5 == 0:
		suma=suma+a
		a=a+1

	else:
		a=a+1

print suma

