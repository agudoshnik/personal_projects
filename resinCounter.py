from datetime import datetime, timedelta  
    

#resin counter
#resin recharge is 1 resin in 8 minutes
def getResin():
    #input current Resin
    while True:
      try:
        currentResin = int(input("Enter current amount of resin:"))
        neededResin = int(input("Enter needed amount of resin:"))
        if currentResin > neededResin:
            print("Current resin can not be more than needed")
        elif neededResin < 0 or neededResin > 160:
            print("Needed resin can not be negative or more than the resin cap")
        elif currentResin < 0 or currentResin > 160:
            print("Current resin can not be negative or more than the resin cap")
        else:
            break;
                
      except ValueError:
        print("Provide an integer value...")
        continue
    return (currentResin,neededResin)

#the calculations for the resin
def calculateMinutes(currentResin,neededResin):
    #how much resin will I need and how many minutes will that take
    resinSub = ((neededResin - currentResin) * 8)
    print(resinSub,"minutes are required")
    return resinSub

def calculateTime(resinSub):
    #convert the minutes into hours for better understanding
    hoursNeeded =int(resinSub/60)
    #minutes are taken from the decimal and changed from 100 time to 60 time
    minutesNeeded = float(((resinSub/60)%1)*(60/1))
    #add it to the current time
    presentTime = datetime.now()
    '{:%H:%M:%S}'.format(presentTime)
    updatedTime = datetime.now() + timedelta(hours=hoursNeeded) + timedelta(minutes=minutesNeeded)
    print("Your desired resin will be available at", updatedTime)
    return

def main():
    currentResin,neededResin = getResin()
    resinSub = calculateMinutes(currentResin,neededResin)
    calculateTime(resinSub)
main()
      
