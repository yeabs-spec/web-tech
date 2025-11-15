#while loop
count=1

while count < 6:
    print(count)
    count = count+1
else:
    print('the loop is done')


#for x in collection(list,dictionary,set)
sum=0
for x in range(1,10,2):#loop the odd numbers from 1 to 10
    sum=sum+x #add the odd numbers
print(sum) #print out sum

num=int(input("input a number "))#input for a number
for i in range(1,num + 1):#the num to start from 1 nd stop on the input num
    print(i*i)#printing out ths square of the numbers