import math

def prim(k):
    a = int(math.sqrt(k))
    if k == 2 or k ==3:
    	return True
    elif k%2 == 0:
    	return False
    else:
        for i in range(0,a,2):
            m=3+i
            if k%m == 0:
                return False
    return True

s = 0

for k in range(2,2000000):
	if prim(k):
		s = s+k

print s