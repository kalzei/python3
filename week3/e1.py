def isnum(n):
# tells if n is a number and gives its type
    if not type(n) is str:
        return False
 # ignore everything that isn't string
    n= n.strip()
# identify numbers
    if n.isdigit():
        return True
    elif n[0] in '-+' and isnum(n[1:]):
        return True
    else:
        return False
while True:
    n = input("n=")
    if n == '' : 
        break
    print(isnum(n))        