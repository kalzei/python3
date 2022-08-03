import math
def ypot(a,b):
    if (type(a) is int or type(a) is float) and \
        (type(b) is int or type(b) is float):
        return math.sqrt(math.pow(a,2)+ math.pow(b,2))
    else:
        return False
print('ypotinousa:',ypot(3,4))