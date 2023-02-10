x=int(input("enter a number"))
for y in range(2,x):
     if(x%y)!=0:
        z=1
     else:
        z=0
if z==1:
    print("x is prime number")
else:
    print("x is not prime number")

