# DNA Toolkit file
import collections
Nucleotides = ("A", "C", "G", "T")
DNAReverseComplement = {"A": "T", "T": "A", "G": "C", "C": "G"}
DNAStr = "ATTGCTCATTAGGTACGATCAAAAATTCGCTTAAGCCTTAAGGCAATTTAAACGCGGCTAA"


# GC Content Calculation
def gc_content(seq):
    return round((seq.count('C') + seq.count('G')) /len(seq) * 100)

print(f'[5] + GC Content: {gc_content(DNAStr)}%\n' )

# ----Output----#
# [5] + GC Content: 38%
# --------------#