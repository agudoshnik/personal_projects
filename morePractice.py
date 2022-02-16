def addOne(a):
    n = len(a)-1
    while n >= 0:
        if a[n] < 9 and n!= 0:
            a[n] = a[n] + 1
            n = 0
        elif a[n] < 9 and n == 0:
            a[n] = a[n] + 1
            return(a)
        elif a[n] >= 9:
            a[n] = 0
            n = n - 1
    return(a)

def minMaxSum(a):
    n = len(a)-1
    minSum = 0
    maxSum = 0
    i = 0
    a.sort()
    b = a[::-1]
    while i < n:
        if i%3 ==0:
            minSum = minSum + a[i]
            maxSum = maxSum + b[i]
            print(minSum + maxSum)
            minSum = 0
            maxSum = 0
            i = i + 1
        else:
            minSum = minSum + a[i]
            maxSum = maxSum + b[i]
            i = i + 1
        
    return
def moveNeg(a):
    arr = []
    for i in range(len(a)):
        if a[i] > 0:
            arr.append(a[i])
    for j in range(len(a)):
        if a[j] < 0:
            arr.append(a[j])
    return(arr)

def missingNum(a):
    a.sort()
    for i in range(len(a)):
        if a[i] + 1 != a[i+1]:
            return a[i] + 1

def missingDup(a,b):
    a.sort()
    b.sort()
    if len(a) < len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                return(b[i])
    else:
        for i in range(len(b)):
            if b[i] != a[i]:
                return(a[i])
    if len(a) < len(b):
        return b[-1]
    else:
        return a[-1]

def textFit(s,size):
    text = ""
    finaltext = ""
    i = 0
    while i < len(s):
        if len(s[i] + text) >= size:
            if len(text) < size:
                while len(text) < size:
                    text = text + " "
                finaltext = finaltext +text + "\n"
                text = ""
                    
            else:
                finaltext = finaltext + text + "\n"
                text = ""
                
        else:
            text = text + s[i] + " "
            i = i+1
    return(finaltext)
    
    
def main():

    main()
