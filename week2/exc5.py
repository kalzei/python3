x= input('give temperture in celsius:')
x1= x.split()
x2= [float(x) for x in x1]
print('celsious grades:', x2)
x3=[9/5 *x + 32 for x in x2]
print('grades in Fahreneit:', x3)