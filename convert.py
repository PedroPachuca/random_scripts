import os
from PIL import Image

def convert_images_to_jpg(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            image = Image.open(file_path)

            # Convert image to JPEG if it's not already in JPEG format
            if image.format != 'JPEG':
                new_file_path = os.path.splitext(file_path)[0] + '.jpg'
                image.convert('RGB').save(new_file_path, 'JPEG')
                print(f"Converted file: {new_file_path}")

# Specify the folder containing the images
folder_path = './synth_to_use/'

# Convert images to JPEG format
convert_images_to_jpg(folder_path)

