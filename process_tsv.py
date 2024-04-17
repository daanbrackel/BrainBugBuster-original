import os
import argparse
import pandas as pd

def process_tsv(input_folder):
    for barcode_folder in os.listdir(input_folder):
        barcode_path = os.path.join(input_folder, barcode_folder)
        if os.path.isdir(barcode_path):
            for file in os.listdir(barcode_path):
                if file.endswith(".tsv") and "threshold" not in file:
                    tsv_path = os.path.join(barcode_path, file)
                    output_path = os.path.join(barcode_path, f"{barcode_folder}_processed.tsv")
                    process_file(tsv_path, output_path)

def process_file(input_file, output_file):
    data = pd.read_csv(input_file, sep='\t')
    # Select only the required columns
    processed_data = data[['abundance', 'species', 'genus']]
    processed_data.to_csv(output_file, sep='\t', index=False)

def main():
    parser = argparse.ArgumentParser(description="Process EMU output files")
    parser.add_argument("input_folder", type=str, help="Path to the folder containing barcode output folders")
    args = parser.parse_args()

    process_tsv(args.input_folder)

if __name__ == "__main__":
    main()
