import csv
fields = ['Scrip', 'URL', 'BuyPrice', 'StopLoss', 'TargetPrice']  #Portfolio fields
path = input("Enter the path where you want to save your portfolio file: ")
filenam e = path + 'portfolio.csv'
print ("File saved at: " + filename)  #Show location where file will be saved.
#Add first row containing column names.
with open(filename, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(fields)


with open(filename, 'a', newline='') as file:
    writer = csv.writer(file)
    while True:
        scrip = input("Enter name of scrip: ")
        buyp = input("Enter buy price: ")
        sl = input("Enter stop loss: ")
        targetp = input("Enter target price: ")
        link = input("Enter the Moneycontrol URL for the scrip: ")
        stocklist = [scrip, link, buyp, sl, targetp]
        writer.writerow(stocklist)
        more = input("Do you want to add another scrip to the portfolio? (y/n) ")
        if (more == 'y'):
            continue
        elif (more == 'n'):
            break
        else:
            for i in range(0, 4):
                print ("Invalid choice. Please type y or n. ")
                more = input("Do you want to add another scrip to the portfolio? (y/n) ")
                if more == 'y' or more == 'n':
                    break

            break
#Print file contents.
with open(filename, 'r') as f2:
    reader = csv.reader(f2)
    for r in reader:
        print(r)
