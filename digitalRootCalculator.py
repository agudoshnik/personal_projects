def getNumber():
    while True:
      try:
        number = int(input("Enter number:"))
        if number < 0:
            print("Cannot be negative")
        else:
            break;
                
      except ValueError:
        print("Provide an integer value...")
        continue
    return number
    
def digitalRootCalculator(number):
    digitalRoot = 0
    checkedRoot = False
    
    while checkedRoot == False:
        while (number > 0): 
                digitalRoot = digitalRoot + (number%10)
                number = number//10
        if(digitalRoot > 9):
            number = digitalRoot
            digitalRoot = 0
        else:
            checkedRoot = True   
    print(digitalRoot)
    return

def main():
    number = getNumber()
    digitalRootCalculator(number)

main()
