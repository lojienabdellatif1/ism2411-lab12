print("---exercise 2---")

import csv 
from datetime import datetime
SALES_FILE= "data/sales.csv"

with open(SALES_FILE, newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print("---exercise 3---")
#skips the header row 
with open(SALES_FILE, newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)

print("---exercise 4---")
#computing totals and skipping the header 
total_revenue = 0

with open(SALES_FILE, newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        line_total = price * quantity
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
        total_revenue += line_total

print(f"Total revenue: ${total_revenue:.2f}")

print("---exercise 5---")
#filtering and writing 
CLEANED_FILE = "data/cleaned.csv" #imputting file for writing 
original_count = 0
written_count = 0

with open(SALES_FILE, newline="") as infile, open(CLEANED_FILE, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile) #create csv.writer for the output file 

    writer.writerow(["Product", "Price", "Qty", "Total"]) #writing updated headers 
    next(reader)

    for row in reader:
        original_count += 1
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        total = price * quantity

        if total > 100:
            writer.writerow([product, f"{price:.2f}", quantity, f"{total:.2f}"])
            written_count += 1

print(f"Rows in original: {original_count}")
print(f"Rows written to cleaned.csv: {written_count}")

print("---exercise 6---")
#using DictReader for bigger data sets practice 
dict_total = 0

with open(SALES_FILE, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        line_total = price * quantity
        print(f"{product}: {quantity} units × ${price:.2f} = ${line_total:.2f}")
        dict_total += line_total

print(f"Total revenue: ${dict_total:.2f}")

print("---exercise 7---")
#sales summary by product 
summary = {} 

with open(SALES_FILE, newline="") as f:
    reader = csv.DictReader(f) # reads the file with DictReader and computes line_total for each row 
    for row in reader:
        product = row["product"]
        line_total = float(row["price"]) * int(row["quantity"]) # if the product is already a key it continues, if not it starts at 0
        summary[product] = summary.get(product, 0) + line_total #gives the names in alphabetical order and prints the total revenue for each product

for product in sorted(summary):
    print(f"{product}: ${summary[product]:.2f}")

print("---exercise 8---")
#using append mode log
dict_total = 0
LOG_FILE = "data/run_log.txt"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(LOG_FILE, "a") as log:
    log.write(f"{timestamp} - Total revenue: ${dict_total:.2f}\n")

print(f"Logged run to {LOG_FILE}")
