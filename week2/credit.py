# calculate in how many years you will pay your credit loan

from tkinter.tix import InputOnly


x=float(input('credit you need:'))
y=float(input('your % rate is:'))
m=float(input('monthly payment:'))
z= float(x+(x*y)/100)
i=0
while z>m*i : 
    i=i+1
print('months for payment:',i)