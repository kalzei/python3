# to process strings as numbers

def abs(x):
    if type(x) is str:
        if __is_int(x): x=int(x)
        elif __is_float(x): x=float(x)
        elif 'E' in x.upper():
            num = x.upper().split('E')
            if __is_float(num[0]) and __is_int(num[1]) :
                x = float(x)
    
    if type(x) is int or type(x) is float:
        if x<0: return -x
        else: return x

def __is_int(x):
# -10  +20
    if x.strip().lstrip('-').isdigit() or \
       x.strip().lstrip('+').isdigit():
        return True
    else:
        return False

def __is_float(x):
# -10.6  +20.7
    if x.strip().lstrip('-').replace('.','',1).isdigit() or \
       x.strip().lstrip('+').replace('.','',1).isdigit():
        return True
    else:
        return False