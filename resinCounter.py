from datetime import datetime, timedelta  
    

#resin counter
#resin recharge is 1 resin in 8 minutes

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
resinSub = ((neededResin - currentResin) * 8)
print(resinSub,"minutes are required")

hoursNeeded =(resinSub/60)
minutesNeeded = float((resinSub/60)%1)

presentTime = datetime.now()
'{:%H:%M:%S}'.format(presentTime)

updatedTime = datetime.now() + timedelta(hours=hoursNeeded) + timedelta(minutes=minutesNeeded)
print("Your desired resin will be available at", updatedTime)
      
