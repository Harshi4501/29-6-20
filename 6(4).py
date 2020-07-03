l1=[3,6,9]
l2=[4,1,7]
l3=[]
x=len(l1)
for i in range(0,x):
    y=l1[i]-l2[i]
    l3.append(y)
print("the difference between two lists:",l3)