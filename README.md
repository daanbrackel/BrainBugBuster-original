# FFPE_16S
multiple script to analyse sequenced 16S FFPE DNA

this repository contains all python scripts needed to process the sequenced 16S DNA from FFPE material (which leads to fragmentated 16S DNA).
The pipeline is based on EMU (https://github.com/treangenlab/emu). 
The first script is used to loop through a folder containing barcode folders containing the reads of the barcode (.fastq or .fast.gz file). this script outputs a new output folder which again contains folders of each barcode containing a abundance.tsv file.
Next script is used to create a new processed.tsv file in each of the output barcode folder which only contains the headers: abundance, species and genus.
A follow up script merges all new made processed.tsv file in one merged_dataframe.csv file which holds all information of every barcode with their abundance per species and genera. 
With the last plotting script all data can be visualized per barcode using plotly. the input is the new made merged_dataframe.csv file and the output needs to be a species.html file and a genus.html file.
