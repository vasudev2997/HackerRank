l,c,max=[],0,0
n,m=map(int,input().split(" "))
for i in range(n):
    l.append(input())
for i in range(n):
    for j in range(i+1,n):
        sum=str(int(l[i])+int(l[j]))
        ones=sum.count('1')
        twos=sum.count('2')
        if(ones+twos>max):
            max=ones+twos
            c=1
        elif(ones+twos==max):
            c+=1
print(max); print(c)
