import csv
import random
import BarCity

items_csv = 'ItemsPrices.csv'
bars_csv ='Bars.csv'

big_cities = ['New York City', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
med_cities = ['Phoenix', 'San Antonio', 'San Diego', 'Dallas', 'San Jose', 'Austin', 'Jacksonville', 'San Francisco']
small_cities = ['Indianapolis', 'Columbus', 'Fort Worth', 'Charlotte', 'Seattle', 'Denver', 'El Paso']

bars = []
items = []
sells = []

items_per_bar = 15

def select_random(list):
    rand = random.randrange(0,len(list))
    return list[rand]

with open(items_csv) as csv_file:
    item_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in item_reader:
        items.append(row)
        line_count += 1
        print(row[0])

ite = len(items)

with open(bars_csv) as csv_file:
    bar_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in bar_reader:
        bars.append(row)

        i = 0
        used = []
  #      sells[0]
        while i < items_per_bar-5:
            rand = random.randrange(0, 30)
            if rand in used:
                print(':(')
            else:
                used.append(rand)
                sells.append([row[0],row[1],items[rand][0],items[rand][1],items[rand][2]])
                i += 1

        if row[1] in med_cities:
            i = 0
            #      sells[0]
            while i < 5:
                rand = random.randrange(0, 30)
                if rand in used:
                    print(':(')
                else:
                    used.append(rand)
                    sells.append([row[0], row[1], items[rand][0], items[rand][1], items[rand][2]])
                    i += 1
        elif row[1] in big_cities:
            i = 0
            #      sells[0]
            while i < 5:
                rand = random.randrange(39, 47)
                if rand in used:
                    print(':(')
                else:
                    used.append(rand)
                    sells.append([row[0], row[1], items[rand][0], items[rand][1], items[rand][2]])
                    i += 1
        elif row[1] in small_cities:
            i = 0
            #      sells[0]
            while i < 5:
                rand = random.randrange(30, 39)
                if rand in used:
                    print(':(')
                else:
                    used.append(rand)
                    sells.append([row[0], row[1], items[rand][0], items[rand][1], items[rand][2]])
                    i += 1
        line_count += 1
        print("test"+row[1])



for i in sells:
    price = 4;
    if i[1] in big_cities:
        i[price] = float(i[price]) + 3.0

    if i[1] in med_cities:
        i[price] = float(i[price]) + 1.0

    if i[1] in small_cities:
        i[price] = float(i[price])


    print(i)


with open('Sells.csv', 'w') as csv_file:
    fieldnames = ['Bar', 'Item', 'Price']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)


    i = 0
    while i < len(sells):
        writer.writerow({'Bar': sells[i][0], 'Item': sells[i][2], 'Price': sells[i][4]})
        i += 1


