def z(m):
	for i in range(2,m):
		if m%i == 0:
			return False
	return True

n = 2
m = 3
while n<10002:
	if z(m):
		n = n+1
		a = m
	m = m+1

print n-1
print a