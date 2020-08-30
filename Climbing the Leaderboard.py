n=int(input())
N=list(map(int,input().split(" ")))
N=list(dict.fromkeys(N))
m=int(input())
M=list(map(int,input().split(" ")))
j=len(N)-1
for i in M:
    while(j>=0):
            if(N[j]==i):
                print(N.index(i)+1)
                break
            if(N[j]>i):
                print(j+2)
                break
            if(j==0):
                print(j+1)
                break
            j-=1
