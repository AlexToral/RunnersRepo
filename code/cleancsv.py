import csv

input_file = "./csv/runners.csv"
output_file = "./csv/filtered_runners.csv"

with open(input_file, mode="r", newline="", encoding="utf-8") as infile, \
     open(output_file, mode="w", newline="", encoding="utf-8") as outfile:

    reader = csv.DictReader(infile)  # Read as a dictionary using headers
    fieldnames = reader.fieldnames  # Get column names

    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()  # Write the header once

    for row in reader:
        # Skip rows that have the header values or are duplicates
        if row["Pos"] not in ["Pos", "DQ", "DNS"]:
            writer.writerow(row)

print(f"Filtered CSV saved as {output_file}")
