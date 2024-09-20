import os
import random
import string
from tqdm import tqdm

#folders
source_folder = 'E:/arbete/HumanDetectionAI/MIAP_TEST_DATA'
target_folder = 'E:/arbete/HumanDetectionAI/PASS_DATA'

def generate_random_string(existing_names):
    while True:
        new_name = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
        if new_name not in existing_names:
            return new_name

existing_names = set([f.split('.')[0] for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))])

total_files = 0
for root, dirs, files in os.walk(target_folder):
    total_files += len(files)

with tqdm(total=total_files, desc="Renaming files", unit="file") as pbar:
    for root, dirs, files in os.walk(target_folder):
        for filename in files:
            file_extension = os.path.splitext(filename)[1]

            new_name = generate_random_string(existing_names)

            existing_names.add(new_name)

            new_filename = new_name + file_extension
            old_file_path = os.path.join(root, filename)
            new_file_path = os.path.join(root, new_filename)
            os.rename(old_file_path, new_file_path)
            
            pbar.update(1)

print('All files in all subfolders have been renamed.')