# DNA Toolset/Code testing file
from DNAToolKit import *
import random

# Creating a random DNA sequence for testing:
randDNAStr = ''.join([random.choice(Nucleotides)for nuc in range(20)])

print(validateSeq(rndDNAStr))

# -- Output -- #
# ATTGCTCATTAGGTACGATCAAAAATTCGCTTAAGCCTTAAGGCAATTTAAACGCGGCTAA
# ------------ #
