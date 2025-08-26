#!/bin/bash

DIR1="/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/lhe/"
DIR2="/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/"

echo "Checking size of: $DIR1"
du -sh "$DIR1"

echo "Checking size of: $DIR2"
du -sh "$DIR2"