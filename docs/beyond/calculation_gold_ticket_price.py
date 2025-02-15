import sqlite3

# Connect to the database
db_path = r"C:\Users\spand\Desktop\IITMTDS PROJECT1\ticket-sales.db"
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Query total sales for "Gold" tickets
query = "SELECT SUM(units * price) FROM tickets WHERE type = 'Gold'"
cursor.execute(query)
total_sales = cursor.fetchone()[0]

# Close the database connection
conn.close()

# Write result to file
output_file = "/data/ticket-sales-gold.txt"
with open(output_file, "w") as file:
    file.write(str(total_sales))

print(f"Task A10 completed: Total sales for 'Gold' tickets written to {output_file}")
