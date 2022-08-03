import math
pi = math.pi
def area(r):
    # function for sphere's area
    return 4*pi*r**2

def vol(r):
    # function for sphere's volume
    return (4/3)*pi*r**3
def isnum(n):
    # check n=number
    if not type(n) is str :
        return False
    n = n.strip()
    if n.isdigit():
        return True
    elif n[0] in '+-' and isnum(n[1:]):
        return True
    elif "." in n:
        if n.count(".") == 1 and isnum(n.replace(".","")):
            return True
        else:
            return False
    else:
        return False
while True:
    r = input("R=")
    if r == 'stop' or r == '' : break
    if isnum(r):
        v = vol(float(r))
        e = area(float(r))
        print("area={:1.2f}, volume={:1.2f}".format(e,v))
    else:
        continue     