#Find the largest palindrome made from the product of two 3-digit numbers.

for i in range(100,1000):
	for j in range(100,1000):
		pal = str(i*j)
		if pal[::] == pal[::-1] and pal>m:
			print pal
		m = pal