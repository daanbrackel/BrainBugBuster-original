# FFPE_16S
multiple script to analyse sequenced 16S FFPE DNA

this repository contains all python scripts needed to process the sequenced 16S DNA from FFPE material (which leads to fragmentated 16S DNA).
The pipeline is based on EMU (https://github.com/treangenlab/emu). 
The first script is used to loop through a folder containing barcode folders containing the reads of the barcode (.fastq or .fast.gz file). this script outputs a new output folder which again contains folders of each barcode containing a abundance.tsv file.
Next script is used to create a new processed.tsv file in each of the output barcode folder which only contains the headers: abundance, species and genus.
A follow up script merges all new made processed.tsv file in one merged_dataframe.csv file which holds all information of every barcode with their abundance per species and genera. 
With the last plotting script all data can be visualized per barcode using plotly. the input is the new made merged_dataframe.csv file and the output needs to be a species.html file and a genus.html file.

# installing EMU
### create an environment for python v3.7
`conda create --name py37 python=3.7` 

`conda activate py37`

### install plotly in your py37 environment
`pip install plotly`


### Install Emu
do this in the direction you would like to install EMU in (for instance your programs folder)

`conda config --add channels defaults`

`conda config --add channels bioconda`

`conda config --add channels conda-forge`

`conda install emu`

# installing all needed scripts
install all python scripts in the same directory (preferrebly in the same programs folder were you installed EMU).

you can download the list of below scripts from this repository and upload them to your programs folder or create them yourself by using nana "file_name.py", and copy pasting the script.

- EMU_loop_script.py

- process_tsv.py

- merge_barcode_tsv.py

- plot_emu_merged.py

# running the full pipeline
- start of by running the EMU_loop_script.py script. you can do this as followed (assuming your in the program directorie where all scripts are located):

  `python EMU_loop_script.py "input_folder" "output_folder" "emu_database_dir"`

  or enter 

  `python EMU_loop_script.py --help`

  for an explenation what each in/output is.

- next run process_tsv.py:

  `python process_tsv.py "input_folder"`

  or enter 

  `python EMU_loop_script.py --help`

  for an explenation what each in/output is.

- now merge all barcodes into one dataframe:

  `python merge_barcode_tsv.py "input_folder" "output_folder"`

  or enter 

  `python merge_barcode_tsv.py --help`

  for an explenation what each in/output is.

- finally visualize all your data in a plot:

  `python plot_emu_merged.py "input_csv" "output_species.html" "output_genus.html"`

  or enter 

  `python plot_emu_merged.py --help`

  for an explenation what each in/output is.
