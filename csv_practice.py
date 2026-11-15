print("---exercise 2---")

import csv 
SALES_FILE= "data/sales.csv"

with open(SALES_FILE, newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)