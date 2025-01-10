def matrixChainMultiplcation(p):
    n = len(p)-1;
    m = [[0 for _ in range(n)] for _ in range(n)]
    c=[[0 for _ in range (n)] for _ in range(n)]
    for i in range(n):
        m[i][i]=0;
            
    for L in range(2,n+1):
        for i in range(n-L+1):
            j = i+L-1;
            m[i][j]= float('inf');
            for k in range (i,j):
                temp = m[i][k]+m[k+1][j]+p[i]*p[k+1]*p[j+1];
                if(temp<m[i][j]):
                    m[i][j]= temp;
                    c[i][j]= k;
    return m,c;


p=[3,4,5,2,3];

(m,c)= matrixChainMultiplcation(p);

print("M table:\n")
for i in range(len(m)):
    print(m[i]);
    
    

