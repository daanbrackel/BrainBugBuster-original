import os
import pandas as pd
import argparse

def merge_processed_tsv_files(input_folder):
    dfs = []
    for root, dirs, files in os.walk(input_folder):
        for folder in dirs:
            barcode_folder_path = os.path.join(root, folder)
            for file in os.listdir(barcode_folder_path):
                if file.endswith("output_processed.tsv"):
                    tsv_file_path = os.path.join(barcode_folder_path, file)
                    df = pd.read_csv(tsv_file_path, sep='\t')
                    df['Barcode'] = folder
                    dfs.append(df)
                    break  # Stop after finding the first matching file
    merged_df = pd.concat(dfs, ignore_index=True)
    return merged_df

def save_merged_dataframe(merged_dataframe, output_file):
    merged_dataframe.to_csv(output_file, index=False)
    print("Merged dataframe saved as '{}'.".format(output_file))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge processed TSV files and save as CSV")
    parser.add_argument("input_folder", type=str, help="Path to the folder containing barcode_output folder with the processed TSV files")
    parser.add_argument("output_file", type=str, help="Path to save the merged CSV file (advised to keep in the same folder were all barcode_output folders can be found)")
    args = parser.parse_args()

    merged_dataframe = merge_processed_tsv_files(args.input_folder)
    save_merged_dataframe(merged_dataframe, args.output_file)
