#No. divisible by 7 & not a multiple of 5
l=[x for x in range(2000,3201) if x%7==0 if (x%5)!=0]
print(l)

