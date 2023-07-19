import os
import random
import shutil

def split_data(source_folder, destination_folder, split_ratio):
    file_list = os.listdir(source_folder)
    file_list = [file for file in file_list if file.endswith('.png')]  # Filter files with .jpg extension
    random.shuffle(file_list)

    # Calculate the split point
    split_point = int(len(file_list) * split_ratio)

    # Split the files into training and testing sets
    training_files = file_list[:split_point]
    testing_files = file_list[split_point:]


    # Copy images to training folder
    for file_name in training_files:
        src = os.path.join(source_folder, file_name)
        dst = os.path.join(destination_folder, 'train', 'images', file_name)
        shutil.copy(src, dst)

        file_stem = os.path.splitext(file_name)[0] 
        new_filename = file_stem + ".jpg"
        src_mask = os.path.join(source_folder, new_filename)
        dst_mask = os.path.join(destination_folder, 'train', 'masks', new_filename)
        shutil.copy(src_mask, dst_mask)

    # Copy images to testing folder
    for file_name in testing_files:
        src = os.path.join(source_folder, file_name)
        dst = os.path.join(destination_folder, 'test', 'images', file_name)
        shutil.copy(src, dst)

        file_stem = os.path.splitext(file_name)[0] 
        new_filename = file_stem + ".jpg"
        src_mask = os.path.join(source_folder, new_filename)
        dst_mask = os.path.join(destination_folder, 'test', 'masks', new_filename)
        shutil.copy(src_mask, dst_mask)

# Specify the source folder containing the images and masks
source_folder = './orig/'

# Specify the destination folder for the split data
destination_folder = './use/'

# Specify the split ratio (e.g., 0.8 for 80% training, 0.2 for 20% testing)
split_ratio = 0.8

# Split the data
split_data(source_folder, destination_folder, split_ratio)

