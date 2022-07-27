grade= input('give your grade:')
grade= float(grade)
if grade>=5 and grade<= 10:
    print('pass')
    print('congrats')
elif grade<5 and grade>0:
    print('fail')
    print('try again')
else :
    print('wrong number')