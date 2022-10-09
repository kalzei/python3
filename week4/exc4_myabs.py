import myabs

while True:
    num= input('give number:')
    if num == '':break
    num= myabs.abs(num)
    if num:
        print('absolut:{}'.format(num))
    else :
        print ('no number')

