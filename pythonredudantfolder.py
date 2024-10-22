import os
import shutil

# Iterate through folders from 001 to 008
for n in range(1, 9):
    # Set the path to the main directory (where the redundant directory might exist)
    parent_dir_17 = f"C:\\ELDRIAN\\Odoo17\\odoo_module\\Sorted Odoo Module\\Odoo17"
    parent_dir_16 = f"C:\\ELDRIAN\\Odoo17\\odoo_module\\Sorted Odoo Module\\Odoo16"
    parent_dir_15 = f"C:\\ELDRIAN\\Odoo17\\odoo_module\\Sorted Odoo Module\\Odoo15"

    # Check if redundant directory exists inside each main directory
    inner_dir_17 = os.path.join(parent_dir_17, f"oddons-20240919T020433Z-{n:03d}")
    inner_dir_16 = os.path.join(parent_dir_16, f"oddons-20240919T020433Z-{n:03d}")
    inner_dir_15 = os.path.join(parent_dir_15, f"oddons-20240919T020433Z-{n:03d}")
   

    # Function to move contents and remove inner directory
    def fix_directory_structure(parent_dir, inner_dir):
        if os.path.exists(inner_dir):
            # Move all files and folders from the inner directory to the parent directory
            for item in os.listdir(inner_dir):
                source_path = os.path.join(inner_dir, item)
                dest_path = os.path.join(parent_dir, item)
                try:
                    shutil.move(source_path, dest_path)
                except Exception as e:
                    print(f"Error moving {item}: {e}")
            
            # Remove the now empty inner directory
            try:
                os.rmdir(inner_dir)
                print(f"Removed redundant directory: {inner_dir}")
            except Exception as e:
                print(f"Error removing directory {inner_dir}: {e}")
        else:
            print(f"No redundant directory found in: {parent_dir}")

    # Fix structure for Odoo16 and Odoo15
    fix_directory_structure(parent_dir_17, inner_dir_17)
    fix_directory_structure(parent_dir_16, inner_dir_16)
    fix_directory_structure(parent_dir_15, inner_dir_15)

print("Directory structure fix complete!")
