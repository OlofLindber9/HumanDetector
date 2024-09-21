import os
import csv

folders = {
    'E:/arbete/HumanDetectionAI/PASS_TRAIN_DATA': 'E:/arbete/HumanDetectionAI/labels/PASS/PASS_TRAIN_LABELS.csv',
    'E:/arbete/HumanDetectionAI/PASS_VAL_DATA': 'E:/arbete/HumanDetectionAI/labels/PASS/PASS_VAL_LABELS.csv',
    'E:/arbete/HumanDetectionAI/PASS_TEST_DATA': 'E:/arbete/HumanDetectionAI/labels/PASS/PASS_TEST_LABELS.csv'
}

# Common data to be written for each image
common_data = [
    'imageWithNoHuman', '0', '0', '0', '0', '0',
    '0', '0', '0', '0', 'Unknown', 'Unknown'
]

for folder, csv_filename in folders.items():
    # Get list of images in the folder
    images = os.listdir(folder)
    
    # Open CSV file for writing
    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        header = [
            'ImageID', 'LabelName', 'Confidence', 'XMin', 'XMax', 'YMin', 'YMax',
            'IsOccluded', 'IsTruncated', 'IsGroupOf', 'IsDepictionOf', 'IsInsideOf',
            'GenderPresentation', 'AgePresentation'
        ]
        csv_writer.writerow(header)
        
        # Write data for each image
        for image_name in images:
            if os.path.isfile(os.path.join(folder, image_name)):
                image_id, _ = os.path.splitext(image_name)
                row = [image_id] + common_data
                csv_writer.writerow(row)
    
    print(f"CSV file '{csv_filename}' has been created with {len(images)} entries.")
