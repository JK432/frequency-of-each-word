# Write a program to count the frequencies of each word from a file 
o=open("file1.txt","r")
r=[]
r=o.read().split()
m={}
for i in r:
  count=0
  for x in r:
    if(x==i):
      count=count+1

  
  m[i]=count
print(m)
