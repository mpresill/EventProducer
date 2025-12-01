#!/usr/bin/env python3
import pylhe
import pandas as pd
from tqdm import tqdm
import gzip
import glob
import re
import os

#   
#   To make pylhe work on lxplus, create a virtual environment:
#   python3 -m venv lhe_env
#   source lhe_env/bin/activate  # inside a clean cmsenv
#   pip install pylhe pandas tqdm
#
#   Run with:
#   python3 lhe_cross-section_pylhe.py
#
#   deactivate when done

# File list
lhe_files = sorted(
    glob.glob("/eos/experiment/fcc/ee/analyses_storage/Higgs_and_TOP/HiggsTauTau/ecm240/MCgenCP/lhe/NovCampaign/*/*.lhe.gz")
)

results = []

for lhe in tqdm(lhe_files, desc="Processing LHE files"):
    try:
        with gzip.open(lhe, 'rt') as f:
            content = f.read()

        # Number of events
        n_events = pylhe.read_num_events(lhe)

        # Cross section (pb)
        match = re.search(r'Integrated weight \(pb\)\s*:\s*([0-9.eE+-]+)', content)
        xsec = float(match.group(1)) if match else None

        results.append({
            'file': lhe,
            'xsection_pb': xsec,
            'n_events': n_events
        })

    except Exception as e:
        print(f"Error on {lhe}: {e}")
        results.append({'file': lhe, 'xsection_pb': None, 'n_events': None})


# Build initial dataframe
df = pd.DataFrame(results)

# Extract base path (full directory)
df['basepath'] = df['file'].apply(os.path.dirname)

# Group by basepath and compute mean of numeric columns
df_grouped = (
    df.groupby('basepath')
      .mean(numeric_only=True)
      .reset_index()
)

# Save ONLY the grouped results
df_grouped.to_csv('lhe_cross_sections_grouped_1Dec25.csv', index=False)

print("\nGrouped dataframe:")
print(df_grouped)
