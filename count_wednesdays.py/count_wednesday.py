from datetime import datetime

# File paths
input_file = r"C:\Users\spand\Desktop\IITMTDS PROJECT1\dates.txt"
output_file = r"C:\Users\spand\Desktop\IITMTDS PROJECT1\dates-wednesdays.txt"

# Function to try different date formats
def parse_date(date_str):
    formats = [
        "%Y-%m-%d",           # e.g., 2007-01-07
        "%b %d, %Y",          # e.g., Oct 03, 2012
        "%Y/%m/%d %H:%M:%S",  # e.g., 2023/02/18 05:08:46
        "%d-%b-%Y",           # e.g., 02-Mar-2011
        "%d-%b-%Y %H:%M:%S",  # e.g., 21-Jun-2015 22:35:31
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str.strip(), fmt)
        except ValueError:
            continue
    raise ValueError(f"Unrecognized date format: {date_str}")

# Read dates from file
with open(input_file, "r") as file:
    dates = file.readlines()

# Count Wednesdays
wednesday_count = 0
for date in dates:
    try:
        parsed_date = parse_date(date)
        if parsed_date.weekday() == 2:  # Wednesday
            wednesday_count += 1
    except ValueError as e:
        print(f"Skipping invalid date: {date.strip()} - {e}")

# Write count to file
with open(output_file, "w") as file:
    file.write(str(wednesday_count))

print(f"Task A3 completed: Found {wednesday_count} Wednesdays.")
