# builds a telefonbook

contacts= {'Betty':222333,'Foteini':111333, 'Evi':333222, 'Kanelina':555444}
print('my conctacts are \n', contacts)
print('give new contact')
name= input('new name:')
name= str(name)
tel= input('new tel:')
tel= int(tel)
contacts.update({(name):tel})
print('my conctacts are: \n', contacts)
lista= list(contacts.items())
lista.sort()
print('list in alphabetical order: \n',lista) 
