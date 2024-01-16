
# DNA ToolKit/Code testing file
from DNAToolKit import *

rndDNAStr = "ATTGCTCATTAGGTACGATC"

print(validateSeq(rndDNAStr))

# -- Output -- #
# ATTGCTCATTAGGTACGATC #
# ------------ #


# DNA ToolKit/Code testing file
from DNAToolKit import *

rndDNAStr2 = "ATTCGCTGAGGCCCccTaTTTAACGTAA"
print(validateSeq(rndDNAStr2))

# -- Output -- #
# ATTCGCTGAGGCCCCCTATTTAACGTAA
# ------------ #


# DNA ToolKit/Code testing file
from DNAToolKit import *

rndDNAStr3 = "ATTCGCTGAGGXCCccTaTTTAACGTAAX"
print(validateSeq(rndDNAStr3))

# -- Output -- #
# False #
# ------------ #





