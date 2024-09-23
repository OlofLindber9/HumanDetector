#from datasets import load_dataset

#ds = load_dataset("OpenFace-CQUPT/HumanCaption-10M", cache_dir="E:/arbete/HumanDetectionAI/DATA/train/Human/DATAFROMHUGGINGFACE", split="train[:10%]")

from datasets import load_dataset
from tqdm import tqdm

# Load the dataset
ds = load_dataset("OpenFace-CQUPT/HumanCaption-10M", split='train')

# Specify the output file
output_file = 'image_urls.txt'

# Open the file in write mode
with open(output_file, 'w') as f:
    # Iterate through the dataset and write URLs to the file with progress bar
    for example in tqdm(ds, desc="Extracting URLs"):
        if 'url' in example and example['url'] is not None:
            f.write(f"{example['url']}\n")

print(f"All URLs have been written to {output_file}")
