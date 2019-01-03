from functools import reduce
l=[]
l1=[]
for i in range(6):
 x=int(input("enter number: "))
 l.append(x)
l1=[x*3 for x in l];
print(l1)
sum1=reduce(lambda a,b:a+b,l)
print("old sum ",sum1)
sum2=reduce(lambda a,b:a+b,l1)
print("new sum",sum2)
