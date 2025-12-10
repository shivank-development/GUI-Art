import pubchempy as pcp

# Ask user for a chemical name
chemical_name = input("Enter chemical name: ")

try:
    # Fetch compound details from PubChem
    compound = pcp.get_compounds(chemical_name, 'name')[0]

    print(f"IUPAC Name: {compound.iupac_name}")
    print(f"Common Name: {compound.synonyms[0]}")
    print(f"Molecular Weight: {compound.molecular_weight}")
    print(f"Formula: {compound.molecular_formula}")

except IndexError:
    print(f"No information found for '{chemical_name}'.")
