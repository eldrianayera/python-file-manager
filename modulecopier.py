import os
import shutil

# Paths
source_path = r'\\wsl$\Ubuntu\home\asus\odoo17\odoo17_apex\common_addons'  # Correct WSL path
dest_path = r'C:\ELDRIAN\Odoo17\odoo17_ef\user'  # Windows path

# Read folder names from the file
with open('formattedlist2.txt', 'r', encoding='utf-8') as file:
    folders_to_copy = [line.strip() for line in file if line.strip()]  # Get non-empty lines 

# Copy folders if they exist
for folder in folders_to_copy:
    full_source_path = os.path.join(source_path, folder)  # Construct full source path
    full_dest_path = os.path.join(dest_path, folder)  # Construct full destination path

    # Check if the folder exists before copying
    if os.path.exists(full_source_path):
        print(f"Copying: {full_source_path} to {full_dest_path}")
        shutil.copytree(full_source_path, full_dest_path)
    else:
        print(f"Folder does not existttttttttttttttttttttttttttttttttttttt: {full_source_path}") 


        
