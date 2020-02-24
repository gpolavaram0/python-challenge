import os
import csv

budget_data_csv = os.path.join("Instructions","PyBank","Resources", "budget_data.csv")

#print(budget_data_csv)
#print("Hello World")

#with open(budget_data_csv, newline='') as csvfile:

#with open('budget_data_csv', 'r') as budget_csv:
    

# # Method 1: Plain Reading of CSV files
budgetFile = open(budget_data_csv, 'r' )
next(csv.reader(budgetFile))
budgetReader = list(csv.reader(budgetFile))
#budgetReader = next(budgetReader)
#next(budgetReader)
monthCounter = 0
profitCounter = 0
maxProfitInc = budgetReader[0][1]
    #rec1 = budgetRead.readlines()
rowProfit = 0

prevRowVal1 = 0
prevRowVal2 = 0

ProfitInc = 0
ProfitDec = 0

maxProfitInc = 0
maxProfitDec = 0

maxProfitIncRow = ""
maxProfitDecRow = ""
   

for row in budgetReader:

    profitCounter = profitCounter + int(row[1])

    ProfitInc = int(row[1]) - prevRowVal1
    prevRowVal1 = int(row[1])

    if ProfitInc > maxProfitInc:
        maxProfitInc = ProfitInc
        maxProfitIncRow = row[0]
    elif ProfitInc < maxProfitDec:
        maxProfitDec = ProfitInc
        maxProfitDecRow = row[0]
        pass

    monthCounter += 1

changeProfit = int(budgetReader[monthCounter-1][1]) - int(budgetReader[0][1])
avgChange = changeProfit/(monthCounter-1)

PyBank_txt = open("PyBank.txt",'w')

PyBank_txt.write("Financial Analysis\n----------------------------\n")
PyBank_txt.write(f"Total Months: {monthCounter}" + "\n")
PyBank_txt.write(f"Total Profit: ${profitCounter}" + "\n")
PyBank_txt.write(f"Average  Change: ${avgChange}" + "\n")
PyBank_txt.write("Greatest Increase in Profits: " + maxProfitIncRow + " " + "($" +str(maxProfitInc) + ")")
PyBank_txt.write("\nGreatest Decrease in Profits: " + maxProfitDecRow + " " + "($" +str(maxProfitDec) + ")")

PyBank_txt.close()

print("Financial Analysis\n----------------------------")
print(f"Total Months: {monthCounter}")
print(f"Total Profit: ${profitCounter}")
print(f"Average  Change: ${avgChange}")

print("Greatest Increase in Profits: " + maxProfitIncRow + " " + "($" +str(maxProfitInc) + ")")
print("Greatest Decrease in Profits: " + maxProfitDecRow + " " + "($" +str(maxProfitDec) + ")")


