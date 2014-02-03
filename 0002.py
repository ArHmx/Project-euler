#Find the sum of the even-valued terms (Fibonacci)

c = 1
a = 0
b = 0
s = 0

for i in range(32):
	a = c
	c = a + b
	b = a

	if c%2 == 0:
		s = s + c
 
print s