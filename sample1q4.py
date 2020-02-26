import math 
d=list(map(int,input().split()))
c=50
h=30
e=[]
for i in d:
	q=pow((2*c*i/h),0.5)
	e.append(q)
print(e)

