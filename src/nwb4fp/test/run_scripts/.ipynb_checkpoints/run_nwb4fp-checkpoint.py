from nwb4fp.main import main_create_nwb
import sys
from pathlib import Path

base_path = Path("Q:/Sachuriga/Sachuriga_Python")
base_data_folder = Path("S:/Sachuriga/")
project_path = fr"{base_path}/quality_metrix/"

sex = "F"
animals = ["65588"] 
age = "P45+"
species = "Mus musculus"
vedio_search_directory = base_data_folder/fr"Ephys_Vedio/CR_CA1/"
path_save = base_data_folder/fr"nwb"
temp_folder = r'C:/temp_waveform/'

main_create_nwb.run_qmnwb(animals,
                          base_data_folder,
                          sex,age,
                          species,
                          vedio_search_directory,
                          path_save,
                          temp_folder)