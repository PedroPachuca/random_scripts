import os
import fnmatch

def delete_matching_files(first_folder, second_folder):
    first_files = os.listdir(first_folder)
    second_files = os.listdir(second_folder)

    for first_file in first_files:
        first_file_stem = os.path.splitext(first_file)[0]
        matching_files = fnmatch.filter(second_files, f"{first_file_stem}*")

        for matching_file in matching_files:
            file_path = os.path.join(second_folder, matching_file)
            os.remove(file_path)
            print(f"Deleted file: {file_path}")

# Specify the folders containing the images
first_folder = './use/test/images/'
second_folder = './all/'

# Delete matching files in the second folder for each file stem in the first folder
delete_matching_files(first_folder, second_folder)

