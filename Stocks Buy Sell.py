# Program to find the max profit you can get from buying and selling stocks. You are given an array with stocks price for seven days, and you can buy and sell any day.
def Calculate(a,asize):
    profit=0
    for i in range (1,asize):
        #if the current element is greater then the last element then we will buy the previous day and sell the current day.
        if a[i]>a[i-1]:
            profit+=a[i]-a[i-1]
    return profit
# prices for 7 days
prices=[623,765,143,99,278,736,342]
profit=Calculate(prices,len(prices))
print("Your profit is",profit)