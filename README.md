# Neuroscience Data to NWB Conversion Script

This repository houses a Python script, `main_create_nwb.py`, designed to convert neuroscience data into the Neurodata Without Borders (NWB) format. It is specifically tailored for processing electrophysiology data obtained from the open ephys system and behavioral tracking data analyzed with DeepLabCut.

## Introduction

The `test_qmnwb` function facilitates the checking the manual curated sorting files and DLC file is fullfilled the next step or not. The `test_qmnwb` function will create a `4nwb_check.csv` to let you check whether or not the files are meeting the requirement. The `run_qmnwb`  function facilitates the conversion of neuroscience data into NWB format, a standardized format for neurophysiology data sharing and storage. This script is particularly useful for researchers working with data from Mus musculus, focusing on electrophysiology and behavioral data.  The `run_qmnwb` will read all the phy output ended with `phy_k` folder under each individual animals, and select the curated `good` units to calculate the qualyty metrix using python package `spikeinterface` built-in function and create a new phy output folder ended with `phy_k_manual` to preparing for the conversion to `.nwb` file.

## Features

- **Data Conversion**: Efficiently converts electrophysiology and behavioral data into the NWB format.
- **Species and Demographic Specificity**: required by 'nwbpy'.
- **Video File Handling**: Automatically searches and processes video files from specified directories, integrating them with the NWB dataset.
- **Data Verification**: Generates a CSV file post-conversion, allowing users to verify the processed data's integrity and completeness.

## Installation

To use this script, you need to clone this repository and install the required Python package, `nwb4fp`.

### Cloning the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <https://github.com/sachuriga283/QuattrocoloLab2nwb-nwb4fp.git>
cd ./QuattrocoloLab2nwb-nwb4fp
pip install requirements.txt
```

### Install with pipy
```bash
pip install nwb4fp
```
or create a condda env and install (recommended)
```bash
conda create -n nwb4fp -y python
conda activate nwb4fp
pip install nwb4fp
```

### usage (example custom python file for running the nwb4fp)
```bash

from nwb4fp.main.main_create_nwb import run_qmnwb,test_qmnwb
from pathlib import Path
import pandas as pd

def main():
    import os
    import sys

    base_data_folder = Path("base folder")
    vedio_search_directory = base_data_folder/fr"Video_folder/project_name/"
    path_save = base_data_folder/fr"nwb"
    #temp folder to save temporally created waveform folder from spikeinterface
    temp_folder = Path(r'C:/temp_waveform/')
    save_path_test=(r"Your prefered saving path/4nwb_check.csv")
    ## The function will copy the videos to the deeplabcut video folder, which were analyzed by older Deeplabcut models
    idun_vedio_path=r"P:/Overlap_project/data/CR_implant_add_new"

    sex = "F" # or "M"
    ## animals name for now only support 5 numbers str, for example here listed 6 animals
    animals = ["33331", "33332", "33333", "33334", "33335", "33336"]
    ## animals ages for first recording day
    age = "P45+"
    species = "Mus musculus"

    test_qmnwb(animals,
               base_data_folder,
               temp_folder,
               save_path_test,
               vedio_search_directory,
               idun_vedio_path=idun_vedio_path)

    ## check the 4nwb_check.csv file whether all the files (phy output and dlc .h5 file) is there and whether the file is competble to process quality metrix or not
    while True:
    user_input = input("Press 'c' to continue or 'q' to quit: ").strip().lower()
    if user_input == 'c':
        print("Continuing...")
        continue  # This will continue the loop
    elif user_input == 'q':
        print("Quitting...")
        break  # This will break out of the loop
    else:
        print("Invalid input. Please press 'c' to continue or 'q' to quit.")

    ## conversionning the data to nwb format
    run_qmnwb(animals,
              base_data_folder,
              sex,age,
              species,
              vedio_search_directory,
              path_save,
              temp_folder)

if __name__ == "__main__":
    main()
```
