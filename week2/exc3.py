x= float(input('original income:'))
y= float(input('% rate'))  
c= float(x+(x*y/100))
while() :
    if c<1000000:
        continue
    if c>1000000:
        break
    c=x+c
else: 
    print(c)
