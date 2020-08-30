stack=[]
open=['{','[','(']
close=['}',']',')']
n=int(input())
for _ in range(n):
    stack.clear()
    l=input()
    if(l[0] not in close):
        for k in l:
            if(k in open):
                stack.append(k)
            elif(k in close and len(stack)>0):
                if(open.index(stack.pop())==close.index(k)):
                    flag=1
                else:
                    flag=0
                    break
        else:
            if(not stack):
                print("YES")
            else:
                print("NO")
    else:
        print("NO")       
