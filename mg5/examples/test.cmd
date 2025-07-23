test commands from Matteo (from lxplus):
###--model mg5/models/loop_sm_hh.tar commented out for now
#python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_zh_ecm240 --mg5card mg5/examples/mg_ee_zh.mg5  -N 2 -n 100 -q nextweek
#python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_eetata_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/eeh_sm_test.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 1 -n 1 -q nextweek


    ###### electron Z decay (1M events)
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_eetata_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/eeh_sm.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 10 -n 100000 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_eetata_smeft_cehim_p1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/eeh_smeft_cehim_p1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 100 -n 10000 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_eetata_smeft_cehim_m1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/eeh_smeft_cehim_m1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 100 -n 10000 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_eetata_smeft_cehre_m1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/eeh_smeft_cehre_m1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 100 -n 10000 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_eetata_smeft_cehre_p1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/eeh_smeft_cehre_p1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 100 -n 10000 -q nextweek


    ###### muon Z decay (1M events)
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_mumutata_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/mumuh_sm.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 1 -n 100 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_mumutata_smeft_cehim_p1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/mumuh_smeft_cehim_p1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 100 -n 10000 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_mumutata_smeft_cehim_m1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/mumuh_smeft_cehim_m1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 100 -n 10000 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_mumutata_smeft_cehre_m1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/mumuh_smeft_cehre_m1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 100 -n 10000 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_mumutata_smeft_cehre_p1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/mumuh_smeft_cehre_p1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 100 -n 10000 -q nextweek


    ###### quark Z decay (1M events)
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_jjtata_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/jjh_sm.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 10 -n 100000 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_jjtata_smeft_cehim_p1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/jjh_smeft_cehim_p1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 100 -n 10000 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_jjtata_smeft_cehim_m1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/jjh_smeft_cehim_m1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 100 -n 10000 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_jjtata_smeft_cehre_m1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/jjh_smeft_cehre_m1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 100 -n 10000 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_jjtata_smeft_cehre_p1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/jjh_smeft_cehre_p1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 100 -n 10000 -q nextweek



python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_eetata_smeft_cehim_p1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP/eeh_smeft_cehim_p1_max1prong_hadronic.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO.tar -N 100 -n 1000 -q workday



### test in corso ad inizio luglio 
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_eetata_mod1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP_21July2025/eeh_sm_mod1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO_v2.tar -N 100 -n 10000 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_eetata_mod1_smeft_cehim_m1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP_21July2025/eeh_sm_cehim_m1_mod1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO_v2.tar -N 100 -n 10000 -q nextweek
python3 bin/run.py --FCCee --LHE --send --condor --typelhe mg -p mg_ee_eetata_mod1_smeft_cehim_p1_ecm240 --mg5card mg5/examples/mg_ee_htatau_CP_21July2025/eeh_sm_cehim_p1_mod1.mg5 --model mg5/models/SMEFTsim_topU3l_MwScheme_UFO__taudecay_UFO_v2.tar -N 100 -n 10000 -q nextweek
