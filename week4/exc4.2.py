num=""
while type(num) is str:
    num= input ("give a number:")
    try:
        num=float(num)
    except ValueError:
        print("give a new number:")
print("thank you") 
