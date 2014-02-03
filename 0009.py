

"""
bien chingon (incompleto)
for i in range(1,101):
    a = i*3
    b = i*4
    c = i*5
    if a+b+c == 1000:
        print a*b*c"""




for i in range(1000):
	for j in range(1000):
		for k in range(1000):
			if (i**2)+(j**2) == k**2 and i+j+k == 1000:
				print i*j*k