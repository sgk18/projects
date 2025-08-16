a=[]
x=int(input("\n enter no items : \n"))

#loop
for x in range(x):
   f=int(input("\n enter the item :\n"))
   a.append(f)
#normal list
print("normal list:\n",a)
#reverse list
c=a[::-1] 
print("reverse list:\n",c)
#sorted list
a.sort()
print("sorted list :\n",a)

#sorted list(reverse)
a.sort(reverse=True)
print( "decsecding list:\n",a)
