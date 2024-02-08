import csv
counter = 0
customers = open('customers.csv', 'r')
outfile = open('customer_country.csv', 'w')

csv_file = csv.reader(customers) 

next(csv_file)

outfile.write("Full Name, Country\n")

for line in csv_file:
    outfile.write(f'{line[1]} {line[2]}, {line[4]}\n')
    counter += 1

print(f'Total number of customers: {counter}')

customers.close()
outfile.close()