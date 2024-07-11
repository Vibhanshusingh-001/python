from rdkit import Chem
from rdkit.Chem import Draw

# Define a SMILES string for a molecule
smiles = 'CCO'

# Create a molecule object from the SMILES string
mol = Chem.MolFromSmiles(smiles)

# Generate 2D coordinates for the molecule
Chem.Compute2DCoords(mol)

# Draw the molecule
Draw.MolToImage(mol)
