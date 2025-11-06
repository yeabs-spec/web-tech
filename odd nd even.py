#odd nd even
def main():
    n=int(input("enter a number?"))
    if n%2==1:
        print("Weird")
        main()
    elif(n%2==0 and n>2 and n<5):
        print("Not Weird")
        main()
    elif(n%2==0 and n>6 and n<20):
        print("weird")
        main()
    elif(n%2==0 and n>20):
        print("not weird")
        main()
main()        
    