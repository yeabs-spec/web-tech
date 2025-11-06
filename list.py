name=['hanna','gobew','bisrat','desu','beka','67654','yt65r']
first , second , third,*forth = name#unpacking
print(forth)#^
print(third)#^
print(type(name))
print(len(name))#length of the list
print(name[5])#indexing
print(name[-5])#negative indexing
new_list = name[1:3]#slicing
print(new_list)#^
new_listt = name[-6:-3]#slicing negative indexing
print(new_listt)#^
name[5]='shakatar'#modify
print(name)
print('gobew' in name)#checking element
name.append('issac')#adding to a list
print(name)
name.insert(3,'jacob')#adding to a list by specific index
print(name)
print(name.pop())#last element in the list
new_lisst=name.copy()#copying a list
print(new_lisst)
numbers=['44','77','56','66','87','78']#joining two lists
neww_list=numbers   + name
neww_list=numbers.extend(name)
print(neww_list)
