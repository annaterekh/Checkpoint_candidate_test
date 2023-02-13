def findMaxSingleDigit(numbers):
    maxNumber = -1

    for i in numbers:
        if 0 <= i <= 9:
            maxNumber = max(i, maxNumber)
    
    if maxNumber > -1:
        return maxNumber
    return None


print(findMaxSingleDigit([-5, 94, 1001, -100, 76, 1, 0, 503]))