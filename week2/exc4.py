# list comprenhension
print([x for x in range(1,21) if x%3==0])

# using for command
list1=[]
for i in range(1,21):
    if i%3==0 and i%2==0:
        list1.append(i)
print (list1)

# list modified 
list1= [1,3,6,9,10]
print([x+10 for x in list1 if x%2==1])