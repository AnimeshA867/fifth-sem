def floydWarshall(W,n):
    D=W;
  
    for k in range (n):
      for i in range(n):
          for j in range(n):
              if(D[i][j]>D[i][k]+D[k][j]):
                  D[i][j]=D[i][k]+D[k][j]
    return D;

W=[[0,4,11],[6,0,2],[3,float('inf'),0]]

print(floydWarshall(W,3))