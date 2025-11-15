students={'name':'hanna','age':45,'sec':'b'}
print(len(students))#length 
print(students['name'])#accesing an element
students['last_name'] = 'kebede'#adding an element
students['f_name'] = 'kebede'#adding an element
students['last_name'] = 'yakob'#updating an element
print('f_name'in students) #checking if the key is in the dictionary
students.pop('f_name')#removing items from dictionary
print(students.keys())#checking the keys of an element
