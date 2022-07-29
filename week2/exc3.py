x= float(input('original income:'))
y= float(input('% rate'))  
c= float(x+(x*y/100))
i=0
while c<1000000 :
    i=i+1
    c= x+c
    
print('years:',i)