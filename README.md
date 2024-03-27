This repository contains a script for processing neuroscience data into NWB (Neurodata Without Borders) format. The script is designed to handle data from electrophysiology data recorded with open ephys system and behavioral track analyzed with deeplabcut.

## Introduction

The script `main_create_nwb.py` in this repository is designed to facilitate the conversion of neuroscience data into the NWB format, which is a data standard for neurophysiology. This particular script is configured to work with data from a specific experimental setup involving Mus musculus.

## Features

- Converts experimental data into NWB format.
- Handles data specifically from Mus musculus of age P45+ and sex F.
- Searches for video files in specified directories.
- Generates a CSV file for checking the processed data.

## Installation

Clone this repository to your local machine using:

```bash
git clone <repository-url>
