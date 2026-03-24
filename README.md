# Biosynfoni natural product fingerprint

BioSynFoni is a biosynthesis-informed count-based molecular fingerprint designed for natural product research. It decomposes molecules into 39 biosynthetic building block substructures derived from Dewicks classification of natural product biosynthetic pathways. The fingerprint is computed via SMARTS substructure matching using RDKit and returns an integer count vector. It was shown to outperform MACCS, Morgan, and Daylight-like fingerprints for biosynthetic distance estimation and performs comparably for natural product classification while being more compact and interpretable.



## Information
### Identifiers
- **Ersilia Identifier:** `eos9li5`
- **Slug:** `biosynfoni`

### Domain
- **Task:** `Representation`
- **Subtask:** `Featurization`
- **Biomedical Area:** `Any`
- **Target Organism:** `Any`
- **Tags:** `Fingerprint`, `Natural product`

### Input
- **Input:** `Compound`
- **Input Dimension:** `1`

### Output
- **Output Dimension:** `39`
- **Output Consistency:** `Fixed`
- **Interpretation:** Each of the 39 output values is a count of how many times a specific biosynthetic building block substructure was matched in the input molecule. Higher counts indicate a greater presence of that biosynthetic unit.

Below are the **Output Columns** of the model:
| Name | Type | Direction | Description |
|------|------|-----------|-------------|
| feat_00 | integer | high | Count of coenzyme A (CoA) substructure matches |
| feat_01 | integer | high | Count of NADH coenzyme substructure matches |
| feat_02 | integer | high | Count of NADPH coenzyme substructure matches |
| feat_03 | integer | high | Count of standard amino acid substructure matches |
| feat_04 | integer | high | Count of non-standard amino acid substructure matches |
| feat_05 | integer | high | Count of open-chain pyranose C6O6 sugar matches |
| feat_06 | integer | high | Count of open-chain furanose C5O5 sugar matches |
| feat_07 | integer | high | Count of cyclic pyranose C5O4 sugar matches |
| feat_08 | integer | high | Count of cyclic furanose C4O3 sugar matches |
| feat_09 | integer | high | Count of indole-C2N 12-atom polyketide/NRP building block matches |

_10 of 39 columns are shown_
### Source and Deployment
- **Source:** `Local`
- **Source Type:** `External`

### Resource Consumption


### References
- **Source Code**: [https://github.com/lucinamay/biosynfoni](https://github.com/lucinamay/biosynfoni)
- **Publication**: [https://doi.org/10.1186/s13321-025-01081-6](https://doi.org/10.1186/s13321-025-01081-6)
- **Publication Type:** `Peer reviewed`
- **Publication Year:** `2025`
- **Ersilia Contributor:** [GemmaTuron](https://github.com/GemmaTuron)

### License
This package is licensed under a [GPL-3.0](https://github.com/ersilia-os/ersilia/blob/master/LICENSE) license. The model contained within this package is licensed under a [MIT](LICENSE) license.

**Notice**: Ersilia grants access to models _as is_, directly from the original authors, please refer to the original code repository and/or publication if you use the model in your research.


## Use
To use this model locally, you need to have the [Ersilia CLI](https://github.com/ersilia-os/ersilia) installed.
The model can be **fetched** using the following command:
```bash
# fetch model from the Ersilia Model Hub
ersilia fetch eos9li5
```
Then, you can **serve**, **run** and **close** the model as follows:
```bash
# serve the model
ersilia serve eos9li5
# generate an example file
ersilia example -n 3 -f my_input.csv
# run the model
ersilia run -i my_input.csv -o my_output.csv
# close the model
ersilia close
```

## About Ersilia
The [Ersilia Open Source Initiative](https://ersilia.io) is a tech non-profit organization fueling sustainable research in the Global South.
Please [cite](https://github.com/ersilia-os/ersilia/blob/master/CITATION.cff) the Ersilia Model Hub if you've found this model to be useful. Always [let us know](https://github.com/ersilia-os/ersilia/issues) if you experience any issues while trying to run it.
If you want to contribute to our mission, consider [donating](https://www.ersilia.io/donate) to Ersilia!
