a=int(input("enter the numer :"))
c=int(a)
total=1
while(a>0):
    print(a)
    total*=a
    a=a-1
print("the {}!={}".format(c,total))