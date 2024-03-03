from pathlib import Path
import string
import sys
base_path = Path("Q:/Sachuriga/Sachuriga_Python")
base_data_folder = Path("S:/Sachuriga/")
project_path = fr"{base_path}/quality_metrix/"
sys.path.append(fr"{project_path}/quality_metrix")

# change to project root
sys.path.append(project_path)

from preprocess.load_data import load_data
from postprocess.quality_metrix import qualitymetrix
from postprocess.nwbPHYnOPHYS import nwbPHYnOPHYS
from postprocess.add_wfcor import add_wf_cor
# set params for nwb

sex = "F"
animals = ["65409", "65410"] 
age = "P45+"
species = "Mus musculus"
vedio_search_directory = base_data_folder/fr"Ephys_Vedio/CR_CA1/"
path_save = base_data_folder/fr"nwb"

def main():
    for indvi in animals:
        ID = indvi
        counter = 0
        #getting sorted files02
        folder_path = fr"{str(base_data_folder)}/Ephys_Recording/CR_CA1/{ID}/"
        ##for quality metrix
        sorted_files = load_data(folder_path, file_suffix='_phy_k')

        for file in sorted_files:
            print(file)
            qualitymetrix(file)
            add_wf_cor(fr"{file}_manual")
            nwbPHYnOPHYS(fr"{file}_manual",
                        sex,
                        age,
                        species,
                        vedio_search_directory,
                        path_to_save_nwbfile = path_save)
            counter += 1
            percent = counter/len(sorted_files)
            print(f"{percent} % completet!!!!{file}\ncreated new phy folder {file}_manual \ncreated nwb file at {path_save}for {ID} {age} {species}\n\n\n\n")

if __name__== "__main__":
    main()