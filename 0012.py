def TrianNum(term):
	sum = 0
	l = []
	for i in range(term):
		i += 1
		sum += i
		l.append(sum)
	return l[-1]

m = 0
p = []

while True:
	m += 1
	for i in range((TrianNum(m))):
		i += 1
		if TrianNum(m)%i == 0:
			try:
				p.index(i)
			except:
				p.append(i)
	if len(p) > 500:
		break
	else:
		p = []

print TrianNum(m)