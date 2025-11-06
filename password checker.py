#password checker
password=input('enter password?')

if(password.isdigit()):
    print('false')
elif(password.isalpha()):
    print('false')
elif(password.isupper()):
    print('false')
elif(password.islower()):
    print('false')
else:
    print('true')