import json

# File paths
input_file = r"C:\Users\spand\Desktop\IITMTDS PROJECT1\contacts.json"
output_file = r"C:\Users\spand\Desktop\IITMTDS PROJECT1\contacts-sorted.json"

# Read contacts from JSON file
with open(input_file, "r") as file:
    contacts = json.load(file)

# Sort contacts by last_name and first_name
sorted_contacts = sorted(contacts, key=lambda x: (x['last_name'], x['first_name']))

# Write sorted contacts to new JSON file
with open(output_file, "w") as file:
    json.dump(sorted_contacts, file, indent=4)

print(f"Task A4 completed: Contacts sorted and saved to {output_file}.")
