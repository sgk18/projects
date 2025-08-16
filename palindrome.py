a=input("Enter the 7 letter palindrome :")

c=a[0]+a[1]+a[2]
d=a[6]+a[5]+a[4]
print("\n{} & {} \n".format(c,d))
if(c == d):
    print("this is a palandrome")
else:
    print("it is not a palandromne")