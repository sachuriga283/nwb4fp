# Neuroscience Data to NWB Conversion Script

This repository houses a Python script, `main_create_nwb.py`, designed to convert neuroscience data into the Neurodata Without Borders (NWB) format. It is specifically tailored for processing electrophysiology data obtained from the open ephys system and behavioral tracking data analyzed with DeepLabCut.

## Introduction

The `test_qmnwb` function facilitates the checking the manual curated sorting files and DLC file is fullfilled the next step or not. The `run_qmnwb`  function facilitates the conversion of neuroscience data into NWB format, a standardized format for neurophysiology data sharing and storage. This script is particularly useful for researchers working with data from Mus musculus, focusing on electrophysiology and behavioral data.

## Features

- **Data Conversion**: Efficiently converts electrophysiology and behavioral data into the NWB format.
- **Species and Demographic Specificity**: Optimized for data from Mus musculus, particularly targeting individuals of age P45+ and sex F.
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
