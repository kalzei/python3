#creates a % of your grade

from sys import flags


grade= input('give your grade:')
grade= float(grade)
if grade>=50 or grade<=100:
    print('welldone, you pass')
elif grade<50 or grade>0:
    print('try again')
else :
    print('wrong number')
x=grade*20/100
x=float(x)
print('your grade is:',x)



