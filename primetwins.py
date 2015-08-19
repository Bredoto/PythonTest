xmin=3
xmax=100
xold=2
def twins(x,y):
	if x-y==int(sys.argv[3]):
		print x,y
		return x,y

import sys
for x in range(int(sys.argv[1]),int(sys.argv[2])):
	for d in range(2,x+1):
		if x%d==0 and d!=x:
				break
		if d>=0.5*x:
				twins(x,xold)
				xold=x



