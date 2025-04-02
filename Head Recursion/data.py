def headrec(n, num):
    if n > num:
        return
    headrec(n + 1, num)
    print(n)

n =  int(input("Enter your number to print for n as it is pogrammed to do i guess what should i say? im just a pogram : "))

headrec(1, n)