rows,columns=map(int, input().split()) 
values_1=[list(map(int, input().split())) for i in range(rows)] 
values_2=[list(map(int, input().split())) for i in range(rows)]
print()
for i,j in zip(values_1,values_2): 
    for k,m in zip(i,j[::-1]):  
        print(k+m,end=" ")
    print()
