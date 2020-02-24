"""
Even Fibonacci numbers

"""

a = 1
b = 2
l=[1,2]
c = 3
while c < 4000000:
    l.append(c)
    a=b
    b=c
    c=a+b
s=0 
for i in range(len(l)):
    
    if l[i]%2==0:
        s+=l[i]
print(s)

     
    
    

    