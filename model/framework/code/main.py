# imports
import os
import csv
import sys
from rdkit import Chem
import numpy as np
from biosynfoni import Biosynfoni
from ersilia_pack_utils.core import write_out, read_smiles

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


# Read smiles
_, smiles_list = read_smiles(input_file)

# run model
outputs = biosynfoni_fingerprint(smiles_list)

#check input and output have the same lenght
input_len = len(smiles_list)
output_len = len(outputs)
assert input_len == output_len

# Write output
write_out(outputs, HEADER, output_file, np.float32)