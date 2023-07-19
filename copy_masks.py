import os
import shutil

def copy_files_with_matching_stem(source_folder, target_folder, extension_folder):
    source_files = os.listdir(source_folder)
    target_files = os.listdir(target_folder)

    for source_file in source_files:
        true_stem = os.path.splitext(source_file)[0]
        source_file_stem = source_file[:-11]
        target_file = f"{source_file_stem}.png"
        print("working on " + source_file_stem)
        print("target file is " + target_file)

        if target_file in target_files:
            source_path = os.path.join(source_folder, source_file)
            target_path = os.path.join(target_folder, target_file)
            destination_path = os.path.join(extension_folder, true_stem + ".png")
            shutil.copy(target_path, destination_path)
            print(f"Copied file: {destination_path}")

# Specify the folders containing the files
source_folder = './curated_synth/'
target_folder = './orig/'
extension_folder = './chosen/'

# Copy files with matching file stems and rename them
copy_files_with_matching_stem(source_folder, target_folder, extension_folder)

