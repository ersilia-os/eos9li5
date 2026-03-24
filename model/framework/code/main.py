# imports
import os
import csv
import sys
from rdkit import Chem
from biosynfoni import Biosynfoni

# parse arguments
input_file = sys.argv[1]
output_file = sys.argv[2]

# current file directory
root = os.path.dirname(os.path.abspath(__file__))

# 39-dimensional BioSynFoni fingerprint (full_1103 version)
FP_SIZE = 39
HEADER = ["feat_{:02d}".format(i) for i in range(FP_SIZE)]

# my model
def biosynfoni_fingerprint(smiles_list):
    results = []
    for smi in smiles_list:
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            results.append([None] * FP_SIZE)
        else:
            results.append(Biosynfoni(mol).fingerprint)
    return results


# read SMILES from .csv file, assuming one column with header
with open(input_file, "r") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    smiles_list = [r[0] for r in reader]

# run model
outputs = biosynfoni_fingerprint(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# write output in a .csv file
with open(output_file, "w") as f:
    writer = csv.writer(f)
    writer.writerow(HEADER)
    for o in outputs:
        writer.writerow(o)
