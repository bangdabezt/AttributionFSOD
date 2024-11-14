import os
import shutil

def copy_and_rename_images(src_dir, dest_dir):
    # Create destination directory if it doesn't exist
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    # Iterate through each subfolder in the source directory
    for subfolder in os.listdir(src_dir):
        subfolder_path = os.path.join(src_dir, subfolder)
        
        # Check if it's a directory
        if os.path.isdir(subfolder_path):
            for filename in os.listdir(subfolder_path):
                # Check if the file is an image (you can add more extensions if needed)
                if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.tiff')):
                    # Generate the new name with zero-padding
                    name, ext = os.path.splitext(filename)
                    new_name = f"{subfolder}{int(name):06}{ext}"
                    
                    # Define the source and destination paths
                    src_file = os.path.join(subfolder_path, filename)
                    dest_file = os.path.join(dest_dir, new_name)
                    
                    # Copy the file to the new location with the new name
                    shutil.copy(src_file, dest_file)
                    print(f"Copied and renamed {src_file} to {dest_file}")

# Define source and destination directories
src_directory = './source'
dest_directory = './JPEGImages'
# VFA/data/attribution/COCO2017/JPEGImages
# Call the function
copy_and_rename_images(src_directory, dest_directory)
