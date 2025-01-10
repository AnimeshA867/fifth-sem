def fibo(n):
    a,b,c=0,1,0;
    for _ in range(n):
        a=b;
        b=c;
        print(f"{c}\t");
        c=a+b;
        

fibo(10)