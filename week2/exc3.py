x= float(input('original income:'))
y= float(input('% rate'))  
c= float(x+(x*y/100))
while c<1000000 :
    c= x+c
    if c>1000000:
        break
else: 
    print(c)
