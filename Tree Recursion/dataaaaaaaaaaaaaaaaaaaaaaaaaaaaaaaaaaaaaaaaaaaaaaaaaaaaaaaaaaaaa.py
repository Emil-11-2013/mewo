def incdec(n,num):
    if(n<1 or n>num):
         return
    print(n)
    incdec(n-1,num)
    print(n)

n =int(input("Enter your number to print for n as it is pogrammed to do i guess what should i say? im just a pogram : "))
incdec(n,n)