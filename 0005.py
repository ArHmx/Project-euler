#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20.

l = [2,3,5,7,11,13,17,19]
p = [11,13,14,15,16,17,18,19,20]
m = []
for i in p:
	for j in l:
		if i%j == 0:
			m.append(j)
del m[-1]
print m