import csv
import random

cities_csv = 'DatabaseCities.csv'
bars_csv = 'Database-Bars.csv'
streets_csv = 'DatabaseStreet.csv'
output_bar_csv = 'Bars.csv'

open_hours = [1100, 1130, 1200, 1230, 1300, 1330, 1400, 1430, 1500]
close_hours = [100, 130, 200]

def shrink_arr(list, c):
    i = 0
    arr = []
    for i in range(len(list)):
        if list[i][0][0][0] == c[0] and c[0:3] != "The":
            arr.append(list[i])
        elif list[i][0][0][0] == c[4] and c[0:3] == "The":
            arr.append(list[i])

    if arr == []:
        return 'null'

    return arr


def select_random(list):
    rand = random.randrange(0,len(list))
    return list[rand]

def generate_phone(city):
    if city == 'New York City':
        return select_random(['212','332','347','646','718','917','929'])
    if city == 'Los Angeles':
        return select_random(['213','323','310','424','818','747'])
    if city == 'Chicago':
        return select_random(['312','872','773'])
    if city == 'Houston':
        return select_random(['713','281','832','346'])
    if city == 'Philadelphia':
        return select_random(['215','267','445'])
    if city == 'Phoenix':
        return select_random(['480','602','623'])
    if city == 'San Antonio':
        return select_random(['210','830','726'])
    if city == 'San Diego':
        return select_random(['619','858'])
    if city == 'Dallas':
        return select_random(['214','269','972','682'])
    if city == 'San Jose':
        return select_random(['408','669'])
    if city == 'Austin':
        return select_random(['512','737'])
    if city == 'Jacksonville':
        return select_random(['904'])
    if city == 'San Francisco':
        return select_random(['415','628'])
    if city == 'Indianapolis':
        return select_random(['417','463'])
    if city == 'Columbus':
        return select_random(['614','380'])
    if city == 'Fort Worth':
        return select_random(['682','817'])
    if city == 'Charlotte':
        return select_random(['704','980'])
    if city == 'Seattle':
        return select_random(['206'])
    if city == 'Denver':
        return select_random(['303','720'])
    if city == 'El Paso':
        return select_random(['915'])


cities = []
bars = []
streets = []
st_suffix = ['St', 'Rd', 'Ave', 'Place', 'Way', 'Blvd', 'Court', 'Circle', 'Dr']

with open(cities_csv) as csv_file:
    city_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in city_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            city = [row[0], row[2]]
            cities.append(city)
            line_count += 1
    print(f'Processed {line_count} lines.')

with open(bars_csv) as csv_file:
    bar_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in bar_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            bars.append(row[0])
            line_count += 1
    print(f'Processed {line_count} lines.')


with open(streets_csv) as csv_file:
    street_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in street_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            streets.append(row[0])
            line_count += 1
    print(f'Processed {line_count} lines.')

with open(output_bar_csv, 'w') as csv_file:
    fieldnames = ['Bar', 'City', 'License', 'Phone', 'Address', 'Open', 'Close']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    i = 0
    for i in range(len(bars)):

        shrunk_list = shrink_arr(cities, bars[i])

        if shrunk_list == 'null':
            city = select_random(cities)
        else:
            city = select_random(shrunk_list)

        bar_license = city[1] + str(random.randrange(10000,99999))
        phone = str(generate_phone(city[0])) + "-" + str(random.randrange(100,999)) + "-" + str(random.randrange(1000,9999))

        address = str(random.randrange(1, 999)) + " " + select_random(streets) + " " + select_random(st_suffix)

        open_time = open_hours[random.randrange(0,len(open_hours))]

        close_time = close_hours[random.randrange(0,len(close_hours))]

        writer.writerow({'Bar': bars[i], 'City': city[0], 'License': bar_license, 'Phone': phone, 'Address': address, 'Open': open_time, 'Close': close_time})
