def knapsack(weight,values,capacity):
    ratio = [(values[i]/weight[i],values[i],weight[i]) for i in range(len(weight))]
    
    ratio.sort(reverse=True, key = lambda x:x[0])
    
    totalValue= 0;
    
    for r, values,weight in ratio:
        if capacity>=weight:
            capacity-=weight;
            totalValue+=values;
        else:
            totalValue+=r*capacity;
            break;
        
    return totalValue
    
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50

print("Maximum value:", knapsack(weights, values, capacity))