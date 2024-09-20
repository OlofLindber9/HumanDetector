import csv

input_csv_path = 'E:/arbete/HumanDetectionAI/labels/MIAP/open_images_extended_miap_boxes_val.csv'
output_csv_path = 'E:/arbete/HumanDetectionAI/labels/MIAP/open_images_extended_miap_boxes_val(1).csv'

def replace_labelname_in_csv(input_csv, output_csv):
    with open(input_csv, mode='r', newline='') as infile, open(output_csv, mode='w', newline='') as outfile:
        csv_reader = csv.reader(infile)
        csv_writer = csv.writer(outfile)

        header = next(csv_reader)
        csv_writer.writerow(header)

        for row in csv_reader:
            if row[1] == '/m/01g317':
                row[1] = 'imageWithHuman'
            csv_writer.writerow(row)

replace_labelname_in_csv(input_csv_path, output_csv_path)

print(f'CSV file has been updated and saved to {output_csv_path}')
