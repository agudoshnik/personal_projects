def getBinary():
    while True:
      try:
        numberCheck = True
        binaryNum = int(input("Enter number:"))
        binarySave = binaryNum
        while (binarySave > 0):
            if(binarySave%10 != 0 and binarySave%10 != 1):
                numberCheck = False
                binarySave = binarySave//10
            else:
                binarySave = binarySave//10

        if binaryNum < 0:
            print("Cannot be negative")
        elif binaryNum > 11111111:
            print("Cannot be more than max")
        elif numberCheck == False:
            print("Not a binary value")

        else:
            break;

      except ValueError:
        print("Provide an integer value...")
        continue
    return binaryNum

def binToDec(binaryNum):
    check = 0
    decimal = 0
    while binaryNum > 0:
        if binaryNum%10 == 1:
            decimal = decimal + (2**check)
            check = check + 1
            binaryNum = binaryNum // 10
        else:
            check = check + 1
            binaryNum = binaryNum // 10
    print(decimal)
    return


def getDecimal():
    while True:
      try:
        decimalNum = int(input("Enter number:"))
        if decimalNum < 0:
            print("Cannot be negative")
        elif decimalNum > 255:
            print("Cannot be more than max")

        else:
            break;

      except ValueError:
        print("Provide an integer value...")
        continue
    return decimalNum

def decToBin(decimal):
    print(bin(decimal).replace("0b", ""))
    return 

def main():
    while True:
      try:
        print("Please select 1 if you would like to convert from Binary to Decimal")
        print("Please select 2 if you would like to convert from Decimal to Binary")
        print("Please select 3 to stop the program")
        response = int(input("Enter number:"))
        if response == 1:
            binaryNum = getBinary()
            binToDec(binaryNum)
        elif response == 2:
            decimalNum = getDecimal()
            decToBin(decimalNum)
        elif response == 3:
            break;
        elif response > 3 or response < 0:
            print("Not a valid answer")
        else:
            break;

      except ValueError:
        print("Provide an integer value...")
        continue
    return 


main()
