import spikeinterface as si
import spikeinterface.extractors as se
import spikeinterface.postprocessing as post
from postprocess.get_potential_merge import get_potential_merge
from spikeinterface.preprocessing import (bandpass_filter,
                                           common_reference)
import spikeinterface.exporters as sex
import spikeinterface.qualitymetrics as sqm
from pathlib import Path

def main() -> object:
    """
    :rtype: object
    """
    print("main")
def qualitymetrix(path):

    sorting = se.read_phy(folder_path=path, load_all_cluster_properties=True,exclude_cluster_groups = ["noise", "mua"])
    global_job_kwargs = dict(n_jobs=24, chunk_size=10000, chunk_duration="1s", total_memory="32G")
    si.set_global_job_kwargs(**global_job_kwargs)
    temp_path = path.split("_phy")
    raw_path = temp_path[0]
    stream_name = 'Record Node 101#OE_FPGA_Acquisition_Board-100.Rhythm Data'
    try:
        recording = se.read_openephys(raw_path, stream_name=stream_name, load_sync_timestamps=True)
    except AssertionError:
        try:
            stream_name = 'Record Node 102#OE_FPGA_Acquisition_Board-101.Rhythm Data'
            recording = se.read_openephys(raw_path, stream_name=stream_name, load_sync_timestamps=True)
        except AssertionError:
            stream_name = 'Record Node 101#Acquisition_Board-100.Rhythm Data'
            recording = se.read_openephys(raw_path, stream_name=stream_name, load_sync_timestamps=True)

    import probeinterface as pi

    # from probeinterface import plotting
    manufacturer = 'cambridgeneurotech'
    probe_name = 'ASSY-236-F'
    probe = pi.get_probe(manufacturer, probe_name)
    print(probe)
    # probe.wiring_to_device('cambridgeneurotech_mini-amp-64')
    # map channels to device indices
    mapping_to_device = [
        # connector J2 TOP
        41, 39, 38, 37, 35, 34, 33, 32, 29, 30, 28, 26, 25, 24, 22, 20,
        46, 45, 44, 43, 42, 40, 36, 31, 27, 23, 21, 18, 19, 17, 16, 14,
        # connector J1 BOTTOM
        55, 53, 54, 52, 51, 50, 49, 48, 47, 15, 13, 12, 11, 9, 10, 8,
        63, 62, 61, 60, 59, 58, 57, 56, 7, 6, 5, 4, 3, 2, 1, 0
    ]

    probe.set_device_channel_indices(mapping_to_device)
    probe.to_dataframe(complete=True).loc[:, ["contact_ids", "shank_ids", "device_channel_indices"]]
    probegroup = pi.ProbeGroup()
    probegroup.add_probe(probe)

    pi.write_prb(f"{probe_name}.prb", probegroup, group_mode="by_shank")
    recording_prb = recording.set_probe(probe, group_mode="by_shank")
    rec = bandpass_filter(recording_prb, freq_min=300, freq_max=6000)
    rec_save = common_reference(rec, reference='global', operator='median')

    sorting.set_property(key='group', values = sorting.get_property("channel_group"))

    wf = si.extract_waveforms(rec_save, sorting, folder='C:/temp_waveform/', overwrite=True, 
                              sparse=True, method="by_property",by_property="group",max_spikes_per_unit=1000)
    
    #get potential merging sorting objects
    print("processing potential merge...\n")
    
    sort_merge = get_potential_merge(sorting, wf)
    wfm = si.extract_waveforms(rec_save, sort_merge, folder='C:/temp_waveform/', overwrite=True, 
                              sparse=True, method="by_property",by_property="group",max_spikes_per_unit=1000)


    spike_locations = post.compute_unit_locations(waveform_extractor=wfm,
                                                   method= 'monopolar_triangulation',
                                                  radius_um=50.)

    from spikeinterface.postprocessing import compute_principal_components,compute_template_metrics
    compute_principal_components(waveform_extractor=wfm,n_components=3,whiten=True,mode='by_channel_local',dtype='float64')
    compute_template_metrics(wfm)
    qm_params = sqm.get_default_qm_params()
    qm_params["nn_isolation"]["max_spikes"]=10000
    sqm.compute_quality_metrics(waveform_extractor=wfm, qm_params=qm_params,sparsity=wf.sparsity, skip_pc_metrics=False)
    print("completet!!!!automerge & quality_metrix_part")

    path_iron = Path(path + "_manual")
    sex.export_to_phy(waveform_extractor=wfm,
                      output_folder = path_iron,
                      remove_if_exists=True,
                      copy_binary=True)

    wfm.save(Path(path + "_manual/waveforms"), format='binary')
    print("completet!!!!_export_to_phy_part")
if __name__ == "__main__":
    main()