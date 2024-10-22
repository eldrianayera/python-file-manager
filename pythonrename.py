import os

# Set the path to the parent directory containing Odoo folders
parent_dir = r"C:\ELDRIAN\Tutorial Videos Odoo\\[ FreeCourseWeb.com ] Udemy - Odoo Functional Implementation Guide  Accounting [En]"
for item in os.listdir(parent_dir):

    full_path = os.path.join(parent_dir, item)

    # Ensure the item is a directory before proceeding
    if os.path.isdir(full_path):

        for child in os.listdir(full_path):

            child_path = os.path.join(full_path, child)

            # Form the new name with the first character of the parent directory name followed by '.'
            new_name = item[0:1] + '.' + child
            new_path = os.path.join(full_path, new_name)

            # Check that the first character is not '1', '2', '3', or '4' (as strings)
            if child :
                os.rename(child_path, new_path)
                print(f'Successfully renamed {child} to {new_name}')
            else:
                print(f'Skipped renaming {child}, parent folder starts with {item[0]}')
    else:
        print(f'Skipped {item}, not a directory')

print("Renaming complete.")




# # List of Odoo folder names to rename
# odoo_folders = [f"Odoo{n}" for n in range(12, 18)]  # Creates a list like ['Odoo12', 'Odoo13', 'Odoo14', 'Odoo15', 'Odoo16', 'Odoo17']

# # Iterate through each folder and rename it
# for folder in odoo_folders:
#     old_path = os.path.join(parent_dir, folder)
#     new_folder_name = f"{folder}_modules"  # Append '_modules' to the folder name
#     new_path = os.path.join(parent_dir, new_folder_name)

#     # Check if the old folder exists before renaming
#     if os.path.exists(old_path):
#         os.rename(old_path, new_path)  # Rename the folder
#         print(f"Renamed: {old_path} to {new_path}")
#     else:
#         print(f"Folder does not exist: {old_path}")

# print("Renaming complete!")
