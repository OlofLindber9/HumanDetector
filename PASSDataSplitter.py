import os
import shutil
from tqdm import tqdm

train_folder = 'E:/arbete/HumanDetectionAI/PASS_TRAIN_DATA'
val_folder = 'E:/arbete/HumanDetectionAI/PASS_VAL_DATA'
test_folder = 'E:/arbete/HumanDetectionAI/PASS_TEST_DATA'

images = os.listdir(train_folder)

# Calculate the number of images for each split
total_images = len(images)
train_count = int(total_images * 0.80)
val_count = int(total_images * 0.05)
test_count = total_images - train_count - val_count  # Remaining goes to text

# Move images to validation folder
with tqdm(total=val_count, desc="moving val images", unit="file") as pbar:
    for img in images[train_count:train_count + val_count]:
        shutil.move(os.path.join(train_folder, img), os.path.join(val_folder, img))
        pbar.update(1)

# Move images to test folder
with tqdm(total=test_count, desc="moving test images", unit="file") as pbar:
    for img in images[train_count + val_count:]:
        shutil.move(os.path.join(train_folder, img), os.path.join(test_folder, img))
        pbar.update(1)

print(f'Successfully moved images: {train_count} in TRAIN, {val_count} in VAL, {test_count} in TEST')
