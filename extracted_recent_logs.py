import os

# File paths
logs_dir = r"C:\Users\spand\Desktop\IITMTDS PROJECT1\logs"
output_file = r"C:\Users\spand\Desktop\IITMTDS PROJECT1\logs-recent.txt"

# Get list of .log files in the logs directory
log_files = [f for f in os.listdir(logs_dir) if f.endswith('.log')]

# Sort log files by modification time, most recent first
log_files.sort(key=lambda f: os.path.getmtime(os.path.join(logs_dir, f)), reverse=True)

# Get the first line of the 10 most recent log files
recent_lines = []
for log_file in log_files[:10]:
    log_file_path = os.path.join(logs_dir, log_file)
    with open(log_file_path, 'r') as file:
        first_line = file.readline().strip()
        recent_lines.append(first_line)

# Write the first lines to the output file
with open(output_file, 'w') as file:
    for line in recent_lines:
        file.write(line + '\n')

print(f"Task A5 completed: First lines of the 10 most recent .log files saved to {output_file}.")
