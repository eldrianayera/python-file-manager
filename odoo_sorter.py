import os
import shutil
from pathlib import Path

# Base source directory where the oddons folders are located
base_source_dir = r"C:\ELDRIAN\Odoo17\odoo_module\Odoo modules"

# Function to ensure directories exist
def ensure_directory(path):
    Path(path).mkdir(parents=True, exist_ok=True)
    print(f"Ensured directory exists: {path}")

# Loop through the range to process each oddons folder inside numbered directories
for n in range(2, 9):  # Looping from 002 to 008
    # Set the source directory for each numbered folder (the oddons folder inside it)
    source_dir = os.path.join(base_source_dir, f"oddons-20240919T020433Z-{n:03d}", "oddons")
    
    # Set the destination directories for each version
    dest_17 = f"C:\\ELDRIAN\\Odoo17\\odoo_module\\Odoo17\\oddons-20240919T020433Z-{n:03d}"
    dest_16 = f"C:\\ELDRIAN\\Odoo16\\odoo_module\\Odoo16\\oddons-20240919T020433Z-{n:03d}"
    dest_15 = f"C:\\ELDRIAN\\Odoo15\\odoo_module\\Odoo15\\oddons-20240919T020433Z-{n:03d}"

    # Ensure destination directories exist
    for dir_path in [dest_17, dest_16, dest_15]:
        ensure_directory(dir_path)

    # Check if the source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory {source_dir} does not exist or is not accessible.")
        continue

    print(f"\nChecking contents of {source_dir}:")
    items = os.listdir(source_dir)
    print(f"Found items: {items}")

    # Counter for moved items
    moved_count = {17: 0, 16: 0, 15: 0}

    # Get all items in the source directory
    for item in items:
        source_path = os.path.join(source_dir, item)
        destination = None

        # Determine the destination based on the item name
        if "17" in item:
            destination = dest_17
            moved_count[17] += 1
        elif "16" in item:
            destination = dest_16
            moved_count[16] += 1
        elif "15" in item:
            destination = dest_15
            moved_count[15] += 1

        if destination:
            try:
                dest_path = os.path.join(destination, item)
                # Move the item to the destination
                shutil.move(source_path, dest_path)
                print(f"Moved {item} from {source_dir} to {destination}")
            except Exception as e:
                print(f"Error moving {item}: {str(e)}")
        else:
            print(f"No matching version found for {item}")

    print(f"\nMoving complete for {source_dir}!")
    print(f"Items moved to Odoo 17 folder: {moved_count[17]}")
    print(f"Items moved to Odoo 16 folder: {moved_count[16]}")
    print(f"Items moved to Odoo 15 folder: {moved_count[15]}")

# Process the additional oddons folder if needed
additional_source_dir = os.path.join(base_source_dir, "oddons")
if os.path.exists(additional_source_dir):
    print(f"\nChecking contents of {additional_source_dir}:")
    additional_items = os.listdir(additional_source_dir)
    print(f"Found items: {additional_items}")

    # Counter for moved items in the additional oddons folder
    moved_count = {17: 0, 16: 0, 15: 0}

    for item in additional_items:
        source_path = os.path.join(additional_source_dir, item)
        destination = None

        # Determine the destination based on the item name
        if "17" in item:
            destination = dest_17
            moved_count[17] += 1
        elif "16" in item:
            destination = dest_16
            moved_count[16] += 1
        elif "15" in item:
            destination = dest_15
            moved_count[15] += 1

        if destination:
            try:
                dest_path = os.path.join(destination, item)
                # Move the item to the destination
                shutil.move(source_path, dest_path)
                print(f"Moved {item} from {additional_source_dir} to {destination}")
            except Exception as e:
                print(f"Error moving {item}: {str(e)}")
        else:
            print(f"No matching version found for {item}")

    print(f"\nMoving complete for {additional_source_dir}!")
    print(f"Items moved to Odoo 17 folder: {moved_count[17]}")
    print(f"Items moved to Odoo 16 folder: {moved_count[16]}")
    print(f"Items moved to Odoo 15 folder: {moved_count[15]}")

print("\nAll moving operations complete!")
