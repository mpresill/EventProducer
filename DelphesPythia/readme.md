## Run locally delphes+pythia on LHE file:
`source /cvmfs/sw.hsf.org/spackages6/key4hep-stack/2022-12-23/x86_64-centos7-gcc11.2.0-opt/ll3gi/setup.sh``

`DelphesPythia8_EDM4HEP card_IDEA.tcl edm4hep_IDEA.tcl pythia_proc.cmd /eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/test/test_output.root``
where the path of the input `.lhe` file is encoded in the `.cmd` file.
 
## Submit delphes+pythia on condor:

everything is encoded in submit.py, read it and adapt it, then submit with 
``python submit.py`
