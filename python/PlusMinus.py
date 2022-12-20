def plusMinus(arr):
    # Write your code here
    lenth = len(arr)
    
    positiveCount = 0;
    negativeCount = 0;
    zeroCount = 0;
    
    for i in range(lenth):
        if(arr[i] > 0):
            positiveCount += 1;
        elif(arr[i] < 0):
            negativeCount += 1;
        elif(arr[i] == 0):
            zeroCount += 1;
    
    # print("{0:.6f}".format((positiveCount / lenth)));
    print("%0.6f "%(positiveCount / lenth));
    print("%0.6f "%(negativeCount / lenth));
    print("%0.6f "%(zeroCount / lenth));
