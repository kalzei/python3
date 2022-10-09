# division with try/except
ans= ""
while ans != "stop":
    x,y= " "," "
    try:
        x=int(input("x=").strip())
        y=int(input("y=").strip())
        print("x/y={},x%y={}".format(x/y,x%y))
    except ValueError as e:
        print("give integer:\n", e)
    except ZeroDivisionError as e:
        print("zero is not correct:\n", e)
    finally :
        ans = input("continue; stop to exit:")
        if ans == "stop":
            break