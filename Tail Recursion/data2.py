def tailrec(n, num):
    
    print(n)
    tailrec(n + 1, num)
    
n =  int(input("Enter your number to print for n as it is pogrammed to do i guess what should i say? im just a pogram : "))

tailrec(1, n)