n=int(input("enter the size of list"))
l=[]
l1=[]
num=[]
for i in range(n):
 x=input("enter the string: ");
 l.append(x)
print(l)
for i in range(len(l)):
 if i%2==0:
  print("index: ",i,"String: ",l[i])
for i in range(len(l)):
 if i%3==0:
  l[i]=l[i].upper()
print(l)
for i in range(len(l)):
 l[i]=" ".join(reversed(l[i].split()))
print(l)
for i in range(len(l)):
 for j in l[i].split():
  if(j.isdigit()):
    num.append(j)
print(num)

