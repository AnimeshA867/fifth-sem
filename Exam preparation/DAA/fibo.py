def fibo(n):
    a=0;
    b=1;
    i=2;
    while(i<n):
        c=a+b;
        a=b;
        b=c;
        print(c);
        i+=1;

    

fibo(5);
    