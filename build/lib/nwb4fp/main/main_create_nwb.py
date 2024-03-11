from pathlib import Path
import string
import sys
from nwb4fp.preprocess.load_data import load_data
from nwb4fp.postprocess.quality_metrix import qualitymetrix
from nwb4fp.postprocess.nwbPHYnOPHYS import nwbPHYnOPHYS
from nwb4fp.postprocess.add_wfcor import add_wf_cor

def main():
    from pathlib import Path
    import string
    import sys
    from nwb4fp.preprocess.load_data import load_data
    from nwb4fp.postprocess.quality_metrix import qualitymetrix
    from nwb4fp.postprocess.nwbPHYnOPHYS import nwbPHYnOPHYS
    from nwb4fp.postprocess.add_wfcor import add_wf_cor

    base_path = Path("Q:/Sachuriga/Sachuriga_Python")
    base_data_folder = Path("S:/Sachuriga/")
    project_path = fr"{base_path}/quality_metrix/"
    sys.path.append(fr"{project_path}/quality_metrix")

    # change to project root
    sys.path.append(project_path)

    from nwb4fp.preprocess.load_data import load_data
    from nwb4fp.postprocess.quality_metrix import qualitymetrix
    from nwb4fp.postprocess.nwbPHYnOPHYS import nwbPHYnOPHYS
    from nwb4fp.postprocess.add_wfcor import add_wf_cor
    # set params for nwb
    sex = "F"
    animals = ["65588"] 
    age = "P45+"
    species = "Mus musculus"
    vedio_search_directory = base_data_folder/fr"Ephys_Vedio/CR_CA1/"
    path_save = base_data_folder/fr"nwb"
    run_qmnwb(animals,base_data_folder,sex,age,species,vedio_search_directory,path_save)

def run_qmnwb(animals,base_data_folder,sex,age,species,vedio_search_directory,path_save):
    for indvi in animals:
        ID = indvi
        counter = 0
        #getting sorted files02
        folder_path = fr"{str(base_data_folder)}/Ephys_Recording/CR_CA1/{ID}/"
        ##for quality metrix
        sorted_files = load_data(folder_path, file_suffix='_phy_k')

        for file in sorted_files[-1:]:
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