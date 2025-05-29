import os
import shutil
import subprocess


# Lista delle directory
Direct = [
#    "mg_ee_eetata_ecm240",                 
    "mg_ee_jjtata_smeft_cehim_p1_ecm240",
    "mg_ee_jjtata_smeft_cehre_m1_ecm240",
#    "mg_ee_eetata_smeft_cehim_m1_ecm240",  
    "mg_ee_jjtata_smeft_cehre_p1_ecm240",
#    "mg_ee_eetata_smeft_cehim_p1_ecm240",  
#    "mg_ee_mumutata_ecm240",
#    "mg_ee_eetata_smeft_cehre_m1_ecm240",  
#    "mg_ee_mumutata_smeft_cehim_m1_ecm240",
#    "mg_ee_eetata_smeft_cehre_p1_ecm240",  
#    "mg_ee_mumutata_smeft_cehim_p1_ecm240",
    "mg_ee_jjtata_ecm240",                 
#    "mg_ee_mumutata_smeft_cehre_m1_ecm240",
    "mg_ee_jjtata_smeft_cehim_m1_ecm240",  
#    "mg_ee_mumutata_smeft_cehre_p1_ecm240"
]

# Creazione della cartella "Direct" nella directory corrente
local_base_dir = os.getcwd()
os.makedirs(local_base_dir, exist_ok=True)

# Percorso alle directory remote di input
base_input_dir = '/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/lhe/'
base_output_dir = '/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/DelphesPythia8_EDM4HEP/'

cwd = os.getcwd()
for direc in Direct:
    print(f"Processing directory: {direc}")

    # Percorsi delle directory di input e output locale e output del root file
    remote_input_dir = os.path.join(base_input_dir, direc)
    local_output_dir = os.path.join(local_base_dir, direc)
    eos_output_dir = os.path.join(base_output_dir, direc)
    os.makedirs(local_output_dir, exist_ok=True)
    os.makedirs(eos_output_dir, exist_ok=True)

    # Processa i file .lhe.gz nella directory remota
    for file in os.listdir(remote_input_dir):
        if file.endswith('.lhe.gz'):
            sample = file.replace('.lhe.gz', '')  # Nome del campione senza estensione
            full_path = os.path.join(remote_input_dir, sample)  # Rimuove .gz dal percorso

            # Copia e modifica pythia_proc.cmd
            pythia_cmd_file = 'pythia_proc.cmd'
            pythia_cmd_sample_file = os.path.join(local_output_dir, f'pythia_proc_{sample}.cmd')
            shutil.copyfile(pythia_cmd_file, pythia_cmd_sample_file)

#            with open(pythia_cmd_file, 'r') as cmd_in, open(pythia_cmd_sample_file, 'w') as cmd_out:
#                for line in cmd_in:
#                    if 'Beams:LHEF =' in line:
#                        cmd_out.write(f'Beams:LHEF = {full_path}.lhe\n')  # Senza virgolette
#                    else:
#                        cmd_out.write(line)

            # Modifica e copia wrapper.sh
            wrapperFile = 'wrapper.sh'
            wrapperFile_new = os.path.join(local_output_dir, f'{sample}_wrapper.sh')
            with open(wrapperFile, 'r') as filein, open(wrapperFile_new, "wt") as fileout:
                for line in filein:
                    # Sostituisci entrambi i placeholder in una singola riga
                    line = line.replace('input_file', os.path.join(remote_input_dir,f'{sample}.lhe.gz'))
                    line = line.replace('output_file', os.path.join(eos_output_dir,f'{sample}.root'))
                    line = line.replace('pythia_proc.cmd', f'pythia_proc_{sample}.cmd')
                    fileout.write(line)

            # Modifica e copia submit.jdl
            jdlFile = 'submit.jdl'
            jdlFile_new = os.path.join(local_output_dir, f'{sample}_submit.jdl')
            with open(jdlFile, 'r') as filein, open(jdlFile_new, "wt") as fileout:
                for line in filein:
                    # Sostituisci entrambi i placeholder in una singola riga
                    line = line.replace('wrapper.sh', f'{sample}_wrapper.sh')
                    line = line.replace('pythia_proc.cmd', f'pythia_proc_{sample}.cmd')
                    fileout.write(line)

            print(f"Prepared files for sample: {sample} in directory: {local_output_dir}")

            os.chdir(local_output_dir)
            subprocess.run("condor_submit {}_submit.jdl".format(sample), shell=True, check=True)
            os.chdir(cwd)

    print(f"Finished processing directory: {direc}, and submitted to HT-condor")

