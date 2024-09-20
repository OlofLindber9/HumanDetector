import os
import csv
from tqdm import tqdm

image_folder_path = 'E:/arbete/HumanDetectionAI/PASS_DATA'
output_csv_path = 'E:/arbete/HumanDetectionAI/labels/PASS/PASS_labels.csv'

def count_total_files(folder_path):
    total_files = 0
    for _, _, files in os.walk(folder_path):
        total_files += len(files)
    return total_files

def collect_image_files(folder_path):
    image_files = []
    total_files = count_total_files(folder_path)
    with tqdm(total=total_files, desc="Collecting Image Files", unit="file") as pbar:
        for root, _, files in os.walk(folder_path):
            for file in files:
                if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                    image_files.append(os.path.join(root, file))
                pbar.update(1)
    return image_files

def write_csv(image_files, output_csv_path):
    with open(output_csv_path, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['ImageID', 'LabelName', 'Confidence', 'XMin', 'XMax', 'YMin', 'YMax', 
                             'IsOccluded', 'IsTruncated', 'IsGroupOf', 'IsDepictionOf', 'IsInsideOf', 
                             'GenderPresentation', 'AgePresentation'])

        for image_path in tqdm(image_files, desc="Processing Images", unit="image"):
            image_id = os.path.basename(image_path).split('.')[0]
            row = [image_id, 'imageWithNoHuman', 0, 0, 0, 0, 0, 0, 0, 0, 0, 'Unknown', 'Unknown']
            csv_writer.writerow(row)

image_files = collect_image_files(image_folder_path)

write_csv(image_files, output_csv_path)

print(f'CSV file has been created at {output_csv_path}')
