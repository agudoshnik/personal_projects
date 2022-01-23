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
    check = 1
    decimal = 0
    while (binaryNum > 0):
        if check == 1 and binaryNum%10 == 1:
            decimal = decimal + 1
            check = check + 1
            binaryNum = binaryNum//10
        elif check == 2 and binaryNum%10 == 1:
            decimal = decimal + 2
            check = check + 1
            binaryNum = binaryNum//10
        elif check == 3 and binaryNum%10 == 1:
            decimal = decimal + 4
            check = check + 1
            binaryNum = binaryNum//10
        elif check == 4 and binaryNum%10 == 1:
            decimal = decimal + 8
            check = check + 1
            binaryNum = binaryNum//10
        elif check == 5 and binaryNum%10 == 1:
            decimal = decimal + 16
            check = check + 1
            binaryNum = binaryNum//10
        elif check == 6 and binaryNum%10 == 1:
            decimal = decimal + 32
            check = check + 1
            binaryNum = binaryNum//10
        elif check == 7 and binaryNum%10 == 1:
            decimal = decimal + 64
            check = check + 1
            binaryNum = binaryNum//10
        elif check == 8 and binaryNum%10 == 1:
            decimal = decimal + 128
            check = check + 1
            binaryNum = binaryNum//10
        else:
            check = check+1
            binaryNum = binaryNum//10
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
    binary = 0
    while decimal > 0:
        if decimal >= 128:
            decimal = decimal - 128
            binary = binary + 10000000
        elif decimal >= 64:
            decimal = decimal - 64
            binary = binary + 1000000
        elif decimal >= 32:
            decimal = decimal - 32
            binary = binary + 100000
        elif decimal >= 16:
            decimal = decimal - 16
            binary = binary + 10000
        elif decimal >= 8:
            decimal = decimal - 8
            binary = binary + 1000
        elif decimal >= 4:
            decimal = decimal - 4
            binary = binary + 100
        elif decimal >= 2:
            decimal = decimal - 2
            binary = binary + 10
        else:
            decimal = decimal - 1
            binary = binary + 1
    print(binary)
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
