n=m=153
sum=r=0
while n>0:
    r=n%10
    sum=sum+(r*r*r)
    n=n//10
    if sum==m:
        print(m,"is an amstrong number")
    else:
        print(m,"is not amstrong number")