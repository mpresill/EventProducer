#!/bin/bash

# funziona come segue:

#  source /cvmfs/sw.hsf.org/spackages6/key4hep-stack/2022-12-23/x86_64-centos7-gcc11.2.0-opt/ll3gi/setup.sh
# ./launch_pythiaDelphes.sh /new/path/to/test.lhe output_file.root
#				/ceph/mpresill/FCCee/ZH_SMEFT_LO_noISR_noCuts_prod/mu/ pythia_cmd.cmd

# Controlla se il numero di argomenti è corretto
if [ "$#" -ne 2 ]; then
    echo "Uso: $0 <nuovo_percorso_LHEF.gz> <nome_output_root>"
    exit 1
fi

# Assegna gli argomenti a variabili
PERCORSO_LHEF_GZ=$1
NOME_OUTPUT_ROOT=$2
FILE_CMD=$3

# Verifica se il file è un archivio .gz
if [[ "$PERCORSO_LHEF_GZ" == *.gz ]]; then
    # Decomprimi il file
    gunzip -k "$PERCORSO_LHEF_GZ"
    # Rimuove l'estensione .gz per ottenere il percorso decompr
    NUOVO_PERCORSO_LHEF="${PERCORSO_LHEF_GZ%.gz}"
else
    echo "Il file fornito non è un file .gz."
    NUOVO_PERCORSO_LHEF=$1
fi

# Esegui il comando DelphesPythia8_EDM4HEP
#source /cvmfs/sw.hsf.org/spackages6/key4hep-stack/2022-12-23/x86_64-centos7-gcc11.2.0-opt/ll3gi/setup.sh
DelphesPythia8_EDM4HEP card_IDEA.tcl edm4hep_IDEA.tcl "$FILE_CMD" "$NOME_OUTPUT_ROOT"


