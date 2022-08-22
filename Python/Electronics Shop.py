b = 60
keyboards = [40,50,60]
drives = [5,8,12]
def getMoneySpent(keyboards, drives, b):

    # Create a list 'sum' that contain the sum of all the two lists combination.
    # If the sum of the two elements is higher than the budget, don't append it to 'sum'
    # Sort 'sum', and take last element (highest value)
    
    sum = []
    for i in range(len(keyboards)):
        for j in range(len(drives)):
            if keyboards[i] + drives[j] <= b:
                sum.append(keyboards[i] + drives[j])
    if len(sum) !=0:
        sum.sort()
        return(sum[-1])
    else:
        return (-1)
print(getMoneySpent(keyboards, drives, b))