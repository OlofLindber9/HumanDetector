import os
import shutil
from tqdm import tqdm

folder_path = 'E:/arbete/HumanDetectionAI/PASS_TRAIN_DATA'

def count_total_files(folder_path):
    total_files = 0
    for _, _, files in os.walk(folder_path):
        total_files += len(files)
    return total_files

total_files = count_total_files(folder_path)
with tqdm(total=total_files, desc="moving images", unit="file") as pbar:
    for root, dirs, files in os.walk(folder_path):
        # Skip the root folder itself
        if root == folder_path:
            continue
        
        for file in files:
            file_path = os.path.join(root, file)
            shutil.move(file_path, os.path.join(folder_path, file))
            pbar.update(1)
    # Remove the empty subfolder
    for dir in dirs:
        os.rmdir(os.path.join(root, dir))

print("All images have been moved to the root of PASS_TRAIN_DATA, and subfolders are now empty.")
