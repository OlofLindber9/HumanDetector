import math
from tqdm import tqdm

# Input and output file names
input_file = 'image_urls.txt'
output_file_prefix = 'image_urls_part_'  # The output files will be named like 'image_urls_part_1.txt', etc.

# Count the total number of lines in the input file
with open(input_file, 'r') as f:
    total_lines = sum(1 for line in f)

# Calculate the number of lines for each part (1/7th)
lines_per_part = math.ceil(total_lines / 7)

# Open the input file again and split into 7 parts with a progress bar
with open(input_file, 'r') as f:
    for part in range(1, 8):  # Loop through each part (1 to 7)
        output_file = f"{output_file_prefix}{part}.txt"
        with open(output_file, 'w') as output:
            # Progress bar for each part
            with tqdm(total=lines_per_part, desc=f"Creating {output_file}", unit="line") as pbar:
                # Write lines for this part
                for _ in range(lines_per_part):
                    line = f.readline()
                    if not line:  # If there are no more lines to read, stop
                        break
                    output.write(line)
                    pbar.update(1)  # Update progress bar for each line written

        print(f"Created {output_file}")

print("All parts have been created successfully.")
