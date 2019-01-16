f=open("D:\Akhil\input.txt","r")
f1=open("D:\Akhil\weights.txt","r")
i=[int(x) for x in f.read().split()]
w=[float(x) for x in f1.read().split()]
t=0
j=0
sum=0.0
while j<5:
  sum=sum+(i[j]*w[j])
  j=j+1

print sum

f.close()
f1.close()
f2=open("D:\Akhil\output.txt","a+")
if sum > t:
   f2.write("Output is 1")
else:
   f2.write("Output is 0")

f2.close()
   
