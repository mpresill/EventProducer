#!/usr/bin/env python3
import pylhe
import pandas as pd
from tqdm import tqdm
import gzip
import glob
import re

#   
#   per far funzionare pylhe su lxplus ho creato un virtual env
#   python3 -m venv lhe_env
#   source lhe_env/bin/activate
#   pip install pylhe pandas tqdm
#
#   python3 lhe_cross-section_pylhe.py
#
#   per uscire poi, deactivate come solito


lhe_files = sorted(glob.glob("/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/lhe/wMadspin/llh-*.lhe.gz"))

results = []

for lhe in tqdm(lhe_files, desc="Processing LHE files"):
    try:
        with gzip.open(lhe, 'rt') as f:
            content = f.read()
            # Cerca la riga che contiene "Integrated weight (pb)"
            match = re.search(r'Integrated weight \(pb\)\s*:\s*([0-9.eE+-]+)', content)
            if match:
                xsec = float(match.group(1))
            else:
                xsec = None
            results.append({'file': lhe, 'xsection_pb': xsec})
    except Exception as e:
        results.append({'file': lhe, 'xsection_pb': None})
        print(f"Errore su {lhe}: {e}")

df = pd.DataFrame(results)
df.to_csv('lhe_cross_sections_correct.csv', index=False)
print(df)