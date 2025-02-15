import os
import json

# File paths
docs_directory = r"C:\Users\spand\Desktop\IITMTDS PROJECT1\docs"
index_file = r"C:\Users\spand\Desktop\IITMTDS PROJECT1\docs\index.json"

# Initialize dictionary to store filenames and titles
file_index = {}

# Walk through the docs directory to find .md files
for root, dirs, files in os.walk(docs_directory):
    for file in files:
        if file.endswith(".md"):
            file_path = os.path.join(root, file)
            
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                # Look for the first H1 (#) line
                for line in lines:
                    if line.startswith("#"):
                        # Extract the title (after the '#')
                        title = line.lstrip("#").strip()
                        file_index[file] = title
                        break

# Write the index to a JSON file
with open(index_file, "w", encoding="utf-8") as json_file:
    json.dump(file_index, json_file, indent=4)

print(f"Task A6 completed: Index created at {index_file}")
