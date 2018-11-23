import numpy as np
import pandas as pd
import csv
import random
import SellsGenerator

with open('firstnames.csv', 'r') as f:
    reader = csv.reader(f)
    firstnames = list(reader)


with open('lastnames.csv', 'r') as f:
    reader = csv.reader(f)
    lastnames = list(reader)

with open('DatabaseStreet.csv', 'r') as f:
    reader = csv.reader(f)
    streetnames = list(reader)

with open('DatabaseCities.csv', 'r') as f:
    reader = csv.reader(f)
    cities = list(reader)

with open('Items.csv', 'r') as f:
    reader = csv.reader(f)
    items = list(reader)

with open('Bars.csv', 'r') as f:
    reader = csv.reader(f)
    bars = list(reader)

with open('Sells.csv', 'r') as f:
    reader = csv.reader(f)
    sells = list(reader)

first = []
last = []
name = []
city = []
item = []
citylist = []
phone = []
addr = []
open_time = []
close_time = []
streetEndings = ["St", "Way", "Place", "Ave", "Rd", "Dr"]
bar = []
bar_4 = []
bar_2 = []
transaction = []
purchasers = []
barTrans = []

bar_3 = bars[1:]

for i in range(5000):
    first.append(str(random.choice(firstnames)).strip('[]').translate(str.maketrans('','', "'")))
    last.append(str(random.choice(lastnames)).strip('[]').translate(str.maketrans('','', "'")))
    addr.append((str(random.randint(1,9999)) + " " + str(random.choice(streetnames)).strip('[]').translate(str.maketrans('','', "'")))
                + " " + str(random.choice(streetEndings)))
    item.append(random.choice(items)[0])
    bar_city = random.choice(bar_3)
    bar.append(bar_city[0])
    for c in cities:
        if c[0] == bar_city[1]:
            citylist.append(c)
            break


for i in range(len(citylist)):
    city.append(citylist[i][0])
    randomArea = ""
    while(randomArea == ""):
        randomArea = random.choice(citylist[i][3:])
    phone.append(randomArea + "-" + str(random.randint(100,999)) + "-" + str(random.randint(1000,9999)))
    name.append(first[i] + " " + last[i])

new_city = []
print(citylist)
for i in range(len(citylist)):
    new_city.append(citylist[i][0])
print(new_city)

df = pd.DataFrame(
	{'Name': name,
     'City': new_city,
     'Phone': phone,
     'Address': addr
	})

df.to_csv('drinkers.csv', index = False)

df = pd.DataFrame(
	{'Drinker': name,
     'Items': item
	})

df.to_csv('likes.csv', index = False)

df = pd.DataFrame(
	{'Drinker': name,
     'Bar': bar
	})

df.to_csv('frequents.csv', index = False)



for i in range(1,20000):
    transaction.append(i)
    purchasers.append(random.choice(name))
    barTrans.append(random.choice(bar_3)[0])

df = pd.DataFrame(
    {'Transaction': transaction,
     'Drinker': purchasers,
     'Bar': barTrans
    })

df.to_csv('bills.csv', index = False)

transBought = []
itemBought = []
quantity = []
drinkersBought = []
cost = [0]*19999
tip = [0]*19999
time = []

for i in range(len(transaction)):
    count = 0
    numItems = 0
    boughtSomething = 0
    for j in range(len(sells)):
        if barTrans[i] == sells[j][0]:
            if boughtSomething == 0:
                numItems = random.randint(1,5)
                boughtSomething = 1
            else:
                numItems = random.randint(0,5)
            if numItems > 0:
                transBought.append(transaction[i])
                itemBought.append(sells[j][1])
                quantity.append(numItems)
                drinkersBought.append(purchasers[i])
                print(sells[j][2])
                cost[i] = cost[i] + numItems*float(sells[j][2])

df = pd.DataFrame(
    {'Transaction': transBought,
     'Drinker': drinkersBought,
     'Item': itemBought,
     'Quantity': quantity
    })

df.to_csv('bought.csv', index = False)

with open("Bars.csv") as csv_file:
    bar_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in bar_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            bar_2.append(row[0])
            open_time.append(row[5])
            close_time.append(row[6])
            line_count += 1
    print(f'Processed {line_count} lines.')

for i in range(len(cost)):
    cost[i] = round((cost[i] + (cost[i] * 0.07)),2)
    percent = round(random.uniform(.1,.5),2)
    tip[i] = cost[i]*percent
    cost[i] = cost[i] + tip[i]

    cost[i] = str(cost[i])
    cost[i] = cost[i][0:cost[i].find('.')+3]

    tip[i] = str(tip[i])
    tip[i] = tip[i][0:tip[i].find('.')+3]

    while True:
        hour = random.randint(0, 23)
        minute = random.randint(0, 59)

        if minute >= 0 and minute < 10:
            minute = "0" + str(minute)

        if hour >= 0 and hour < 10:
            hour = "0" + str(hour)
        trans_time = int(str(hour) + str(minute))

        j = 0
        while bar_2[j] != barTrans[i]:
            j += 1

        if trans_time < int(close_time[j]) or trans_time >= int(open_time[j]):
            time.append(str(hour) + str(minute))
            break

print(len(time))
print(len(purchasers))
print(len(transaction))
print(len(cost))
print(len(tip))

df = pd.DataFrame(
    {'Time': time,
     'Drinker': purchasers,
     'Transaction': transaction,
     'Total': cost,
     'Tip': tip
    })

df.to_csv('transaction.csv', index = False)


