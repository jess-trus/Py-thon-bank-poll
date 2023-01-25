import os

import csv


months= 0
revenue = 0
last_revenue = 0
changes= 0
change_list=[]


csvpath = os.path.join(".", "PyBank", "Resources", "budget_data.csv")

with open(csvpath) as csvfile:
    csvreader= csv.DictReader(csvfile,delimiter=",")
    
    index=0
    for row in csvreader:
        months= months + 1
        revenue= revenue + int(row["Profit/Losses"])
        if (index==0):
            last_revenue=int(row["Profit/Losses"])
            index+=1
        changes=int(row["Profit/Losses"]) - last_revenue
        change_list.append(changes)
        last_revenue=int(row["Profit/Losses"])


        

print(months)
print(revenue)
Average_change=round(sum(change_list)/(len(change_list)-1))
max_value=max(change_list)

min_value=min(change_list)


max_month=change_list.index(max_value)+1

output=(
    f"\nFinancial Analysis\n"
    f"-------------------------\n"
    f"Total Months: {months}\n"
    f"Total: ${revenue}\n"
    f"Average Change: ${Average_change}\n"
    f"Greatest Increase in Profits: ${max_value}\n"
    f"Greatest Decrease in Profits: ${min_value}\n"
)

print(output)

with open('Budget.analysis.txt', "w") as txt_file:
    txt_file.write(output)

1









    
    


        
        




    

