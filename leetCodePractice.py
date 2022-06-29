#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

def listAnswer(nums[],target):
    answer = []
    numReached = False
    j = 1
    i = 0
    while numReached == False:
        if (j >= len(nums)):
            j = i
            i = i + 1
        elif (nums[i] + nums[j]) == target:
            answer.append(i)
            answer.append(j)
            numReached = True
        else:
            j = j+1
#Given a string s, find the length of the longest substring without repeating characters.
def longestSub(s):
    letters = []
    total = 0
    compare = 0
    for i in s:
        if i not in letters:
            letters.append(i)
            compare = compare + 1
        elif i in letters:
            if compare > total:
                total = compare
            compare = 0
            letters.clear()
    print(total)

def reverseNum(x):
    negative = False
    if x < 0:
        negative = True
        x = x * -1
    strx = str(x)
    stry = strx[::-1]
    answer = int(stry)
    if negative == True:
        answer = answer * -1
    print(answer)
