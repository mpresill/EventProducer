import os

folders = [
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHIm__cHB_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHIm__cHBtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHIm__cHWB_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHIm__cHWBtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHIm__cHW_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHIm__cHWtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHIm_m1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHIm_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHRe__ceHIm_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHRe__cHB_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHRe__cHBtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHRe__cHWB_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHRe__cHWBtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHRe__cHW_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHRe__cHWtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHRe_m1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_ceHRe_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHB__cHBtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHB__cHWB_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHB__cHWBtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHB__cHW_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHB__cHWtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHB_m1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHB_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHBtil__cHWB_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHBtil__cHWBtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHBtil__cHW_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHBtil__cHWtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHBtil_m1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHBtil_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHWB__cHWBtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHWB_m1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHWB_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHWBtil_m1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHWBtil_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHW__cHWB_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHW__cHWBtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHW__cHWtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHW_m1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHW_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHWtil__cHWB_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHWtil__cHWBtil_p1_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHWtil_m1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_cHWtil_p1_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_sm_ecm240/",
"/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/NovCampaign/mg_ee_fftata_sm_ecm240/"
]

for folder in folders:
    if os.path.isdir(folder):
        count = len([
            f for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f))
        ])
        print(f"{folder}: {count} files")
    else:
        print(f"{folder}: directory does not exist")
