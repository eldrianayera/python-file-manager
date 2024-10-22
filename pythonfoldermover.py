import os
import shutil

# Define the source and destination directories
source_dir = r"C:\ELDRIAN\Odoo17\odoo_module\Odoo modules Source"
destination_dir = r"C:\ELDRIAN\Odoo17\odoo_module\Sorted Odoo Module\OdooFiles"

# Ensure the destination directory exists
os.makedirs(destination_dir, exist_ok=True)

# Move contents from folders 001 to 008
for n in range(1, 9):
    folder_name = f"oddons-20240919T020433Z-{n:03d}"
    source_path = os.path.join(source_dir, folder_name)

    if os.path.exists(source_path):
        oddons_folder = os.path.join(source_path, "oddons")  # The oddons folder inside each numbered folder
        
        # Check if the oddons folder exists
        if os.path.exists(oddons_folder):
            # Move files inside the oddons folder
            for item in os.listdir(oddons_folder):
                item_source_path = os.path.join(oddons_folder, item)
                
                # Only move files, skip subdirectories
                if os.path.isfile(item_source_path):
                    try:
                        shutil.move(item_source_path, destination_dir)
                        print(f"Moved: {item} from {oddons_folder} to {destination_dir}")
                    except Exception as e:
                        print(f"Error moving {item}: {str(e)}")
        else:
            print(f"oddons folder does not exist: {oddons_folder}")
    else:
        print(f"Folder does not exist: {source_path}")

print("Moving complete!")
