def setOrNot(number,n):
    mask=1
    if (n & mask)==1 or (n & mask)==0:
        if number &(n<<(n-1)):
            print("set")
        else:
            print("notset")
number = int(input("Enter a proper number: "))
n=int(input("Enter a bit position : "))
setOrNot(number,n)