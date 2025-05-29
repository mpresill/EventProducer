#!/bin/bash
export EOS_MGM_URL="root://eospublic.cern.ch"
echo "Starting job on " `date` # Date/time of start of job
echo "Running on: `uname -a`" # Condor job is running on this node
echo "System software: `cat /etc/redhat-release`" # Operating System on that node

source /cvmfs/sw.hsf.org/spackages6/key4hep-stack/2022-12-23/x86_64-centos7-gcc11.2.0-opt/ll3gi/setup.sh
export LC_ALL=C; unset LANGUAGE

# Prendere gli argomenti passati
JOB_ID="${1}_${2}"
if [ -z "$JOB_ID" ]; then
    JOB_ID=$(date +%s%N)  # Fallback al timestamp univoco
fi
echo "job id: ${JOB_ID}"

INPUT_FILE="input_${JOB_ID}.lhe.gz"
TEMP_FILE="temp_${JOB_ID}.lhe"
OUTPUT_TMP="temp_${JOB_ID}.root"

# Copiare il file di input e decomprimere
echo "Copying lhe.gz locally, and unzipping"
cp input_file "${INPUT_FILE}"
gunzip -c "${INPUT_FILE}" > "${TEMP_FILE}"
echo "tmp file is called ${TEMP_FILE}"

# Eseguire il comando DelphesPythia8_EDM4HEP
echo "Launching DelphesPythia8_EDM4HEP"
# Nome del file da modificare
FILE_CMD="pythia_proc.cmd"
# Sostituisci il percorso in Beams:LHEF nel file di configurazione
sed -i "s|^Beams:LHEF = .*|Beams:LHEF = ${TEMP_FILE}|" "$FILE_CMD"
DelphesPythia8_EDM4HEP card_IDEA.tcl edm4hep_IDEA.tcl ${FILE_CMD} ${OUTPUT_TMP}
cp ${OUTPUT_TMP} output_file

# Pulizia (facoltativa)
rm "${TEMP_FILE}" "${INPUT_FILE}" ${OUTPUT_TMP}
echo "Done!"
