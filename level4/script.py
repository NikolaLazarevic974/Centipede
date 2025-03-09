import os

# Set the keyword you want to remove here
keyword = "green"  # Change this to your keyword

# Get the directory where the script is located
current_dir = os.path.dirname(os.path.abspath(__file__)) or os.getcwd()

print(f"Scanning directory: {current_dir}")
print(f"Removing keyword: '{keyword}'")

# Counter for renamed files
renamed_count = 0

# List all files in the directory
for filename in os.listdir(current_dir):
    # Skip directories and the script itself
    if os.path.isdir(os.path.join(current_dir, filename)) or filename == os.path.basename(__file__):
        continue
    
    # Create new filename by removing the keyword
    new_filename = filename.replace(keyword, "").strip()
    
    # Skip if filename wouldn't change
    if new_filename == filename:
        continue
    
    # Construct full paths
    old_path = os.path.join(current_dir, filename)
    new_path = os.path.join(current_dir, new_filename)
    
    try:
        # Rename the file
        os.rename(old_path, new_path)
        renamed_count += 1
        print(f"Renamed: '{filename}' -> '{new_filename}'")
        
    except Exception as e:
        print(f"Error renaming '{filename}': {e}")

print(f"\nProcess complete. Renamed {renamed_count} files.")
