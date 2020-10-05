from molemass import *
mol=["CHHCHH","COHF","KNOOO"]
for mol in mols:
    print("%s MW= %f"%(mol,molemass(mol)))