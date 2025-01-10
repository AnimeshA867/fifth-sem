def knapsack(W,w,v):
    n = len(w);
    m=[[0 for _ in range(W+1)] for _ in range(n)];
    
    for i in range(0,n):
        for wi in range(0,W+1):
            if(w[i]>wi):
                m[i][wi]=m[i-1][wi];
            else:
                m[i][wi]= max(v[i]+m[i-1][wi-w[i]],m[i-1][wi]);
    return m;

v=[2,3,3,4,4,5,7];
w=[3,5,7,4,3,9,2];
W=9;

m=knapsack(W,w,v);
for i in range(len(m)):
    print(m[i]);