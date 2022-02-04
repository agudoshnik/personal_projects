# Find the length of a triangle if given hypotonuse and base
import math

def findLength(b,c):
    if b > c:
        a = b**2 - c**2
    else:
        a = c**2 - b**2
    a = math.sqrt(a)
    return a


def moveHashes():
    s=input()
    x=s.count("#")
    s=s.replace("#","")
    return("#"*x+s)
        
def trailingZeros(n):
    count = n
    while count > 1:
        answer = n * (n - 1)
        count = count - 1
    zeros = 0
    while answer%10 == 0:
        zeros = zeros + 1
        answer = answer//10
    return zeros

def factorial(n):
    if n == 1:
        return n
    else:
        return(n * factorial(n-1))

def fibbanoci(n):
    if n <= 1:
        return n
    else:
        return(fibbanoci(n-1)) + (fibbanoci(n-2))
     
def isPalindrom(word):
    #just reverse it, instead of traversing backwards
    reverse = word[::-1]
    if word == reverse:
        return True
    else:
        return False
def isVowel(char):
    #make a list, if in list, is a vowel easier than an or statement
    vowels = ["A","E","I","O","U"]
    if char.upper() in vowels:
        return True
    else:
        return False
def removeDuplicates1(a):
    noDups = []
    for i in a:
        if i not in noDups:
            noDups.append(i)
    
    return noDups

def removeDuplicates2(arr):
    setList = list(set(arr))
    return setList
def main():
    print(removeDuplicates2([1,1,2,3,3,2]))

main()
    
