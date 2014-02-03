#What is the largest prime factor of the number 600851475143

def z(m):
	for i in range(m):
		i = i+1
		return i

n = 600851475143

for i in range(10000):
	i = i+1
	m = 1
	a = i
	if a>=2 and a%z(m) == 0 and n%a == 0:
		print a
	m = m+1