#Input for bills you have
bills = input("Please enter the bills you have seperated by a comma + space (5, 10, 20, 50, 100): ")
str_list_bills = bills.split(", ")

#Make list of bills
listBills = []
for i in str_list_bills:
    listBills.append(int(i))

#Input for coins you have
coins = input("Please enter the coins you have seperated by a comma + space (0.05, 0.10, 0.25, 1, 2): ")
str_list_coins = coins.split(", ")

#Make list of coins
listCoins = []
for i in str_list_coins:
    listCoins.append(float(i))

#Create Dictionary
totalNum = {0.05: 0,
            0.10: 0,
            0.25: 0,
            1: 0,
            2: 0,
            5: 0,
            10: 0,
            20: 0,
            50: 0,
            100: 0}

#Get amount you need change for
originalAmount = 0
while (originalAmount == 0):
    originalAmount = float(input("Please enter the amount you want change for: "))

round(originalAmount, 2)
#Calculations
i = 0
currentAmount = originalAmount
while currentAmount != 0 :
    while currentAmount >= 5 :
        for i in reversed(listBills):
            if i <= currentAmount:
                currentBill = i
                numOfCurrentBill = currentAmount/currentBill
                totalNum[i] = int(numOfCurrentBill)
                currentAmount = currentAmount - (int(numOfCurrentBill) * currentBill)
                currentAmount = round(currentAmount, 2)
    while 0 < currentAmount < 5 :
        for i in reversed(listCoins):
            if i <= currentAmount:
                currentCoin = i
                numOfCurrentCoin = currentAmount/currentCoin
                totalNum[i] = int(numOfCurrentCoin)
                currentAmount = currentAmount - (int(numOfCurrentCoin) * currentCoin)
                currentAmount = round(currentAmount, 2)

#Print Function
print("Amount | Number Needed")
for i in totalNum:
    print ("$" + str(i),",",totalNum[i])
