a=[[1,2,3],
   [1,2,3],
   [1,2,3]]

b=[[1,2,3],
   [1,2,3],
   [1,2,3]]

result=[[0,0,0],
   [0,0,0],
   [0,0,0]]

for i in range(len(a)):
    for j in range(len(a[0])):
       result[i][j]=a[i][j]+b[i][j]

for r in result:
    print(r)