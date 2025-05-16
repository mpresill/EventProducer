test commands from Matteo (from lxplus):
###--model mg5/models/loop_sm_hh.tar commented out for now
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_zh_ecm240 --mg5card mg5/examples/mg_ee_zh.mg5  -N 2 -n 100 -q workday

python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_eetata_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/eeh_sm_test.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 1 -n 1 -q workday
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_eetata_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/eeh_sm.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 1000 -n 1000000 -q workday