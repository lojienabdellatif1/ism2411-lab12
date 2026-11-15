print("---exercise 2---")

import csv 
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