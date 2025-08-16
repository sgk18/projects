a=[]
x=int(input("\n enter no items : \n"))

#loop
for x in range(x):
   f=int(input("\n enter the item :\n"))
   a.append(f)
a.sort(reverse=True)
print("highest number:",a[0])